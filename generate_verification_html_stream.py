import re
import json

dummy_data = {
    "detailed": {"columns": [], "values": {}, "length": 0},
    "history": {"columns": [], "values": {}, "length": 0},
    "clients": {"columns": [], "values": {}, "length": 0},
    "byOrder": [],
    "stockMap05": {},
    "stockMap08": {},
    "innovationsMonth": [],
    "activeProductCodes": [],
    "productDetails": {},
    "passedWorkingDaysCurrentMonth": 1,
    "isColumnar": True
}
dummy_json = json.dumps(dummy_data)

input_path = 'EXPORTADOR DASH V7.html'
output_path = 'verification_dashboard.html'

# Step 1: Extract logic script
logic_script = ""
with open(input_path, 'r', encoding='utf-8') as f:
    content = f.read()
    match = re.search(r'<script id="report-logic-script" type="text/template">(.*?)</script>', content, re.DOTALL)
    if match:
        logic_script = match.group(1)

if not logic_script:
    print("Logic script not found")
    exit(1)

# Step 2: Stream copy template
start_marker = "const reportTemplate = `"
end_marker = "`;"
is_inside_template = False
buffer = ""

with open(input_path, 'r', encoding='utf-8') as fin, open(output_path, 'w', encoding='utf-8') as fout:
    while True:
        chunk = fin.read(1024)
        if not chunk:
            break

        buffer += chunk

        if not is_inside_template:
            idx = buffer.find(start_marker)
            if idx != -1:
                is_inside_template = True
                # Move buffer cursor to after marker
                buffer = buffer[idx + len(start_marker):]

        if is_inside_template:
            if '${jsonDataString}' in buffer:
                buffer = buffer.replace('${jsonDataString}', dummy_json)

            if '${scriptLogic}' in buffer:
                parts = buffer.split('${scriptLogic}')
                fout.write(parts[0])
                fout.write(logic_script)
                buffer = parts[1]

            end_idx = buffer.find(end_marker)
            if end_idx != -1:
                fout.write(buffer[:end_idx])
                break

            safe_len = len(buffer) - 20
            if safe_len > 0:
                fout.write(buffer[:safe_len])
                buffer = buffer[safe_len:]

print("Generated.")
