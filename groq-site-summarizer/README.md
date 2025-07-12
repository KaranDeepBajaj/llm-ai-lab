# Groq Stock Summary Analyzer 🧠📈

This project extracts the main content of a given stock or business webpage and summarizes it using Groq's LLaMA 4 Scout model.

## Features

- Web scraping with BeautifulSoup
- Cleaned text extraction (ignores scripts, styles, navbars, etc.)
- Smart summarization using Groq LLM
- Markdown-based formatted output

## Setup

1. Clone the repo
2. Install dependencies:
   ```bash
   pip install groq requests beautifulsoup4
