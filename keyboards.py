from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard():
    #Создание и возврат основной клавиатуры
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)  #Создание клавиатуры (кнопки будут подстраиваться под размер экрана)
    button_weather = KeyboardButton('Получить погоду', request_location=True) #Создание кнопки для отправки геопозиции
    button_about = KeyboardButton('О проекте')   #Создание кнопки о проекте
    keyboard.add(button_weather, button_about) #Добавление кнопки на клавиатуру
    return keyboard

