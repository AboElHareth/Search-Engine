import requests
from bs4 import BeautifulSoup
import os

# إعدادات

START_URL = "https://quotes.toscrape.com"
MAX_PAGES = 100
OUTPUT_FOLDER = "Data"

# إنشاء فولدر
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

visited = set()
to_visit = [START_URL]

count = 0

def clean_text(text):
    return " ".join(text.split())

while to_visit and count < MAX_PAGES:
    url = to_visit.pop(0)

    if url in visited:
        continue

    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        text = clean_text(soup.get_text())

        # تجاهل الصفحات الصغيرة
        if len(text) < 200:
            continue

        # اسم الملف
        filename = f"doc{count}.txt"
        filepath = os.path.join(OUTPUT_FOLDER, filename)

        # تخزين
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"URL: {url}\n")
            f.write(f"CONTENT: {text}\n")

        print(f"Saved: {filename}")

        visited.add(url)
        count += 1

        # استخراج لينكات جديدة
        for link in soup.find_all("a"):
            href = link.get("href")

            if href and href.startswith("http"):
                if href not in visited:
                    to_visit.append(href)

    except:
        continue

print("Finished!")