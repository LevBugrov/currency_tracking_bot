import telebot
import parser
import database

bot = telebot.TeleBot('5288800325:AAFaOwTi44D_uKsZ8WBwr4eF4O_OsU0tkZ0')
currency = parser.Currency()
database_answers = database.Database()

bots_answers = {
    "/start": "Этот бот предназначен для отслеживания курса валют",
    "/help": "USD - курс доллара на данный момент\n"
             "EUR - курс евро на данный момент\n"
             "CNY - курс юаня на данный момент\n"
             "all - вывести названия остальных доступных валют\n"
             "ДОБАВИТЬ название - добавляет новую валюту\n"
             "ИЗМЕНИТЬ название старой валюты название новой валюты пароль - изменяет дополнительную валюту\n"
             "УДАЛИТЬ название пароль - удаляет одну из дополнительных валют",
    "привет": "Привет, чем я могу тебе помочь?",
    "usd": f"1 доллар равен {currency.get_currency_price('usd')} рублям",
    "eur": f"1 евро равен {currency.get_currency_price('eur')} рублям",
    "cny": f"1 юань равен {currency.get_currency_price('cny')} рублям",
}


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    command = message.text.lower()
    answer = bots_answers.get(command)
    if answer:
        bot.send_message(message.from_user.id, answer)
    elif database_answers.data.get(command):
        bot.send_message(message.from_user.id, database_answers.get_data(command, currency.get_currency_price()))
    elif command == 'all':
        bot.send_message(message.from_user.id, database_answers.all_currency())
    elif len(command) > 9 and command[:9] == 'добавить ':
        bot.send_message(message.from_user.id, database_answers.add_currency(command[9:], currency))
    elif len(command) > 8 and command[:8] == 'удалить ':
        bot.send_message(message.from_user.id, database_answers.delete_currency(command[8:-5], command[-4:]))
    elif len(command) > 9 and command[:9] == 'изменить ':
        func_input = command[8:].split()
        if len(func_input) != 3:
            bot.send_message(message.from_user.id, "неправильный ввод")
        else:
            bot.send_message(message.from_user.id, database_answers.change_cur(*func_input))
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю :( \nПопробуй использовать /help")


bot.polling(none_stop=True, interval=0)
