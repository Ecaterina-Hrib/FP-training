from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def selenium_scraping():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    query = "Python programming"
    url = f"https://twitter.com/search?q={query.replace(' ', '%20')}&src=typed_query"
    driver.get(url)

    time.sleep(120)

    tweets = driver.find_elements(By.CSS_SELECTOR, 'article div[lang]')

    for tweet in tweets:
        print(tweet.text)

    driver.quit()


selenium_scraping()