from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()
    registration_button = InlineKeyboardButton(
        "Registration 📑",
        callback_data="registration"
    )
    markup.add(registration_button)
    return markup


