import random
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

output_dir = "/home/dev/Documents/Projects/seleniumbase-python/logs"
os.makedirs(output_dir, exist_ok=True)

params_json = '''
{
    "visitorID": 0,
    "geolocation": {
        "display": "United States",
        "language": {
            "lang": "en-US",
            "accept-language": "en-US,en;q=0.5"
        },
        "timezone": "America/Phoenix",
        "mobile": {
            "android": 45,
            "ios": 55
        },
        "countryCode": "us",
        "option": "standard"
    },
    "proxy": {
        "type": "http",
        "name": "myproxy",
        "ip": "147.185.238.169",
        "port": "50148",
        "qty": 5
    },
    "browser": {
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }
}
'''
params = json.loads(params_json)

chrome_options = Options()
chrome_options.add_argument(f"user-agent={params['browser']['userAgent']}")

service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

steps = [
    {"to": "http://seleniumbase.io/demo_page", "type": "href"},
    {"wait_start": 10, "wait_end": 20},
    [{"fillform_name": "#myTextInput", "fillform_content": "This is some content"}],
    {"to": "https://seleniumbase.com", "type": "href", "referrer": ""}
]

result_comparison = []

# Step 1: Navigate to the first page
driver.get(steps[0]['to'])
current_url = driver.current_url
result_comparison.append(f"step::cheateo::1")
result_comparison.append(f"log::cheateo::{current_url}::cheateo::Web Testing Page")

# Capture screenshot and save HTML
timestamp = random.randint(1000, 9999)
screenshot_path = os.path.join(output_dir, f"{timestamp}_1.png")
html_path = os.path.join(output_dir, f"{timestamp}_1.txt")
driver.save_screenshot(screenshot_path)
with open(html_path, 'w', encoding='utf-8') as file:
    file.write(driver.page_source)

result_comparison.append(f"capture::cheateo::{screenshot_path}")
result_comparison.append(f"storeHTML::cheateo::{html_path}")

# Step 2: Wait for a random time between wait_start and wait_end
wait_time = random.randint(steps[1]['wait_start'], steps[1]['wait_end'])
time.sleep(wait_time)
result_comparison.append(f"wait::cheateo::{wait_time}")

# Step 3: Fill out the form
input_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, steps[2][0]['fillform_name']))
)
input_element.send_keys(steps[2][0]['fillform_content'])

result_comparison.append(f"step::cheateo::3")
result_comparison.append(f"sendKeys::cheateo::{steps[2][0]['fillform_name']}::cheateo::{steps[2][0]['fillform_content']}::cheateo::true")

# Capture screenshot and save HTML
timestamp = random.randint(1000, 9999)
screenshot_path = os.path.join(output_dir, f"{timestamp}_3.png")
html_path = os.path.join(output_dir, f"{timestamp}_3.txt")
driver.save_screenshot(screenshot_path)
with open(html_path, 'w', encoding='utf-8') as file:
    file.write(driver.page_source)

result_comparison.append(f"capture::cheateo::{screenshot_path}")
result_comparison.append(f"storeHTML::cheateo::{html_path}")

# Step 4: Navigate to the next page
driver.get(steps[3]['to'])
current_url = driver.current_url
result_comparison.append(f"step::cheateo::4")
result_comparison.append(f"click::cheateo::href::cheateo::a[href*='https://seleniumbase.com']::cheateo::true::cheateo::{steps[3]['to']}")

# Capture screenshot and save HTML
timestamp = random.randint(1000, 9999)
screenshot_path = os.path.join(output_dir, f"{timestamp}_4.png")
html_path = os.path.join(output_dir, f"{timestamp}_4.txt")
driver.save_screenshot(screenshot_path)
with open(html_path, 'w', encoding='utf-8') as file:
    file.write(driver.page_source)

result_comparison.append(f"capture::cheateo::{screenshot_path}")
result_comparison.append(f"storeHTML::cheateo::{html_path}")

# Step 5: Exit
result_comparison.append("exit::cheateo::success")

# Print final result comparison
print(result_comparison)

# Close the browser
driver.quit()