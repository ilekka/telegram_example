from datetime import datetime
import os
from dotenv import load_dotenv


def current_time():
    return datetime.now().strftime('%d/%m/%Y %H:%M:%S')


def check(update, context):

    known_ids = [int(os.getenv('CHAT_ID')), int(os.getenv('GROUP_ID'))]

    if update.effective_chat.id in known_ids:
        return True

    else:
        text = "Go away, I don't know who you are!"
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        return False
