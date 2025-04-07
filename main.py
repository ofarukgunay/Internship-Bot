import requests
from bs4 import BeautifulSoup
import os
import json
from dotenv import load_dotenv

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

def get_vizyonergenç_programs():
    """Scrape internship posts from Vizyoner Genç"""
    url = "https://vizyonergenc.com/ilanlar"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        ilanlar = soup.find_all("a", class_="card card-list card-hover")
        program_list = []

        for ilan in ilanlar:
            title = ilan.find("h5").get_text(strip=True)
            link = "https://vizyonergenc.com" + ilan["href"]
            program_list.append({"title": title, "link": link})

        return program_list
    return []

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
