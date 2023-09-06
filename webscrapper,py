import requests
from bs4 import BeautifulSoup

# Prompt the user for the URL
url = input("Enter the URL you want to scrape: ")

# Send an HTTP GET request to the user-provided URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Now, you can locate and extract specific data from the HTML
    # For example, if you want to extract all the links on the page:
    links = soup.find_all('a')
    
    # Print the links
    for link in links:
        print(link.get('href'))

    # You can also extract other data like text within specific elements, images, etc.
else:
    print('Failed to retrieve the web page. Status code:', response.status_code)
