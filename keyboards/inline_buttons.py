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
    reference_menu_button = InlineKeyboardButton(
        "Reference Menu 🧷",
        callback_data="reference_menu"
    )
    reference_list_button = InlineKeyboardButton(
        "Reference list 🧾",
        callback_data="reference_list"
    )
    parser_links_button = InlineKeyboardButton(
        "Parser",
        callback_data="parser_links"
    )
    markup.add(registration_button)
    markup.add(profile_button)
    markup.add(view_profile_button)
    markup.add(reference_menu_button)
    markup.add(reference_list_button)
    markup.add(parser_links_button)
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


async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    link_button = InlineKeyboardButton(
        "Link 🔗",
        callback_data="reference_link"
    )

    markup.add(link_button)
    return markup
