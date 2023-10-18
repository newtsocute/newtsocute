import telegram

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота, полученного от BotFather
TOKEN = 'YOUR_BOT_TOKEN'


# Функция для обработки команды /start
def start(update, context):
    user = update.effective_user
    context.user_data['user_id'] = user.id
    update.message.reply_html(
        fr'Привет, {user.mention_html()}!',
        reply_markup=main_menu_keyboard()
    )


# Клавиатура с основным меню
def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("Кнопка 1", callback_data='btn1')],
        [InlineKeyboardButton("Кнопка 2", callback_data='btn2')],
    ]
    return InlineKeyboardMarkup(keyboard)


# Обработчик нажатия на кнопки меню
def main_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Выберите действие:",
        reply_markup=main_menu_keyboard()
    )


# Обработчик кнопки 1
def button1(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Вы нажали на кнопку 1",
        reply_markup=main_menu_keyboard()
    )


# Обработчик кнопки 2
def button2(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Вы нажали на кнопку 2",
        reply_markup=main_menu_keyboard()
    )


# Функция для остановки бота
def stop(update, context):
    user_id = context.user_data.get('user_id')
    if user_id:
        context.user_data.clear()
    update.message.reply_text("Бот остановлен.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    # Создаем обработчик для кнопок меню
    dp.add_handler(CallbackQueryHandler(main_menu, pattern='^main$'))

    # Обработчики для кнопок 1 и 2
    dp.add_handler(CallbackQueryHandler(button1, pattern='^btn1$'))
    dp.add_handler(CallbackQueryHandler(button2, pattern='^btn2$'))

    # Обработчик команды /stop
    dp.add_handler(CommandHandler('stop', stop))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()