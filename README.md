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

## 🤖 How to Create a Telegram Bot and Get the Token
 
 1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
 2. Start a chat and send `/newbot`
 3. Choose a name and a username (must end with `bot`, e.g., `myinternshipbot`)
 4. BotFather will give you a token like:
 
 ```
 123456789:ABCdefGHIjklMNOpqrSTUvwxYZ
 ```
 
 Copy and paste this token into your `.env` file as `TELEGRAM_BOT_TOKEN`.
 
 ---
 
 ## 💬 How to Find Your Chat ID
 
 ### For personal use
 
 1. Search for [@userinfobot](https://t.me/userinfobot) on Telegram
 2. Start the chat and it will show your user ID, like:
 
 ```
 Your chat ID: 123456789
 ```
 
 Use this number as `TELEGRAM_CHAT_ID`.
 
 ### For groups
 
 1. Add your bot to the group
 2. Send a message in the group
 3. Go to this URL in your browser (replace with your actual token):
 
 ```
 https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
 ```
 
 4. Look in the JSON for `"chat": {"id": ...}` — that's your group chat ID.  
 It usually starts with `-100`.
 
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

