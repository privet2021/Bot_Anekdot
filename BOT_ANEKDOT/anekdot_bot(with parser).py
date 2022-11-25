# поле для импорта стандартных библиотек
from random import choice

# импорт модулей для работы с aiogram
from aiogram import Bot, Dispatcher, executor, types
# Класс текст перехватывает с помощью хэндлеров определенный текст, работает точно также, как и с командами
from aiogram.dispatcher.filters import Text

# импорт данных для бота из файлов проекта
from BOT_ANEKDOT.Bot_API import TOKEN, START_MESSAGE, BOT_DESCRIPTION, HELP_COMMANDS, NEGATIVE_ANSWER, RANDOM_STIKERS
from BOT_ANEKDOT.Keyboards import keyboard_anekdots, start_menu_keyboard, keyboard_yes_or_no
from BOT_ANEKDOT.anekdots_category_A import anekdots_A
from BOT_ANEKDOT.anekdots_category_B import anekdots_B

# Основные переменные бота
bot_function = 'Случайные анекдоты(с парсером данных)'
# Вызываем экземпляр бота и передаем в него токен телеграм для дальнейшего взаимодействия
bot = Bot(token=TOKEN)
# Диспетчер отвечает за получение обновлений от Телеграма и перенаправляет бота на соответствующий обработчик сообщений
dp = Dispatcher(bot=bot)
# счетчик, сколько анекдотов бот выдал
count_of_anekdots = 0
# счетчик, сколько раз пользователь нажал кнопку назад
count_turned_back = 0


# данная функция вставляется в start_polling и выводит в командной строке сообщение в принте
async def working_message(_):
    print('Бот успешно запущен и работает!')


# строка с собакой - декоратор функции, которая отвечает за комманду /start, message_handler - обработчик полученных сообщений
# команды лучше прописывать в самом начале, так как если сначала прописать тип - текст, то любое введеное сообщение будет определяться как текст
@dp.message_handler(commands=['start'])
# в скобках явно и конкретно указываем, что нам нужен именно тип "сообщение"
async def start_command(message: types.Message):
    # отпрявляет стикер с обезьянкой
    # здесь нужно явно указывать айди чата, чтобы бот знал, куда и кому отправлять стикер
    # chat.id используется для отправки сообщения в группу и личку, from_user.id используется для отправки ТОЛЬКО в личку
    await bot.send_sticker(message.from_user.id,
                           sticker='CAACAgIAAxkBAAEGgXVjfNOtuTn4EpCXiwABiO5CpH0pR-sAAlQTAAIwS9FLhKW9odrtI-grBA')
    # когда указываешь parse_mode, нужно и явно указывать, что является текстом
    # parse_mode - отвечает за обработку текста в стиле HTML, так как в изначальном тексте у меня есть HTML элементы
    # выводим заготовленное стартовое сообщение и затем призыв к действию
    await bot.send_message(chat_id=message.from_user.id,
                           text=START_MESSAGE.format(bot_function),
                           parse_mode="HTML")
    await bot.send_message(chat_id=message.from_user.id,
                           text='Хотите расскажу анекдот?',
                           reply_markup=start_menu_keyboard)
    await message.delete()  # удаляет сообщение пользователя с командой, чтобы не засорять чат


# Далее идут функции команд без подробного описания - все основные моменты описаны в команде /start
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMANDS,
                           parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=BOT_DESCRIPTION.format(bot_function),
                           parse_mode="HTML")
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker='CAACAgIAAxkBAAEGhhZjfkiQAmJ1f0QPwxiksP_h1AaBbwACARQAAkd-2Uukq5EXc5ZdGisE')
    await message.delete()


@dp.message_handler(commands=['count'])
async def count_command(message: types.Message):
    global count_of_anekdots
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Бот рассказал тебе анекдот {count_of_anekdots} раз')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Тебе понравилось?😏',
                           reply_markup=keyboard_yes_or_no)
    await message.delete()


#Выводит прозрачное сообщение поверх всего, привязана к команде /count
@dp.callback_query_handler()
async def yes_or_no(callback: types.CallbackQuery):
    if callback.data == 'YES':
        await callback.answer('Спасибо!😳')
    elif callback.data == 'NO':
        await callback.answer(choice(NEGATIVE_ANSWER))


@dp.message_handler(commands=['sticker'])
async def sticker_command(message: types.Message):
    await bot.send_sticker(chat_id=message.from_user.id, sticker=choice(RANDOM_STIKERS))
    await message.delete()


# Основное тело бота - тут будет происходить вся магия(или нет, пока точно сказать не могу)
@dp.message_handler(Text(equals='Хочу анекдот!'))
async def lets_joke(message: types.Message):
    global count_turned_back
    if count_turned_back == 0:
        await bot.send_message(chat_id=message.from_user.id,
                               text='Отлично! Выбери тип анекдотов, который тебе по душе.',
                               reply_markup=keyboard_anekdots)
    elif count_turned_back > 0:
        await bot.send_message(chat_id=message.from_user.id, text='Ты вернулся!😍🥰')
        await bot.send_sticker(chat_id=message.from_user.id,
                               sticker='CAACAgIAAxkBAAEGgcJjfPSe_ZTgqK4eDpgtR1_R6ayOewACOhYAAopTEUjg9AEWxcK0uysE')
        await bot.send_message(chat_id=message.from_user.id, text='Выбери тип анекдотов, который тебе по душе.',
                               reply_markup=keyboard_anekdots)


@dp.message_handler(Text(equals='Не хочу анекдот!'))
async def no_jokes(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Ну ладно🥺')
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker='CAACAgIAAxkBAAEGgaxjfOrdgageaX8sdVgZT96CbgLmWgACyhYAAnQjGEmw8Cp6CRsmeCsE')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Если всё таки захочешь анекдот, нажми "Хочу анекдот"☺️.',
                           reply_markup=start_menu_keyboard)


@dp.message_handler(Text(equals='А'))
async def Anekdots_A(message: types.Message):
    global count_of_anekdots
    await bot.send_message(chat_id=message.from_user.id, text=choice(anekdots_A))
    count_of_anekdots += 1


@dp.message_handler(Text(equals='Б'))
async def Anekdots_B(message: types.Message):
    global count_of_anekdots
    await bot.send_message(chat_id=message.from_user.id, text=choice(anekdots_B))
    count_of_anekdots += 1


@dp.message_handler(Text(equals='Назад'))
async def return_back(message: types.Message):
    global count_turned_back
    await bot.send_message(chat_id=message.from_user.id,
                           text='Ну ладно.\nЕсли всё таки захочешь анекдот, нажми "Хочу анекдот"☺️.',
                           reply_markup=start_menu_keyboard)
    count_turned_back += 1


# эта конструкция означает то, что конкретно данный файл можно будет запустить только непосредственно
# т.е., не импортируя в другой файл, а только через терминал и только этот файл
if __name__ == '__main__':
    # on_startup  - выводит в консоли заготовленное сообщение при безошибочном запуске бота
    # skip_updates - пропускает любые сообщения от пользвателей за время, когда бот был неактивен
    # Запускаем самого бота с помощью экзекутора
    executor.start_polling(dp, on_startup=working_message, skip_updates=True)
