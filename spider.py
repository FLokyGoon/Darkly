import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

# The base URL to start spidering from
base_url = "http://localhost:8080"

# Set to keep track of visited URLs
visited_urls = set()

def spider(url):
    # If the URL is already visited, skip it
    if url in visited_urls:
        return
    
    # Mark the URL as visited
    visited_urls.add(url)
    
    # Send the GET request
    try:
        response = requests.get(url)
    except requests.RequestException as e:
        print(f"Failed to access {url}: {e}")
        return
    
    # Print the URL being visited
    print(f"Visiting: {url}")
    
    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all links on the page
    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            # Construct the full URL
            full_url = urljoin(base_url, href)
            # Ensure we only visit URLs within the same domain
            if urlparse(full_url).netloc == urlparse(base_url).netloc:
                spider(full_url)  # Recursively spider the next link

# Start spidering from the base URL
spider(base_url)

# Print all the URLs that were visited
print("\nAll visited URLs:")
for url in visited_urls:
    print(url)
