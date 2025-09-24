from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

language_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")],
        [InlineKeyboardButton(text="🇰🇬 Кыргызча", callback_data="lang_ky")],
        [InlineKeyboardButton(text="🇺🇿 Oʻzbekcha", callback_data="lang_uz")],
        [InlineKeyboardButton(text="🇰🇿 Қазақ тілі", callback_data="lang_kk")],
        [InlineKeyboardButton(text="🇧🇾 Беларуская", callback_data="lang_be")],
        [InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")],
        [InlineKeyboardButton(text="🇦🇿 Azərbaycan", callback_data="lang_az")],
        [InlineKeyboardButton(text="🔙 Back", callback_data="back")]
    ]
)

country_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🇷🇺 Россия", callback_data="country_ru")],
        [InlineKeyboardButton(text="🇰🇬 Кыргызстан", callback_data="country_ky")],
        [InlineKeyboardButton(text="🇺🇿 Oʻzbekiston", callback_data="country_uz")],
        [InlineKeyboardButton(text="🇧🇾 Беларусь", callback_data="country_be")],
        [InlineKeyboardButton(text="🇰🇿 Қазақстан", callback_data="country_kk")],
        [InlineKeyboardButton(text="🌏 Bot languge | Язык бота", callback_data="choose_languge")]
    ]
)




REGISTRATION_LINKS = {
    "ru": "https://reg.eda.yandex.ru/?advertisement_campaign=forms_for_agents&user_invite_code=9161e68b422748e5816cb8c1802d9f7f&utm_content=blank&clckid=5420b0b6",
    "uz": "https://reg.eda.yandex.uz/?advertisement_campaign=eats_park&user_login_creator=directsaleads&utm_term=f1547190-9914-11f0-831b-d105c30ac14b&utm_medium=9065b900-237e-11f0-a144-e98fc589c5dc&utm_content=f1547190-9914-11f0-831b-d105c30ac14b&utm_campaign=9065b900-237e-11f0-a144-e98fc589c5dc&utm_source=9065b900-237e-11f0-a144-e98fc589c5dc",
    "ky": "slds.pro/y8qlu",
    "be": "slds.pro/0opf9",
    "kz": "slds.pro/d58pk",
}
def country_actions_keyboard(country_code: str):
    registration_url = REGISTRATION_LINKS.get(country_code, REGISTRATION_LINKS["ru"])
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🚀 Быстрая регистрация", url=registration_url)
        ],
        [
            InlineKeyboardButton(text="🤝🏼 Позвать друга", switch_inline_query="invite")  # пользователю предложит выбрать чат для пересылки
        ],
        [
            InlineKeyboardButton(text="🌍 Работа в других странах", callback_data="back_to_countries")
        ]
    ])
    return keyboard