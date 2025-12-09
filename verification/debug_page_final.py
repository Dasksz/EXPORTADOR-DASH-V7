from playwright.sync_api import sync_playwright
import os

def debug_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/verification_dashboard.html")
        page.wait_for_timeout(2000)

        # Check if dashboard initialized
        if page.locator("#goals-category-pepsico-btn").count() > 0:
            print("Element FOUND")
        else:
            print("Element NOT FOUND")
            # Maybe look for error message
            content = page.content()
            if "Critical Error" in content:
                print("Critical Error found in page content")

        browser.close()

if __name__ == "__main__":
    debug_page()
