import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your QuestionBot. How can I help you?")


def answer_question(update, context):
    question = update.message.text
    response = get_response(question)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)


def get_response(question):

    if question.lower() == 'how are you?':
        return "I'm good, thank you!"
    elif question.lower() == 'what is your name?':
        return "I am ChatBot, a Telegram bot developed by Sathwik."
    else:
        return "I'm sorry, I don't have an answer for that."


def main():
    updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)

    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    message_handler = MessageHandler(Filters.text & ~Filters.command, answer_question)
    dispatcher.add_handler(message_handler)

    updater.start_polling()
    logger.info("Bot started!")

    updater.idle()


if __name__ == '__main__':
    main()
