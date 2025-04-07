# Internship Telegram Bot

This Python bot automatically checks for new internship and talent programs from:

- [Youthall](https://youthall.com/tr/talent-programs)
- [Vizyoner Genç](https://vizyonergenc.com/ilanlar)

When a new internship is detected, it sends a Telegram message to your account or group.  
This bot is ideal for students or young professionals who want to instantly hear about new opportunities.

---

## 🚀 How to Use

### 1. Clone this repository

```bash
git clone https://github.com/ofarukgunay/Internship-Bot.git
cd Internship-Bot
```

### 2. Install the required Python libraries

Make sure you have Python installed, then run:

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

In the root directory, create a file named `.env` and paste the following:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

You can use the `.env.example` file as a reference.

### 4. Run the bot manually

```bash
python bot.py
```

If there are any new internship listings, they will be sent to your Telegram chat.

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

## ⚙️ Automate the Bot (Optional)

To make the bot run automatically every 15 minutes, you can:

- Use a **cron job** (Linux/macOS)
- Use **Task Scheduler** (Windows)
- Deploy it to a cloud service like **Render.com**, **Railway.app**, or **Replit**

---

## 📁 Project Structure

```
Internship-Bot/
├── main.py              => Main bot script
├── requirements.txt     => Required Python packages
├── .env                 => Template for environment variables
├── .gitignore           => Files to ignore in Git
└── README.md            => You’re here!
```

---

## ✨ Features

- Sends real-time internship alerts to Telegram
- Checks two different platforms (Youthall & Vizyoner Genç)
- Avoids duplicate notifications
- Easy to extend with more sources

---

Made with ❤️ by [@ofarukgunay](https://github.com/ofarukgunay)
```
