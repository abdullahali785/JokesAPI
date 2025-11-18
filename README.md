# 🤖 Jokes API

A RESTful Flask API that provides jokes by **language**, **category**, **number**, or **specific joke ID**.  
Uses the `pyjokes` package and supports cross-origin access.

---

## 📦 Features

- Factory + Blueprint architecture
- Loads jokes from `pyjokes` in configured languages
- Ordering rules:
  1. Alphabetical language code (`es` before `eu`)
  2. Neutral jokes before Chuck Norris jokes
- Endpoints:
  - `/api/v1/jokes/<lang>/<category>/<number>`
  - `/api/v1/jokes/<id>`
- Returns:
  - JSON list for multi-joke queries  
  - JSON object for joke by ID
- Clean 404 error messages
- `@cache` for performance
- Fully [deployed online](https://abdullahali785.github.io/Jokes/)

---

## 🛠️ Tech Stack

- Python 3  
- Flask  
- pyjokes  
- Render [https://jokesapi-cl97.onrender.com/]

---
