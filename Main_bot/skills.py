import os
import webbrowser
import sys
import subprocess


try:
	import requests		#pip install requests
except:
	pass


def change_comand(comand):
	print(comand)
    #app.comand_text = comand

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
		print('Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def offBot():
	'''Отключает бота'''
	sys.exit()




def lampon():
	print("lampon")
	#app.change_comand("/on1")
	#app.comand_text = "/on1"



def lampoff():
	app.comand_text = "/off1"


def sw2on():
	app.comand_text = '/on2'


def sw2off():
	app.comand_text = '/off2'


def passive():
	'''Функция заглушка при простом диалоге с ботом'''
	pass