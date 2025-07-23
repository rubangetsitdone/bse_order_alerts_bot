
import requests
import datetime
from bs4 import BeautifulSoup
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler

# Telegram bot setup
TELEGRAM_BOT_TOKEN = 'your_telegram_bot_token'
TELEGRAM_CHAT_ID = 'your_chat_id'
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

# Scheduler
scheduler = BlockingScheduler()

def fetch_bse_announcements():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    date_str = yesterday.strftime('%d-%m-%Y')

    url = 'https://www.bseindia.com/corporates/ann.html'
    session = requests.Session()
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Example placeholder – you need to implement actual form submission and data extraction logic here.
    announcements = ['Example Company - Order worth Rs. 100 Cr.']

    return announcements

def send_telegram_update():
    announcements = fetch_bse_announcements()
    if not announcements:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text='No new order announcements today.')
    else:
        message = "🏗️ *BSE Order Announcements (Yesterday)*\n\n" + "\n".join(f"- {a}" for a in announcements)
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message, parse_mode=telegram.ParseMode.MARKDOWN)

# Schedule daily at 9:00 AM IST (3:30 UTC)
scheduler.add_job(send_telegram_update, 'cron', hour=3, minute=30)
scheduler.start()
