from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random

# Path to your file containing URLs
url_file = '/mnt/data/links.txt'

# Setup Chrome options for Selenium (headless mode to avoid opening the browser window)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode to avoid opening the browser

# Path to the ChromeDriver (replace with your path if needed)
service = Service('/path/to/chromedriver')  # Ensure ChromeDriver is in your PATH or provide the full path

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Function to process a single URL using Selenium
def process_url(url):
    try:
        # Open the URL in the browser
        driver.get(url)

        # Extract the page title (modify this based on what you want to scrape)
        page_title = driver.title
        print(f"Processed URL: {url}, Title: {page_title}")
        
        # Save the result
        with open('results.txt', 'a') as f:
            f.write(f"URL: {url}\nTitle: {page_title}\n\n")

    except Exception as e:
        print(f"Failed to process {url}: {e}")

# Read the URLs from the file and process them one by one
with open(url_file, 'r') as file:
    for line in file:
        url = line.strip()  # Remove any extra spaces or newline characters
        if url:  # Ensure the line isn't empty
            process_url(url)

            # Introduce a random delay between 5 to 15 seconds to avoid rate-limiting
            delay = random.uniform(5, 15)
            print(f"Waiting for {delay:.2f} seconds before the next request...")
            time.sleep(delay)

# Quit the browser after processing all URLs
driver.quit()
