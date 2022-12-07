from django.core.management.base import BaseCommand
from django.conf import settings
import telebot

from telegram_orders.models import User, Menu


bot = telebot.TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)

class Command(BaseCommand):
    help = 'Run telegram bot'

    def handle(self, *args, **kwargs):

        def menu_render(state, message):
            menu = Menu.objects.get(state=state)

            markup = telebot.types.InlineKeyboardMarkup()
            for name, callback_data in menu.buttons.items():
                button = telebot.types.InlineKeyboardButton(name, callback_data=callback_data)
                markup.add(button)

            bot.send_message(message.chat.id, reply_markup=markup,
                             text='Привет!')


        @bot.message_handler(commands=['start'])
        def get_user(message):
            if User.objects.filter(user_id=message.from_user.id).exists():
                User.objects.update(user_id=message.from_user.id, state='start')
            else:
                User.objects.create(user_id=message.from_user.id, state='start')

            menu_render('start', message)

        bot.infinity_polling()
