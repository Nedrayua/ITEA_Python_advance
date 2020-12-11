# 1) Написать бота-консультанта, который будет собирать информацию с
# пользователя (его ФИО, номер телефона, почта, адресс, пожелания).
# Записывать сформированную заявку в БД (по желанию SQl/NOSQL).).

from config import TOKEN
from telebot import TeleBot
from models import GuestProfile


bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_handler(message):
    GuestProfile(from_user_id=message.from_user.id).save()
    message_for_user = f'Добрый день!\nДля дальнейшей работы прошу зарегистрироваться в нашей системе и поочередно заполнить' \
              f'Ваши данные с обязательной команой в конце для подтверждения. Например: Иванов Иван FIO' \
              f'ФИО... FIO\n' \
              f'Номер телефона... (в формате 380.........) TEL\n' \
              f'Почта... POS\n' \
              f'Адресс... ADS\n' \
              f'Пожелания... WSH'

    bot.send_message(
        message.chat.id,
        message_for_user
    )


@bot.message_handler(func=lambda m: m.text[-3:] in {'FIO', 'TEL', 'POS', 'ADS', 'WSH'})
def user_registration(message):
    guest = GuestProfile.objects().get(from_user_id=message.from_user.id)
    options_dict = {'FIO': {'fio': {message.text[:-4]}}, 'TEL': {'num_phone': message.text[:-4]},
                    'POS': {'post': message.text[:-4]}, 'ADS': {'address': message.text[:-4]},
                    'WSH': {'wishes': message.text[-4:]}}
    guest.update(**options_dict[message.text[-3:]])
    print(options_dict[message.text[-3:]])
    print(message.from_user.id)
@bot.message_handler(content_types='text')
def bug_message(message):
    message_for_user = f"Вы прислали: {message.text}"
    bot.send_message(
        message.chat.id,
        message_for_user
    )


bot.polling()