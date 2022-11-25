from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# здесь будут клавиатуры

# Немного теории:

# Про обычную клавиатуру(которая вылазит под полем ввода сообщения в телеграме):
# К ней относятся классы:
# ReplyKeyboardMarkup - функция вызова, для дальнейшего взаимодействия с клавиатурой
# принимает параметры:
# resize_keyboard(True/False) - отвечает за то, стоит ли подстаривать размеры клавиатуры под размеры экрана
# one_time_keyboard(True/False) - пропадёт ли клавиатура после одноразового взаимодействия с пользователем или будет отображаться постоянно
# KeyboardButton - класс кнопки клавиатуры
# ReplyKeyboardRemove - функция удаления клавиатуры в чате
# add - добавляет кнопку в столбец, insert - добавляет кнопку в ряд

# Про Inline-клавиатуру(клавиатура, которая прикреплена к сообщению):
# InlineKeyboardButton - кнопка, прикреппленная к сообщению, а не к полю ввода текста
# принимает параметры: text, url, callback_data, ... и ещё очень много всего
# InlineKeyboardMarkup - функция, которая возвращает обьект inline для дальнейшего использования
# принимает параметры: row_width(int) - указывает на количество кнопок
# в Inline клавиатурах добавление в столбец идёт в виде: .add(b1, b2, ...), а в новый ряд: .add(b1).add(b2)
# callback_data возвращает пакет данных, который в дальнейшем может быть обработан функцией CallvackQuery
# callback_data есть для обоих типов клавиатур, но явно почему-то указывается об этом только для инлайн-клавиатуры

# Стартовое меню выбора режимов
start_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton('Хочу анекдот!')
button2 = KeyboardButton('Не хочу анекдот!')
start_menu_keyboard.add(button1).insert(button2)

# Меню режима анекдотов
keyboard_anekdots = ReplyKeyboardMarkup(resize_keyboard=True)
button_anekdots_A = KeyboardButton('А')
button_anekdots_B = KeyboardButton('Б')
exit_anekdots_ = KeyboardButton('Назад')
keyboard_anekdots.add(button_anekdots_A).insert(button_anekdots_B).add(exit_anekdots_)

# Inline клавиатура для вопроса, понравились анекдоты или нет
keyboard_yes_or_no = InlineKeyboardMarkup(row_width=2)
yes_button = InlineKeyboardButton(text='Да🤤', callback_data='YES')
no_button = InlineKeyboardButton(text='Нет😬', callback_data='NO')
keyboard_yes_or_no.add(yes_button, no_button)