from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, FSInputFile
from aiogram.filters import Command
import asyncio
import logging

BOT_TOKEN = "7978424162:AAFPgLhoSu2zAlwepRQW59cQdK34PKmciNo"

# Инициализация
logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()
#======================================================================


# Клавиатуры
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Производственная активность")],
        [KeyboardButton(text="Погода")],
        [KeyboardButton(text="Общая информация")]
    ],
    resize_keyboard=True
)

@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Выберите пункт:", reply_markup=main_keyboard)

@router.message(lambda message: message.text == "Производственная активность")
async def handle_prom_activ(message: Message):
    await message.answer("Здесь представлены дашборды по бизнес-процессу производственная активность", reply_markup=prom_activ_keyboard)

@router.message(lambda message: message.text == "Погода")
async def handle_weather(message: Message):
    await message.answer("Здесь представлены дашборды по бизнес-процессу погода", reply_markup=weather_keyboard)

@router.message(lambda message: message.text == "Общая информация")
async def handle_info(message: Message):
    await message.answer("Здесь представлена общая информация по бизнес-процессам", reply_markup=info_keyboard)


#======================================================================
prom_activ_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Доходы/расходы")],
        [KeyboardButton(text="Сумма по цехам")],
        [KeyboardButton(text="Распределение суммы")],
        [KeyboardButton(text="В главное меню")]
    ],
    resize_keyboard=True
)

@router.message(lambda message: message.text == "Доходы/расходы")
async def handle_pic1(message: Message):
    image_path = "img/var1/graph.jpg"  # Замените на ваш путь к изображению
    photo = FSInputFile(image_path)
    await bot.send_photo(chat_id=message.chat.id, photo=photo, caption="Линейный график демонстрирует динамику доходов и расходов по времени, что помогает пользователям отслеживать изменения.")


@router.message(lambda message: message.text == "Сумма по цехам")
async def handle_pic2(message: Message):
    image_path = "img/var1/pie.jpg"  # Замените на ваш путь к изображению
    photo = FSInputFile(image_path)
    await bot.send_photo(chat_id=message.chat.id, photo=photo, caption="Круговая диаграмма визуализирует структуру расходов по категори-ям, позволяя понять, на что уходят основные средства.")


@router.message(lambda message: message.text == "Распределение суммы")
async def handle_pic3(message: Message):
    image_path = "img/var1/diagram.jpg"  # Замените на ваш путь к изображению
    photo = FSInputFile(image_path)
    await bot.send_photo(chat_id=message.chat.id, photo=photo, caption="Гистограмма анализирует распределение прибыли, выявляя наиболее прибыльные и убыточные участки бизнеса.")


#======================================================================

weather_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Температура")],
        [KeyboardButton(text="Облачность")],
        [KeyboardButton(text="Ветренность")],
        [KeyboardButton(text="В главное меню")]
    ],
    resize_keyboard=True
)

@router.message(lambda message: message.text == "Температура")
async def handle_pic4(message: Message):
    image_path = "img/var2/temp.jpg"
    photo = FSInputFile(image_path)
    await bot.send_photo(chat_id=message.chat.id, photo=photo, caption="График показывает изменение температуры в течение времени.")

@router.message(lambda message: message.text == "Облачность")
async def handle_pic5(message: Message):
    image_path = "img/var2/pie_cloud.jpg"
    photo = FSInputFile(image_path)
    await bot.send_photo(chat_id=message.chat.id, photo=photo, caption="Круговая диаграмма показывает соотношение степеней облачности по количеству дней.")


@router.message(lambda message: message.text == "Ветренность")
async def handle_pic6(message: Message):
    image_path = "img/var2/rose_wind.jpg"
    photo = FSInputFile(image_path)
    await bot.send_photo(chat_id=message.chat.id, photo=photo, caption="Роза ветров изображает в количестве сколько в данное направление дул ветер.")

#======================================================================
info_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="О боте")],
        [KeyboardButton(text="Что такое дашборд")],
        [KeyboardButton(text="В главное меню")]
    ],
    resize_keyboard=True
)

@router.message(lambda message: message.text == "О боте")
async def handle_about(message: Message):
    await message.answer("Данный бот написан на языке Python и позволяет получить изображения дашбордов по темам 'Погода' или 'Производственная активность'. Дашборды написаны на библиотеке Dash (Plotly), а также Pandas для доступа к базе данных.")

@router.message(lambda message: message.text == "Что такое дашборд")
async def handle_about(message: Message):
    await message.answer("Дашборд (от англ. dashboard) — это инструмент визуализации данных, который представляет собой интерактивный интерфейс, позволяющий быстро и наглядно отслеживать ключевые метрики, показатели или процессы.")

#======================================================================

@router.message(lambda message: message.text == "В главное меню")
async def handle_back(message: Message):
    await message.answer("Возвращаемся в главное меню:", reply_markup=main_keyboard)

#======================================================================
# Обработчик для любых других сообщений
@router.message()
async def handle_unknown(message: Message):
    await message.answer("Пожалуйста, используйте доступные кнопки.")

# Запуск
async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
