import requests
from bs4 import BeautifulSoup
import os
import json
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Load environment variables
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# File names for storing sent program records
YOUTHALL_DATA_FILE = "sent_programs_youthall.json"
VIZYONER_DATA_FILE = "sent_programs_vizyoner.json"

def get_youthall_programs():
    """Scrape talent programs from Youthall"""
    url = "https://www.youthall.com/tr/talent-programs/?page=1&order=6"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        programs = soup.find_all("div", class_="y-talent box_hover border-line-light-blue shadow-light")
        program_list = []

        for program in programs:
            title_element = program.find("div", class_="y-talent_title")
            title = title_element.find("label").get_text(strip=True)
            link_element = program.find("a", href=True)
            link = "https://www.youthall.com" + link_element["href"]
            program_list.append({"title": title, "link": link})

        return program_list
    return []

import requests

def get_vizyonergenç_programs():
    USER_EMAIL = os.getenv("VIZYONER_EMAIL")
    USER_PASSWORD = os.getenv("VIZYONER_PASSWORD")

    options = Options()
    options.headless = False  # testte açık bırak
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 15)

    # Step 1: Go to home page
    driver.get("https://vizyonergenc.com")
    time.sleep(2)

    # Step 2: Click on "Giriş Yap" button (top right)
    try:
        # Giriş yap / Kayıt ol butonunu tıklıyoruz
        login_trigger = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "login-trigger")))
        login_trigger.click()
        print("✅ Clicked 'Giriş Yap / Kayıt Ol' button")
        time.sleep(2)  # Modalın açılmasını bekle
    except Exception as e:
        print("❌ Couldn't click login modal trigger:", e)
        driver.quit()
        return []


    # Step 3: Fill login modal
    try:
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))

        email_input.send_keys(USER_EMAIL)
        password_input.send_keys(USER_PASSWORD)

        # Use the actual login button by ID
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "loginButton")))
        login_button.click()
        print("✅ Clicked 'Giriş Yap' button")
        time.sleep(3)
    except Exception as e:
        print("Login failed:", e)
        driver.quit()
        return []

    # Step 4: Go to listings page
    driver.get("https://vizyonergenc.com/ilanlar")
    time.sleep(3)

    # Step 5: Filter for internship listings
    try:
        staj_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Staj İlanları')]")))
        staj_button.click()
        time.sleep(3)
    except Exception as e:
        print("Could not click Staj İlanları:", e)

    # Step 6: Scrape listings
    program_list = []
    cards = driver.find_elements(By.CLASS_NAME, "job-listing")

    for card in cards:
        try:
            title = card.find_element(By.CLASS_NAME, "job-listing-title").text
            href = card.get_attribute("href")
            if "(Staj)" in title and href:
                program_list.append({"title": title, "link": href})
        except:
            continue

    driver.quit()
    return program_list


def send_telegram_notification(message):
    """Send a message via Telegram bot"""
    telegram_api_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    response = requests.post(telegram_api_url, json=payload)
    print(f"Message sent: {message}")
    print(f"Status Code: {response.status_code}")
    print(response.json())

def load_sent_programs(filename):
    """Load previously sent programs from JSON file"""
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def save_sent_programs(filename, programs):
    """Save updated program list to JSON file"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(programs, file, ensure_ascii=False, indent=2)

def check_and_notify(source_name, get_programs_func, data_file):
    """
    Generic function to fetch, compare and send new programs
    :param source_name: Identifier for the source (used in message)
    :param get_programs_func: Function to get current programs
    :param data_file: File to store previously sent programs
    """
    current_programs = get_programs_func()
    sent_programs = load_sent_programs(data_file)

    new_programs = [
        p for p in current_programs
        if p["title"] not in [s["title"] for s in sent_programs]
    ]

    if new_programs:
        for program in new_programs:
            message = f"📢 [{source_name}]\n{program['title']}\n{program['link']}"
            send_telegram_notification(message)
        updated_programs = sent_programs + new_programs
        save_sent_programs(data_file, updated_programs)
    else:
        print(f"No new programs found on {source_name}.")

def main():
    # Check Youthall
    check_and_notify("Youthall", get_youthall_programs, YOUTHALL_DATA_FILE)
    # Check Vizyoner Genç
    check_and_notify("VizyonerGenç", get_vizyonergenç_programs, VIZYONER_DATA_FILE)

if __name__ == "__main__":
    main()
for p in get_vizyonergenç_programs():
    print(p)
