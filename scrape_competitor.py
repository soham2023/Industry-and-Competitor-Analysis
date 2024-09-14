from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import sqlite3
import time

def scrape_competitors_selenium(url):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        driver.get(url)

        # Increase wait time
        wait = WebDriverWait(driver, 30)
        
        # Debugging: Print the page source to verify content
        print(driver.page_source)  # This can be useful to see if content is loaded

        # Use WebDriverWait to wait for elements to be clickable or visible
        elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.competitor-class'))) # Adjust selector as needed
        
        # Process the data
        competitor_names = [element.text for element in elements]
        
        return competitor_names

    finally:
        driver.quit()

def save_to_db(data, db_filename):
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS competitors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    
    # Insert data into the table
    for name in data:
        cursor.execute('''
            INSERT INTO competitors (name) VALUES (?)
        ''', (name,))
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print(f"Data saved to {db_filename}")

if __name__ == "__main__":
    url = 'https://www.kaggle.com/datasets'  # Replace with the actual URL
    competitors = scrape_competitors_selenium(url)
    
    if competitors:
        save_to_db(competitors, 'competitors.db')
    else:
        print("No competitors found.")
