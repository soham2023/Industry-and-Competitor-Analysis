import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_competitors(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    competitors = []
    
    # Inspect the HTML structure and change this according to what you find
    for listing in soup.find_all('div', class_='product_pod'):  # Adjust this selector based on the HTML structure
        name = listing.h3.a['title']  # This is an example from 'Books to Scrape'
        price = listing.find('p', class_='price_color').text.strip()  # Another example field, modify as needed
        competitors.append({'Name': name, 'Price': price})  # Adjust to capture relevant data

    return competitors

def save_to_csv(data, filename):
    if data:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    else:
        print("No data to save.")

if __name__ == "__main__":
    url = 'http://books.toscrape.com/'  # Adjust URL to the target site
    competitors = scrape_competitors(url)
    save_to_csv(competitors, 'competitors.csv')