import requests
from config import API_KEY, URL_WEATHER_API
from emoji_dict import EMOJI_CODE

def get_weather(lat, lon):
    #Запрос к API и возврат строки с ответом.
    params = {
        'lat': lat,  #Широта
        'lon': lon,  #Долгота
        'lang': 'ru',  #Язык ответа - русский
        'units': 'metric',  #Градусы Цельсия
        'appid': API_KEY  #Наш ключ доступа
    }

    try: #Отправление запроса на сервер
        response = requests.get(url=URL_WEATHER_API, params=params)
        response.raise_for_status()
        weather_data = response.json()  #Преобразуем ответ в Python-словарь

        #Достает нужные данные из ответа
        city_name = weather_data.get('name', 'Неизвестное место') #Получение названия города
        weather_info = weather_data['weather'][0] #Получение информации о погоде
        description = weather_info['description'] #Получение описания погоды
        code = weather_info['id'] #Получение кода погоды
        main_info = weather_data['main'] #Получение основной информации о температуре
        temp = main_info['temp'] #Получение температуры
        temp_feels_like = main_info['feels_like'] #Получение ощущаемой температуры
        humidity = main_info['humidity'] #Получение влажности

        emoji = EMOJI_CODE.get(code, '❓')#Выбирает смайлик по коду погоды

        message_text = f"📍 *Информация о погоде в {city_name}:*\n\n"
        message_text += f"{emoji} *Условия:* {description.capitalize()}\n"
        message_text += f"🌡️ *Температура:* {temp}°C\n"
        message_text += f"🤔 *Ощущается как:* {temp_feels_like}°C\n"
        message_text += f"💧 *Влажность:* {humidity}%\n"

        return message_text

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return "😔 Не удалось получить данные о погоде. Попробуй позже." #Если ошибка с интернетом или сервером
    except (KeyError, IndexError, ValueError) as e:
        print(f"Ошибка при обработке данных: {e}")
        return "😕 Получен некорректный ответ от сервера погоды." #Если сервер вернул непонятные данные