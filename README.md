# Web Data Extractor

A simple web scraping application built with Python and Streamlit. It allows users to extract headings, paragraphs, links, or elements matching a custom CSS selector from a website.

## Features

- Extract headings and paragraphs
- Collect website links and their URLs
- Use custom CSS selectors
- View extracted data in a table
- Download results as a CSV file
- Display the page title, HTTP status, and HTML size

## Tech Stack

- Python
- Streamlit
- Requests
- BeautifulSoup
- Pandas

## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd web-data-extractor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

## How to Use

1. Enter a website URL.
2. Choose what you want to extract.
3. Enter a CSS selector if you choose the custom option.
4. Click **Scrape website**.
5. View the results and download them as a CSV file.

## Limitations

- Some websites block automated requests or require JavaScript to display their content.
- Only scrape websites that permit automated access, and respect their terms of use.

## Purpose

This mini project was built as a hands-on learning exercise to practise Python, web scraping, data extraction, and Streamlit UI development.
