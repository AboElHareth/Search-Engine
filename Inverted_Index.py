import os
import re
import json

DATA_FOLDER = "Data"

index = {}

# 🔹 تنظيف الكلمة
def clean_word(word):
    return re.sub(r'[^a-zA-Z]', '', word).lower()

# قراءة كل الملفات
for filename in os.listdir(DATA_FOLDER):
    filepath = os.path.join(DATA_FOLDER, filename)

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

        # تجاهل أول سطر (URL)
        content = " ".join(lines[1:])

        words = content.split()

        for word in words:
            word = clean_word(word)

            if word == "":
                continue

            if word not in index:
                index[word] = {}

            if filename not in index[word]:
                index[word][filename] = 0

            index[word][filename] += 1

# حفظ في JSON
with open("Inverted_Index.json", "w", encoding="utf-8") as f:
    json.dump(index, f, indent=2)

print("Inverted Index Created ✅")