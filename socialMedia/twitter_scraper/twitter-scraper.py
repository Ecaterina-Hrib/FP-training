from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def selenium_scraping():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    query = "Happy kitten"
    url = f"https://twitter.com/search?q={query.replace(' ', '%20')}&src=typed_query"
    driver.get(url)

    try:
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'article div[lang]'))
        )
    except:
        print("Tweets did not load.")
        driver.quit()
        return

    for _ in range(5):
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(3)

    tweets = driver.find_elements(By.CSS_SELECTOR, 'article div[lang]')

    for tweet in tweets:
        try:
            print(tweet.text)
            print("-" * 80)
        except Exception as e:
            print("Error reading tweet:", e)

    driver.quit()

selenium_scraping()
