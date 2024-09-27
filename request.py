from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up Selenium WebDriver (requires ChromeDriver)
def setup_driver():
    options = Options()
    options.add_argument('--headless')  # Run in headless mode (without GUI)
    service = Service('/usr/bin/chromedriver')  # Replace with the path to your ChromeDriver
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# Read URLs from the file
def read_urls_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

# Visit URLs using Selenium to bypass Cloudflare
def visit_urls_with_selenium(urls):
    driver = setup_driver()
    num_urls_per_second = 10
    visit_interval = 1 / num_urls_per_second  # Time interval between visits

    for url in urls:
        try:
            driver.get(url)
            print(f"Visited: {url}, Title: {driver.title}")
            time.sleep(visit_interval)  # Wait for the defined interval
        except Exception as e:
            print(f"Error visiting {url}: {e}")
    driver.quit()

if __name__ == "__main__":
    urls_file = 'allurls3'  # Change this to your file containing URLs
    urls = read_urls_from_file(urls_file)
    visit_urls_with_selenium(urls)
