from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random

# Path to your file containing URLs
url_file = '/sec/root/test3/links.txt'

# Setup Chrome options for Selenium (headless mode to avoid opening the browser window)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode to avoid opening the browser

# Path to the ChromeDriver (replace with your path if needed)
service = Service('/usr/bin/chromedriver')  # Ensure ChromeDriver is in your PATH or provide the full path

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Function to process and extract search results from a Google search URL
def process_url(url):
    try:
        # Open the URL in the browser
        driver.get(url)

        # Wait for the page to load completely (you can adjust the time if needed)
        time.sleep(3)

        # Extract search results: titles, URLs, and descriptions
        search_results = driver.find_elements(By.CSS_SELECTOR, 'div.g')

        # Prepare a list to store the results
        results = []

        for result in search_results:
            try:
                # Extract the title
                title_element = result.find_element(By.CSS_SELECTOR, 'h3')
                title = title_element.text

                # Extract the URL
                url_element = result.find_element(By.CSS_SELECTOR, 'a')
                link = url_element.get_attribute('href')

                # Extract the description (snippet)
                snippet_element = result.find_element(By.CSS_SELECTOR, 'span.st')
                snippet = snippet_element.text

                # Save the result in a dictionary
                results.append({
                    'title': title,
                    'url': link,
                    'snippet': snippet
                })

            except Exception as e:
                print(f"Failed to extract a result: {e}")
                continue
        
        # Save the extracted results to a file
        with open('search_results.txt', 'a') as f:
            f.write(f"Results for URL: {url}\n")
            for res in results:
                f.write(f"Title: {res['title']}\nURL: {res['url']}\nSnippet: {res['snippet']}\n\n")
            f.write("="*40 + "\n\n")

        print(f"Processed URL: {url}, Results saved.")

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
