# Internship Telegram Bot 🤖

This Python bot automatically checks for new internship and talent programs from:

- [Youthall](https://youthall.com/tr/talent-programs)
- [Vizyoner Genç](https://vizyonergenc.com/ilanlar)

When a new internship is detected, it sends a Telegram message to your account or group. This bot is ideal for students or young professionals who want to instantly hear about new opportunities.

---

## ✨ Features
- ✅ Telegram integration with custom bot token and chat ID
- ✅ Automatically logs in to Vizyoner Genç using a modal login system
- ✅ Detects and sends only newly published internships
- ✅ Avoids duplicate notifications by storing previously sent titles
- ✅ Selenium-based scraping to handle dynamic content (JavaScript-loaded listings)

---

## 🚀 How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/ofarukgunay/Internship-Bot.git
cd Internship-Bot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

> Make sure you have Google Chrome installed.

---

### 3. Set Up the Environment Variables
Create a `.env` file in the root directory and add your configuration:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
VIZYONER_EMAIL=youremail@example.com
VIZYONER_PASSWORD=yourpassword123
```

- `TELEGRAM_BOT_TOKEN`: Token provided by @BotFather
- `TELEGRAM_CHAT_ID`: ID of your Telegram or group chat
- `VIZYONER_EMAIL`: Your login email for vizyonergenc.com
- `VIZYONER_PASSWORD`: Your login password

**Note:** Do NOT wrap these values in quotes.

---

## 🔍 How It Works

### Youthall:
- Uses `requests` + `BeautifulSoup` to scrape internship titles and links
- Compares them with saved records in `sent_programs_youthall.json`

### Vizyoner Genç:
- Uses `selenium` to open the main page
- Clicks the "Giriş Yap / Kayıt Ol" button to open modal
- Logs in with credentials
- Navigates to internship listing page
- Filters only "Staj İlanları"
- Collects visible internships and their detail links
- Avoids duplicates by saving to `sent_programs_vizyoner.json`

---

## 🚨 Important Notes
- You must have **Google Chrome** and **ChromeDriver** installed.
- The bot uses `webdriver-manager` to automatically fetch the right ChromeDriver.
- Run the bot using:
```bash
python main.py
```


## 📄 Project Structure
```
Internship-Bot/                     
├── main.py                    # Main bot logic
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (excluded from git)
├── sent_programs_youthall.json
├── sent_programs_vizyoner.json
└── README.md
```


Made with ❤️ by [@ofarukgunay](https://github.com/ofarukgunay)

