# Основной файл приложения. Запускать его!

from sklearn.feature_extraction.text import CountVectorizer     #pip install scikit-learn
from sklearn.linear_model import LogisticRegression
import words
import string
from aiogram import Bot, Dispatcher, executor, types
import os
import webbrowser
import sys
import subprocess
import config
# поключить нужный модуль

# модуль-заглушка
from alpaca_d import llminit, evaluate

# модель alpaca-lora
#from alpaca import alpaca_init, evaluate 

# модель g4f gpt external
# from g4f_external import init, evaluate



try:
	import requests		#pip install requests
except:
	pass

comand_text = ""

def change_comand(comand):
    comand_text = comand


def browser():
	'''Открывает браузер заданнный по уполчанию в системе с url указанным здесь'''

	webbrowser.open('https://www.youtube.com', new=2)


def game():
	'''Нужно разместить путь к exe файлу любого вашего приложения'''
	try:
		subprocess.Popen('C:/Program Files/paint.net/PaintDotNet.exe')
	except:
		print('Путь к файлу не найден, проверьте, правильный ли он')


def offpc():
	#Эта команда отключает ПК под управлением Windows
	os.system('shutdown \s')
	print('пк был бы выключен, но команде # в коде мешает;)))')


def weather():
	'''Для работы этого кода нужно зарегистрироваться на сайте
	https://openweathermap.org или переделать на ваше усмотрение под что-то другое'''
	try:
		print ("погода")
		params = {'q': 'Tula', 'units': 'metric', 'lang': 'ru', 'appid': 'ключ к API'}
		response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
		if not response:
			raise
		w = response.json()
		
	except:
		print('Произошла ошибка при попытке запроса к ресурсу API')


def offBot():
	#Отключает бота
	sys.exit()

def sw1on():
	global comand_text
	comand_text = "/on1"



def sw1off():
	global comand_text
	comand_text = "/off1"


def sw2on():
	global comand_text
	comand_text = '/on2'


def sw2off():
	global comand_text
	comand_text = '/off2'


def passive():
	'''Функция заглушка при простом диалоге с ботом'''
	pass


def remove_punctuation(text):
    # Создаем строку со всеми знаками пунктуации
    punctuation = string.punctuation
    
    # Удаляем знаки пунктуации из текста
    no_punct = ''.join(char for char in text if char not in punctuation)
    
    return no_punct

def recognize(data):
    result = "мне нечего на это ответить"
    
    #Анализ сообщения

    #Пропускаем все, если длина расспознанного текста меньше 7 символов
    if len(data) < 7:
        return result
    #если нет фразы обращения к ассистенту, то отправляем запрос альпаке
    lowdata = remove_punctuation(data.lower())
    trg = words.TRIGGERS.intersection(lowdata.split())
    if not trg:
        return evaluate (data)
    #если была фраза обращения к ассистенту
    #удаляем из команды имя асистента
    lowdata = lowdata.split()
    filtered_data = [word for word in lowdata if word not in words.TRIGGERS]
    lowdata = ' '.join(filtered_data)

    #получаем вектор полученного текста
    #сравниваем с вариантами, получая наиболее подходящий ответ
    # Преобразование команды пользователя в числовой вектор
    user_command_vector = vectorizer.transform([lowdata])
    # Предсказание вероятностей принадлежности к каждому классу
    predicted_probabilities = clf.predict_proba(user_command_vector)
    # Задание порога совпадения
    threshold = 0.05
    # Поиск наибольшей вероятности и выбор ответа, если он превышает порог
    max_probability = max(predicted_probabilities[0])
    print(max_probability)
    if max_probability >= threshold:
        answer = clf.classes_[predicted_probabilities[0].argmax()]
    else:
        return ("Команда не распознана")
     #получение имени функции из ответа из data_set
    func_name = answer.split()[0]
    #запуск  функции
    exec(func_name + '()')
    #возврат ответа
    return(answer.replace(func_name, ''))



#Обучение модели на data_set 

vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(list(words.data_set.keys()))
    
clf = LogisticRegression()
clf.fit(vectors, list(words.data_set.values()))



#инициализация большой языковой модели
llminit()

#del words.data_set

# запуск бота
bot = Bot(token=config.MAIN_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    if (len(config.TRUSTED_LIST)>0) and not (message.from_id  in config.TRUSTED_LIST):
        return
    await message.reply("Привет!\nЯ умный бот - персональный ассистент!\nМеня зовут Кеша.\nЯ могу много чего.\nОтправь мне любое сообщение, а я тебе обязательно отвечу.")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
	if (len(config.TRUSTED_LIST)>0) and not (message.from_id  in config.TRUSTED_LIST):
		return
	await message.reply("Для выполнения мной предопределенных команд обратитесь ко мне по имени")


#@dp.message_handler(commands=['settings'])
#async def send_welcome(message: types.Message):
#   await message.reply("Настройки")
 
@dp.message_handler()
async def echo(message: types.Message):
    global comand_text
    if (len(config.TRUSTED_LIST)>0) and not (message.from_id  in config.TRUSTED_LIST):
        return
    await message.answer(recognize(message.text))
    mess = comand_text
    comand_text = ""
    if len(mess)>0:
        await bot.send_message(config.CHAT_ID, mess)

	



if __name__ == '__main__':
     executor.start_polling(dp, skip_updates=True)
 

