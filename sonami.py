from telethon import TelegramClient, events
from telethon import types
import datetime

now = "☑️ Today"
service = "Custom"

#sign in information 
API_ID = 0000000
API_HASH = ''
session_name = 'anon'
my_channel = 'sonami_ir'

def time():
    global now
    hour = datetime.datetime.now()
    hour = hour.strftime("%H")
    hour = int(hour)

    if hour >= 7 and hour <= 12:
        now = "🌤 Morning"

    if hour >= 13 and hour <= 17:
        now = "☀️ Mid-day"

    if hour >= 18 and hour <= 21:
        now = "⛅ Evening"

    if hour >= 21 and hour <= 23:
        now = "🌒 Night"

    if hour <= 6:
        now = "🌑 Mid-Night"

def type(msg):
    global service
    if "@FindProxy" in msg:
        if "همراه اول" in msg:
            service = "MCI"

        elif "ایرانسل" in msg:
            service = "Wifi | Irancell"

    if "@TelMTProto" in msg:
        service = "Custom"

    if "secret_proxy" in msg:
        service = "Custom"

client = TelegramClient(session_name,API_ID,API_HASH)

@client.on(events.NewMessage)
async def handle_message(event):
    msg = event.message.text
    if event.message.reply_markup and event.message.reply_markup.rows:
        url_button = event.message.reply_markup.rows[0].buttons[0]
        if isinstance(url_button, types.KeyboardButtonUrl):
            url = url_button.url
            if "@FindProxy" in msg or "@TelMTProto" in msg or "@secret_proxy" in msg:
                time()
                type(msg)
                text = ('''%s Proxy %s

Link : %s

🔝🔹@sonami_ir'''%(now,service,url))

                await client.send_message(my_channel, text)

client.start()
client.run_until_disconnected()