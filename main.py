import telebot
from config import TOKEN
from keyboards import get_main_keyboard
from weather_api import get_weather

bot = telebot.TeleBot(TOKEN) #Создание бота
keyboard = get_main_keyboard() #Получение клавиатуры

@bot.message_handler(commands=['start']) #Начало работы(приветствие)
def send_welcome(message):
    welcome_text = (
        "👋 Сап! Я тот, кто пояснит тебе все о погоде.\n\n"
        "Чтобы узнать погоду, нажми кнопку 'Получить погоду' и отправь мне свою геопозицию.\n"
        "Также можешь узнать обо мне, нажав кнопку 'О проекте'."
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)

@bot.message_handler(regexp='О проекте') #Кнопка о проекте
def send_about(message):
    #Сообщение с информацией о боте и его создателе.
    about_text = (
        "ℹ️ *Информация о боте:*\n\n"
        "📌 *Название:* PogodaBro\n"
        "📌 *Версия:* 1.0\n"
        "📌 *Описание:* Этот бот показывает текущую погоду в вашем местоположении, используя данные OpenWeatherMap.\n"
        "📌 *Автор:* [Robekorech1]\n"
    )
    bot.send_message(message.chat.id, about_text, parse_mode='Markdown', reply_markup=keyboard)

@bot.message_handler(content_types=['location'])
def send_weather(message):
    #Извлечение координат и отправка ответа.
    lon = message.location.longitude #Долгота
    lat = message.location.latitude  #Широта

    bot.send_chat_action(message.chat.id, 'typing') #Бот "печатает"
    bot.send_message(message.chat.id, "🔍 Получаю данные о погоде...") #Бот начал обработку

    weather_message = get_weather(lat, lon) #Получает погоду (вызывает функцию из weather_api.py)

    bot.send_message(message.chat.id, weather_message, parse_mode='Markdown', reply_markup=keyboard) #Отправляет результат
#Запуск бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()