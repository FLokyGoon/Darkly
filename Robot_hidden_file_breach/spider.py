import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from collections import deque

def explore_directory(base_url):
    queue = deque([base_url])
    visited = set()

    # Create a file to save the output
    with open("readme_output.txt", "w") as output_file:
        while queue:
            url = queue.popleft()
            if url in visited:
                continue
            visited.add(url)
            
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Find all links on the page
            for link in soup.find_all("a"):
                href = link.get("href")
                if href and href != "../":
                    full_url = urljoin(url, href)
                    
                    # If it's a directory, add it to the queue
                    if href.endswith("/"):
                        queue.append(full_url)
                    # If it's the README file, check its content length
                    elif "README" in href:
                        readme_response = requests.get(full_url)
                        content = readme_response.text    
                        output_file.write("README content:\n")
                        output_file.write(content + "\n\n")  # Add newline separators
                        if "flag" in content:
                            output_file.write(f"Found README with flag: {full_url}\n")
                            return

# Start exploring from the base URL
base_url = "http://localhost:8080/.hidden/"
explore_directory(base_url)