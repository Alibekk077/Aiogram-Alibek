from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="bmw olik"),
        ],
        [
            KeyboardButton(text="merc sila"),
            KeyboardButton(text="audi")
        ],
    ],
    resize_keyboard=True
)