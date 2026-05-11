import os
import json

DATA_FOLDER = "Data"

doc_map = {}

for filename in os.listdir(DATA_FOLDER):
    filepath = os.path.join(DATA_FOLDER, filename)

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

        url = ""
        content = ""

        for line in lines:
            if line.startswith("URL:"):
                url = line.replace("URL:", "").strip()

            if line.startswith("CONTENT:"):
                content = line.replace("CONTENT:", "").strip()

        doc_map[filename] = {
            "url": url,
            "content": content
        }

# حفظ الملف النهائي
with open("Doc_Map.json", "w", encoding="utf-8") as f:
    json.dump(doc_map, f, indent=2)

print("Doc_Map.json created ✅")