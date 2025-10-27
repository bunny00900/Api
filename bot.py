import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set your OpenAI API key
openai.api_key = "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"

# Function to get the AI response from OpenAI
def get_ai_response(user_input: str) -> str:
    try:
        response = openai.Completion.create(
            model="gpt-4",  # Or you can use "gpt-3.5-turbo"
            prompt=user_input,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

# Start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am an AI bot. Type anything, and I will respond.')

# Function to handle incoming messages
def chat(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text  # Get the message sent by the user
    ai_response = get_ai_response(user_input)  # Get the AI-generated response
    update.message.reply_text(ai_response)  # Send the AI response back to the user

def main():
    # Use your Bot's API Token here
    bot_token = "8205921307:AAFqvo67zwXvVRePy7pFHcg7NIcTIrJz8RI"

    updater = Updater(bot_token, use_context=True)
    dispatcher = updater.dispatcher

    # Handlers for different commands and messages
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, chat))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
