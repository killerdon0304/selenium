import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def setup_driver():
    options = Options()
    options.add_argument("--headless")  # Headless optional
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)

def cookies():
    driver = setup_driver()
    driver.get("https://netfree2.cc/mobile/home")

    data_hash = driver.find_element(By.TAG_NAME, "body").get_attribute("data-hash")
    if not data_hash:
        try:
            button = driver.find_element(By.CSS_SELECTOR, "button.open-support.checker")
            button.click()
            print("✅ Button clicked.")
            
        except Exception as e:
            print("❌ Button click failed:", e)
            driver.quit()
            return

    t=0
    for _ in range(50):
        print(t)
        t+=1
        data_hash1 = driver.find_element(By.TAG_NAME, "body").get_attribute("data-hash")
        if data_hash1:
            print("hasth mil gaya")
            cookies = driver.get_cookies()
            # सभी cookies को print करें
            for cookie in cookies:
                if cookie['name'] == 't_hash_t':
                    print(cookie)
                    result={cookie['name']:cookie['value']}

                    with open("cookies.json", "w") as f:
                        json.dump(result, f, indent=4)
            return result
        time.sleep(1)

    driver.quit()


if __name__ == "__main__":
    print(cookies())
