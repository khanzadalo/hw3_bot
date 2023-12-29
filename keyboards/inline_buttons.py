from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()
    registration_button = InlineKeyboardButton(
        "Registration 📑",
        callback_data="registration"
    )
    profile_button = InlineKeyboardButton(
        "My profile 😎",
        callback_data="profile"
    )
    view_profile_button = InlineKeyboardButton(
        "View Profiles 👍🏻👎🏻",
        callback_data="random_profile"
    )
    markup.add(registration_button)
    markup.add(profile_button)
    markup.add(view_profile_button)
    return markup


async def like_dislike_keyboard(owner_tg_id):
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "LIKE 👍🏻",
        callback_data=f"like_{owner_tg_id}"
    )
    dislike_button = InlineKeyboardButton(
        "DISLIKE 👎🏻",
        callback_data="random_profile"
    )
    markup.add(like_button)
    markup.add(dislike_button)
    return markup


async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "Update 🟢",
        callback_data=f"update_profile"
    )
    dislike_button = InlineKeyboardButton(
        "Delete ❌",
        callback_data="delete_profile"
    )
    markup.add(like_button)
    markup.add(dislike_button)
    return markup
