import telebot

bot = telebot.TeleBot('your api key here')
from hacker_news import send_email
from email_conf import FROM, PASS,PORT,SERVER


# Create a dictionary to store user email addresses
user_emails = {}

# Initialize the variable to store the final email address
final_email = None

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Hi! Please send your email address as a text message.')

@bot.message_handler(func=lambda message: message.text and '@' in message.text)
def handle_email(message):
    chat_id = message.chat.id
    email_text = message.text.strip()
    # Store the user's email address in the dictionary
    user_emails[chat_id] = email_text
    # Inform the user that the email address has been recorded
    bot.send_message(chat_id, f'Thank you! Your email address has been recorded: {email_text}')
    # call send_email from hacker_news.py
    send_email(TO=email_text, FROM=FROM, SERVER=SERVER, PASS=PASS, PORT=PORT)
    if send_email:
         bot.send_message(chat_id, f'Thank you! email has been sent to: {email_text}')

bot.polling()