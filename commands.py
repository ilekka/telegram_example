from utils import check


def ping(update, context):

    if not check(update, context):
        return

    context.bot.send_message(chat_id=update.effective_chat.id, text='Ping!')


def send_nudes(update, context):

    if not check(update, context):
        return

    with open('/home/ilkka/Python/telegram_example/photo.jpg', 'rb') as pic:
        context.bot.send_document(
                chat_id=update.effective_chat.id, document=pic)


def chatid(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text=str(chat_id))


def unknown(update, context):

    if not check(update, context):
        return

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Sorry, I didn't understand that command.")
