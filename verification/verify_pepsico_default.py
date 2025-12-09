from playwright.sync_api import sync_playwright
import os

def test_pepsico_default():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        cwd = os.getcwd()
        page.goto(f"file://{cwd}/verification_dashboard.html")
        page.wait_for_timeout(2000)

        # Check initial state of buttons
        pepsico_btn = page.locator("#goals-category-pepsico-btn")
        elma_btn = page.locator("#goals-category-elmachips-btn")

        pepsico_class = pepsico_btn.get_attribute("class")
        elma_class = elma_btn.get_attribute("class")

        print(f"PEPSICO Btn Class: {pepsico_class}")

        if "bg-[#0d9488]" in pepsico_class:
            print("SUCCESS: PEPSICO button is active.")
        else:
            print("FAILURE: PEPSICO button is not active.")

        if "bg-[#334155]" in elma_class:
            print("SUCCESS: ELMA button is inactive.")
        else:
            print("FAILURE: ELMA button is not inactive.")

        # Check sub-tabs visibility
        pepsico_tabs = page.locator("#goals-sub-tabs-pepsico")
        elma_tabs = page.locator("#goals-sub-tabs-elmachips")

        pepsico_tabs_class = pepsico_tabs.get_attribute("class")
        elma_tabs_class = elma_tabs.get_attribute("class")

        if "hidden" in pepsico_tabs_class:
             print("FAILURE: PEPSICO sub-tabs are hidden.")
        else:
             print("SUCCESS: PEPSICO sub-tabs are visible.")

        if "hidden" not in elma_tabs_class:
             print("FAILURE: ELMA sub-tabs are visible.")
        else:
             print("SUCCESS: ELMA sub-tabs are hidden.")

        page.screenshot(path="verification/pepsico_default_final.png")
        browser.close()

if __name__ == "__main__":
    test_pepsico_default()
