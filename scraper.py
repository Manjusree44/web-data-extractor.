
import streamlit as s
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin, urlparse

s.title("Web Data Extractor")
s.write(
    "Extract headings, paragraphs, and links "
    "from websites and export the results."
)
choice = s.sidebar.selectbox(
    "What do you want to scrape?",
    ["Headings", "Paragraphs", "Links",
     "Custom CSS selector"]
)
web = s.text_input(
    "Enter the URL",
    "https://books.toscrape.com/"
)


selector = ""
if choice == "Custom CSS selector":
    selector = s.text_input("Enter a CSS selector", "h2")
def is_valid_url(url):
    parsed = urlparse(url.strip())

    return (
        parsed.scheme in ("http", "https")
        and bool(parsed.netloc)
        and "." in parsed.netloc
    )
if s.button("Scrape website"):
    if not is_valid_url(web):
       s.error("Please enter a valid URL starting with http:// or https://")
       s.stop()
    try:
        response = requests.get(
    web,
    timeout=15,
    headers={
        "User-Agent": "Mozilla/5.0 (compatible; MyLearningScraper/1.0)"
    }
)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        s.subheader(soup.title.get_text(strip = True) if soup.title else "No page title found")
        col1,col2 = s.columns(2)
        with col1:
            s.metric("Http status", response.status_code)
        with col2:
            s.metric("HTML SIZE", f"{len(response.text):,} characters")

        if choice == "Headings":
            results = soup.find_all(["h1", "h2", "h3"])

        elif choice == "Paragraphs":
            results = soup.find_all("p")

        elif choice == "Links":
            results = soup.find_all("a")

        else:
            results = soup.select(selector)

        data = []

        for item in results:
            text = item.get_text(" ", strip=True)

            if choice == "Links":
                link_url = urljoin(web, item.get("href", ""))

                data.append({
                    "Text": text,
                    "URL": link_url
                })
            else:
                data.append({
                    "Content": text
                })

        if data:
            df = pd.DataFrame(data)

            s.success(f"Found {len(df)} elements!")
            s.dataframe(df, use_container_width=True)

            s.download_button(
                label="Download CSV",
                data=df.to_csv(index=False).encode("utf-8"),
                file_name="scraped_data.csv",
                mime="text/csv"
            )
        else:
            s.warning("No matching elements found.")

    except requests.exceptions.HTTPError as e:
        if response.status_code == 403:
            s.error(
    "403 Forbidden: This website refused the request. "
    "Try a website that permits automated access."
)
        elif response.status_code == 404:
            s.error("Page not found (404), check the url or maybe try")
        else:
              s.error(f"Website returned an HTTP error: {e}")
    except requests.exceptions.RequestException as e:
      s.error(f"Could not connect to the website: {e}")
         
    except Exception as e:
        s.error(f"Something went wrong: {e}")

