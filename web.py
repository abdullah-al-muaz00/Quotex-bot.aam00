from flask import Flask
from bot import send_telegram_message, start_bot

app = Flask(__name__)

@app.route("/")
def home():
    return "🟢 AAM Quotex Bot is Running"

@app.route("/test")
def test():
    text = "**__𝑨𝑨𝑴 𝑻𝒓𝒂𝒅𝒆𝒓__**\nThis is a test signal from web ✅"
    success = send_telegram_message(text)
    if success:
        return "✅ Test message sent!"
    else:
        return "❌ Failed to send message"

if __name__ == "__main__":
    start_bot()
    app.run(host="0.0.0.0", port=8000)
