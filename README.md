# 🔎 Mini Search Engine

A lightweight Search Engine built using Python and JavaScript that supports keyword search, phrase matching, result ranking, and highlighted search results through efficient text indexing and preprocessing techniques.

---

## 🚀 Features

* Keyword-based search
* Phrase search support
* Dynamic result ranking
* Highlight matched words
* Fast text indexing
* Document preprocessing using Python
* Lightweight and clean UI
* Efficient search experience

---

## 🛠️ Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend / Processing

* Python

---

## ⚙️ How It Works

The project processes and indexes text documents using Python scripts, then performs fast searching and result visualization using JavaScript.

### Main Concepts:

* Text Indexing
* Tokenization
* Text Preprocessing
* Phrase Matching
* Ranking System
* Regular Expressions
* Search Highlighting

## Note

Large dataset and generated JSON index files are excluded from the repository due to size limitations.

---

## 📂 Project Structure

```bash
├── index.html
├── style.css
├── script.js
├── links.py
├── inverted_index.py
├── mapping.py
├── inverted_index.json
├── doc_map.json
├── documents/
│   ├── doc1.txt
│   ├── doc2.txt
│   └── ...
```

---

## ▶️ Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/AboElHareth/Search-Engine.git
```

### 2. Run Python preprocessing/indexing

```bash
python links.py
python inverted_index.py
python mapping.py
```

### 3. Open the project

Run `index.html` in your browser.

---

## 💡 Future Improvements

* Add TF-IDF ranking
* Support fuzzy search
* Add filters and categories
* Improve ranking algorithms
* Add dark mode
* Connect to a real database
* Add search suggestions
