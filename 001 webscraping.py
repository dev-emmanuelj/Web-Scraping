import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the web page
url = 'http://example.com'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    page_content = response.content
    # Step 2: Parse HTML content
    soup = BeautifulSoup(page_content, 'html.parser')
    
    # Step 3: Extract the title
    page_title = soup.title.string
    print(f"Page Title: {page_title}")
    
    # Step 4: Extract hyperlinks
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        link_text = link.string
        print(f"Link Text: {link_text}, URL: {href}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
