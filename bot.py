import os
import requests
import threading
import time
from datetime import datetime
from dotenv import load_dotenv
import schedule

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

MARKET_PAIRS = [
    "EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CAD",
    "NZD/USD", "USD/CHF", "EUR/GBP", "EUR/JPY", "GBP/JPY"
]

def signal_message(pair, duration, accuracy):
    now = datetime.now().strftime("%Y-%m-%d %I:%M %p")
    msg = (
        "**__𝑨𝑨𝑴 𝑻𝒓𝒂𝒅𝒆𝒓__**\n"
        f"📈 Market: {pair}\n"
        f"⏱️ Duration: {duration}\n"
        f"🕒 Time: {now}\n"
        f"🎯 Accuracy: {accuracy}%\n"
        "**__𝑩𝒀 𝑴𝒖𝒂𝒛__**"
    )
    return msg

def result_message(pair, status):
    now = datetime.now().strftime("%Y-%m-%d %I:%M %p")
    emoji = "✅ WIN" if status == "WIN" else "❌ LOSS"
    msg = (
        "**__𝑨𝑨𝑴 𝑻𝒓𝒂𝒅𝒆𝒓__**\n"
        f"🏁 Result: {emoji}\n"
        f"📈 Market: {pair}\n"
        f"🕒 Time: {now}"
    )
    return msg

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    res = requests.post(url, data=payload)
    return res.status_code == 200

def send_signals():
    duration = "1 Minute"
    accuracy = 97  # এখানে প্রয়োজনমতো পরিবর্তন করতে পারো

    for pair in MARKET_PAIRS:
        sig_msg = signal_message(pair, duration, accuracy)
        send_telegram_message(sig_msg)
        time.sleep(3)  # ছোট বিরতি
        # 1 মিনিট পরে রেজাল্ট মেসেজ পাঠানো (এখানে সরলায়িত WIN মেসেজ)
        res_msg = result_message(pair, "WIN")
        send_telegram_message(res_msg)
        time.sleep(177)  # মোট 3 মিনিটের হিসাব

def run_schedule():
    schedule.every().day.at("10:00").do(send_signals)
    # প্রতিদিন রাত 3 টা পর্যন্ত চালাতে হবে, তাই শেষ সময় সেট করো
    # এখানে দৈনিক শুরু করার সময় নির্দিষ্ট, তুমি চাইলে স্লাইডার মতো সময় দিন।

    while True:
        schedule.run_pending()
        time.sleep(1)

def start_bot():
    thread = threading.Thread(target=run_schedule)
    thread.daemon = True
    thread.start()
