from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_rmp(url):
    #headless (invisible) chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("window-size=800x600")
    prefs = {
    "profile.managed_default_content_settings.images": 2,
    "profile.managed_default_content_settings.stylesheets": 1,
    "profile.managed_default_content_settings.fonts": 2
    }
    options.add_experimental_option("prefs", prefs)

    # Launch browser using ChromeDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        print(f"🌐 Opening: {url}")
        driver.get(url)

        wait = WebDriverWait(driver, 5) # max wait, 5 seconds

        # Scrape the overall rating
        rating_elem = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "RatingValue__Numerator-qw8sqy-2")))
        rating = rating_elem.text
        print(rating)

        # Scrape "Would Take Again" and "Level of Difficulty"
        feedbacks = driver.find_elements(By.CLASS_NAME, 'FeedbackItem__FeedbackNumber-uof32n-1')
        would_take_again = feedbacks[0].text if len(feedbacks) > 0 else "N/A"
        difficulty = feedbacks[1].text if len(feedbacks) > 1 else "N/A"

        print(f"⭐ Overall Rating: {rating}")
        print(f"🔁 Would Take Again: {would_take_again}")
        print(f"📊 Difficulty: {difficulty}")

        return {
            "rating": rating,
            "would_take_again": would_take_again,
            "difficulty": difficulty
        }

    except Exception as e:
        print(f"❌ Error: {e}")
        return None

    finally:
        driver.quit()

start_time = time.perf_counter()
rmp_url = "https://www.ratemyprofessors.com/professor/2337555"
scrape_rmp(rmp_url)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(elapsed_time)