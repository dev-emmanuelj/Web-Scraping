# Web-Scraping
Web Scraping with Python: A Step-by-Step Guide



Web scraping is like being a digital Sherlock Holmes, extracting hidden clues (or data) from websites. This guide will show you how to build a simple web scraper in Python using the `requests` library to fetch web pages and `BeautifulSoup` to parse HTML content. Grab your virtual magnifying glass and let's get started!

## Prerequisites

Before you can start sleuthing, ensure Python is installed on your machine. You will also need to install the `requests` and `BeautifulSoup4` libraries. Think of these as your detective tools. Install them using pip:

```bash
pip install requests
pip install beautifulsoup4
```

## Step 1: Import Libraries

Begin by importing the necessary libraries. No detective can start without their toolkit:

```python
import requests
from bs4 import BeautifulSoup
```

## Step 2: Fetch the Web Page

Use the `requests` library to fetch the content of the web page you want to scrape. Let's scrape a hypothetical webpage, `http://example.com`. (Imagine it's the internet's version of 221B Baker Street.)

```python
url = 'http://example.com'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    page_content = response.content
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
```

## Step 3: Parse HTML Content

Time to bring out `BeautifulSoup`, your HTML parsing sidekick. Together, you'll make sense of the garbled mess that is HTML.

```python
soup = BeautifulSoup(page_content, 'html.parser')
```

## Step 4: Extract Data

Assume we want to extract the title of the page and all the hyperlinks. It's like finding the headlines and the getaway routes. Elementary, my dear Watson!

### Extracting the Title

```python
page_title = soup.title.string
print(f"Page Title: {page_title}")
```

### Extracting Hyperlinks

To extract all hyperlinks (`<a>` tags) and their corresponding URLs:

```python
links = soup.find_all('a')
for link in links:
    href = link.get('href')
    link_text = link.string
    print(f"Link Text: {link_text}, URL: {href}")
```

## Full Example

([Combining all the steps, here is the complete script. It’s like the big reveal at the end of a mystery novel])

## Conclusion

And there you have it, a web scraper worthy of its own detective novel! By using the `requests` library to fetch web pages and `BeautifulSoup` to parse and extract information, you can automate data collection from the web. Always remember to respect the `robots.txt` file of websites and their terms of service to ensure ethical scraping practices. After all, even digital detectives have a code of honor. Happy sleuthing!
