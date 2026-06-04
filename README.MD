<div align="center">

# 🎥 KinopoiskSearch

### A movie search site on the kinopoisk portal

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)]()
[![JavaScript](https://img.shields.io/badge/JavaScript-ES2016–ES2025%2B-blue.svg)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0%2B-blue.svg)]()
[![AsyncIO](https://img.shields.io/badge/Async-First-purple.svg)]()
[![Tests](https://img.shields.io/badge/tests-pytest-success.svg)]()
[![Architecture](https://img.shields.io/badge/architecture-clean-orange.svg)]()

</div>

# ✨ Features

## 🎥 User Features

- Top 250 movies
- Movie title search


# 🧱 Tech Stack

| Layer | Technology |
|------|------------|
| Language | Python 3.8+ |
| Language | JavasScript |
| Framework | FastAPI 0.111.0 |
| Validation | Pydantic |
| Config | pydantic-settings |
| Testing | Pytest |
| Async | asyncio |


# 📁 Project Structure

```text
KinopoiskSearch/
│── src/
│   ├── app/                # Application layer
│   ├── domain/             # Business logic
│   ├── core/               # Shared utilities
│   ├── setting/
│   └── tests/
│
├── tests/
├── mypy.ini/
├── pytest.ini/
├── pyproject.toml
└── README.md
```


## 🚀 Quick Start
### 1️⃣ Clone repository

```bash
git clone https://github.com/razielSan/KinopoiskSearch.git
cd KinopoiskSearch
```


### 2️⃣ Create virtual environment

Linux / macOS

```python
python -m venv venv
source venv/bin/activate

```
Windows

```python
python -m venv venv
venv\Scripts\activate
```


### 3️⃣ Install dependencies

```bash
pip install -e .
```

### ⚙️ Configuration

Create file:

```bash
src/app/kinopoisk/backend/.env
```

Example:

```.env
API_KEY=YOUR_API_KEY
```

### ▶️ Run Application

```bash
app
```


### 🧪 Testing

Run tests:

```bash
pytest tests
```

### 🤝 Contributing

Pull requests are welcome.

If you'd like to improve architecture, performance, or UX — feel free to open an issue.


### 📬 Contact

Telegram: @razielasus
