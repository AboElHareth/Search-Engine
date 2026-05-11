let index = {};
let docMap = {};

// =======================
// Load data files
// =======================

// inverted index
fetch("Inverted_Index.json")
    .then(res => res.json())
    .then(data => {
        index = data;
        console.log("Index loaded ✅");
    });

// doc map (url + content)
fetch("Doc_Map.json")
    .then(res => res.json())
    .then(data => {
        docMap = data;
        console.log("Doc map loaded ✅");
    });

// =======================
// Clean word
// =======================
function clean(word) {
    return word.toLowerCase().replace(/[^a-z]/g, "");
}

// =======================
// Highlight function
// =======================
function highlight(text, query) {
    let cleaned = query.trim().toLowerCase();

    let regex = new RegExp(`\\b${cleaned}\\b`, "gi");
    return text.replace(regex, "<mark>$&</mark>");
}

// =======================
// Search function
// =======================
function search() {
    let query = document.getElementById("searchBox").value;
    let cleaned = query.trim().toLowerCase();

    let results = {};

    
    if (cleaned.includes(" ")) {

        for (let doc in docMap) {
            let content = docMap[doc].content.toLowerCase();
            let regex = new RegExp(cleaned,"gi");
            let matches = content.match(regex);

            if (matches) {
                results[doc] = matches.length;
            }
        }

    } 
    
    else {
        let word = clean(cleaned);

        if (index[word]) {
            for (let doc in index[word]) {
                results[doc] = index[word][doc];
            }
        }
    }

    display(results, query);
}

// =======================
// Display results
// =======================
function display(results, query) {
    let container = document.getElementById("results");
    container.innerHTML = "";

    let sorted = Object.entries(results)
        .sort((a, b) => b[1] - a[1]);

    if (sorted.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <div class="empty-icon">🔍</div>
                <h3>No results found</h3>
                <p>Try searching for a different word or phrase.</p>
            </div>
        `;
        return;
    }

    // Results header
    let header = document.createElement("div");
    header.className = "results-header";
    header.innerHTML = `
        <span class="results-count"><strong>${sorted.length}</strong> result${sorted.length !== 1 ? 's' : ''} found</span>
    `;
    container.appendChild(header);

    sorted.forEach(([doc, score], i) => {

        let data = docMap[doc];
        if (!data) return;

        let url = data.url;
        let content = data.content;

        let highlighted = highlight(content, query);

        let div = document.createElement("div");
        div.className = "result";
        div.style.animationDelay = `${i * 0.05}s`;

        div.innerHTML = `
            <div class="result-url">
                <span class="result-url-dot"></span>
                <a href="${url}" target="_blank">${url}</a>
            </div>
            <p>${highlighted}</p>
            <div class="result-footer">
                <span class="score-badge">Score: ${score}</span>
                <a href="${url}" target="_blank" class="visit-link">Visit ↗</a>
            </div>
        `;

        container.appendChild(div);
    });
}