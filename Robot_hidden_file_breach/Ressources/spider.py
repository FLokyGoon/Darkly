import subprocess
import re

def fetch_directory_links(base_url):
    """
    Fetches all links from a given URL directory listing using curl.
    """
    try:
        # Use curl to get the directory listing
        result = subprocess.run(['curl', '-s', base_url], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error fetching directory: {result.stderr}")
            return []

        # Extract all href links using regex
        links = re.findall(r'href="([^"]+)"', result.stdout)
        return links

    except Exception as e:
        print(f"Error fetching directory links: {e}")
        return []

def check_readme_for_flag(url):
    """
    Fetches a URL and checks if it contains the word 'flag'.
    """
    try:
        # Use curl to fetch the content of the readme file
        result = subprocess.run(['curl', '-s', url], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error fetching file: {result.stderr}")
            return False

        # Check if 'flag' is in the content
        if 'flag' in result.stdout.lower():
            print(f"Flag found in: {url}")
            print(f"Content: {result.stdout}")
            return True

    except Exception as e:
        print(f"Error checking file for flag: {e}")
    
    return False

def main():
    base_url = "http://localhost:8080/.hidden/"
    links_to_check = [base_url]

    # Track visited links to avoid checking the same link multiple times
    visited_links = set()

    while links_to_check:
        current_url = links_to_check.pop(0)
        visited_links.add(current_url)

        # Fetch all links in the current directory
        links = fetch_directory_links(current_url)

        for link in links:
            # Ignore parent directory link
            if link in ("../", "./"):
                continue

            # Construct the full URL
            full_url = current_url + link
            
            if full_url in visited_links:
                continue
            if link.endswith('/'):
                links_to_check.append(full_url)  # Add directory to check its content
            elif link.lower() == 'readme':  # Check only readme files
                if check_readme_for_flag(full_url):
                    return  # Exit if the flag is found

if __name__ == "__main__":
    main()
