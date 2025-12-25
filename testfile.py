import json
import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters
from Slovar import recipes

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Супы🥘", "Салаты🥗", "Напитки☕️🍸"],
        ["Дессерты🍰", "Закуски🍢", "На праздники🥂"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Выбери категорию кулинарных шедевров, из которой хотели бы, что-нибудь приготовить",
        reply_markup=reply_markup
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет я самый лучший кулинарный бот🥠🍚. Введи команду /menu , чтобы запустить бота")

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "На праздники🥂":
        # СОЗДАЕМ клавиатуру для праздников
        holiday_keyboard = ReplyKeyboardMarkup(
            [
                ["Новый год🎄🎅", "Пасха☦️", "День рождения🥳🎉"],
                ["Назад🔙"]
            ],
            resize_keyboard=True
        )
        # ОТПРАВЛЯЕМ сообщение с этой клавиатурой
        await update.message.reply_text(
            "Выберите праздник:",
            reply_markup=holiday_keyboard
        )

    elif text == "Назад🔙":
        # Возвращаемся в главное меню
        keyboard = [
            ["Супы🥘", "Салаты🥗", "Напитки☕️🍸"],
            ["Дессерты🍰", "Закуски🍢", "На праздники🥂"]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text(
            "Главное меню:",
            reply_markup=reply_markup
        )

    elif text == "Супы🥘":
        all_recipes_text = "🍲 **Все супы:**\n\n"

        for i, recipe in enumerate(recipes["супы"], 1):
            all_recipes_text += f"**{i}. {recipe['название']}**\n"
            all_recipes_text += f"{recipe['краткое_описание']}\n"

            # Добавляем ингредиенты
            ingredients = "\n".join([f"   • {ing}: {amt}" for ing, amt in recipe['ингредиенты_на_порцию'].items()])
            all_recipes_text += f"Ингредиенты:\n{ingredients}\n\n"
            all_recipes_text += "─" * 30 + "\n\n"

        await update.message.reply_text(all_recipes_text, parse_mode='Markdown')

    elif text == "Салаты🥗":
        all_recipes_text = "🥗 **Все салаты:**\n\n"

        for i, recipe in enumerate(recipes['салаты'], 1):
            all_recipes_text += f"**{i}. {recipe['название']}**\n"
            all_recipes_text += f"{recipe['краткое_описание']}\n"

            ingredients = "\n".join([f"   • {ing}: {amt}" for ing, amt in recipe['ингредиенты_на_порцию'].items()])
            all_recipes_text += f"Ингредиенты:\n{ingredients}\n\n"
            all_recipes_text += "─" * 30 + "\n\n"

        await update.message.reply_text(all_recipes_text, parse_mode='Markdown')

    elif text == "Напитки☕️🍸":
        all_recipes_text = "🥤🍸 **Все напитки:**\n\n"

        for i, recipe in enumerate(recipes['напитки'], 1):
            all_recipes_text += f"**{i}. {recipe['название']}**\n"
            all_recipes_text += f"{recipe['краткое_описание']}\n"

            ingredients = "\n".join([f"   • {ing}: {amt}" for ing, amt in recipe['ингредиенты_на_порцию'].items()])
            all_recipes_text += f"Ингредиенты:\n{ingredients}\n\n"
            all_recipes_text += "─" * 30 + "\n\n"

        await update.message.reply_text(all_recipes_text, parse_mode='Markdown')\

    elif text == "Дессерты🍰":

        all_recipes_text = "🥧🎂 **Все дессерты:**\n\n"

        for i, recipe in enumerate(recipes['десерты'], 1):
            all_recipes_text += f"**{i}. {recipe['название']}**\n"
            all_recipes_text += f"{recipe['краткое_описание']}\n"

            ingredients = "\n".join([f"   • {ing}: {amt}" for ing, amt in recipe['ингредиенты_на_порцию'].items()])
            all_recipes_text += f"Ингредиенты:\n{ingredients}\n\n"
            all_recipes_text += "─" * 30 + "\n\n"

        await update.message.reply_text(all_recipes_text, parse_mode='Markdown')

    elif text == "Закуски🍢":
        all_recipes_text = "🍟 **Все закуски:**\n\n"

        for i, recipe in enumerate(recipes['закуски'], 1):
            all_recipes_text += f"**{i}. {recipe['название']}**\n"
            all_recipes_text += f"{recipe['краткое_описание']}\n"

            ingredients = "\n".join([f"   • {ing}: {amt}" for ing, amt in recipe['ингредиенты_на_порцию'].items()])
            all_recipes_text += f"Ингредиенты:\n{ingredients}\n\n"
            all_recipes_text += "─" * 30 + "\n\n"

        await update.message.reply_text(all_recipes_text, parse_mode='Markdown')

    elif text == "Новый год🎄🎅":
        all_recipes_text = "🎅🎇 **Всё на Новый год:**\n\n"

        for i, recipe in enumerate(recipes['на_праздники']['новый_год'], 1):
            all_recipes_text += f"**{i}. {recipe['название']}**\n"
            all_recipes_text += f"{recipe['краткое_описание']}\n"

            ingredients = "\n".join([f"   • {ing}: {amt}" for ing, amt in recipe['ингредиенты_на_порцию'].items()])
            all_recipes_text += f"Ингредиенты:\n{ingredients}\n\n"
            all_recipes_text += "─" * 30 + "\n\n"

        await update.message.reply_text(all_recipes_text, parse_mode='Markdown')

    elif text == "Пасха☦️":
        all_recipes_text = "☦️ **Всё на Пасху:**\n\n"

        for i, recipe in enumerate(recipes['на_праздники']['пасха'], 1):
            all_recipes_text += f"**{i}. {recipe['название']}**\n"
            all_recipes_text += f"{recipe['краткое_описание']}\n"

            ingredients = "\n".join([f"   • {ing}: {amt}" for ing, amt in recipe['ингредиенты_на_порцию'].items()])
            all_recipes_text += f"Ингредиенты:\n{ingredients}\n\n"
            all_recipes_text += "─" * 30 + "\n\n"

        await update.message.reply_text(all_recipes_text, parse_mode='Markdown')

    elif text == "День рождения🥳🎉":
        all_recipes_text = "🎉🎈 **Всё на День рождение:**\n\n"

        for i, recipe in enumerate(recipes['на_праздники']['день_рождения'], 1):
            all_recipes_text += f"**{i}. {recipe['название']}**\n"
            all_recipes_text += f"{recipe['краткое_описание']}\n"

            ingredients = "\n".join([f"   • {ing}: {amt}" for ing, amt in recipe['ингредиенты_на_порцию'].items()])
            all_recipes_text += f"Ингредиенты:\n{ingredients}\n\n"
            all_recipes_text += "─" * 30 + "\n\n"

        await update.message.reply_text(all_recipes_text, parse_mode='Markdown')

def main():
    TOKEN = ""

    # ВАЖНО: скройте токен перед публикацией кода!
    # Лучше использовать переменные окружения:
    # import os
    # TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    app = ApplicationBuilder().token(TOKEN).build()

    # Регистрируем обработчики команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))

    # Обработчик текстовых сообщений (для кнопок)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

    # Запускаем бота
    print("Бот запущен...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()

