import requests
from bs4 import BeautifulSoup

# URL of the web page to scrape
url = 'https://www.geeksforgeeks.org/how-to-install-android-virtual-deviceavd/'  # Replace with the URL you want to scrape

# Send a GET request to the web page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the web page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract text from the web page
    page_text = soup.get_text()
    print("Page Text:")
    print(page_text)
    
    # Extract all links from the web page
    links = soup.find_all('a')
    print("\nLinks:")
    for link in links:
        print(link.get('href'))
    
    # Extract all image URLs from the web page
    images = soup.find_all('img')
    print("\nImages:")
    for img in images:
        print(img.get('src'))
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
