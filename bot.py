import constants
import telebot
import openai
from telebot import types
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

openai.api_key = constants.openai

bot = telebot.TeleBot(constants.token)


def handle_message(update, context):
    # Get the user's message
    message = update.message.text

    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"User: {message}\nBot:",
        max_tokens=1024,
        temperature=0.5,
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the generated response from the API response
    response_text = response["choices"][0]["text"]

    # Send the response to the user
    bot.send_message(chat_id=update.message.chat_id, text=response_text)


# Set up the bot to listen for user messages
updater = Updater(bot.token, use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

# Start the bot
updater.start_polling()
