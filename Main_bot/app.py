'''
Требуется:
pip install scikit-learn


pip install --force-reinstall -v "aiogram==2.23.1"

pip install pyttsx3

Не обязательно:
pip install requests

Для получения справки, спроси у него 'Что ты умеешь Кеша?' или 'справка Кеша'

'''


from sklearn.feature_extraction.text import CountVectorizer     #pip install scikit-learn
from sklearn.linear_model import LogisticRegression
import words
import string
from skills import *
from alpaca_d import alpaca_init, evaluate
from aiogram import Bot, Dispatcher, executor, types

MAIN_TOKEN = '5800510923:AAGGIu2AuPktr_F6RmeJvwR-pbO-m5Q8D6o'

#def recognize(data, vectorizer, clf):

def remove_punctuation(text):
    # Создаем строку со всеми знаками пунктуации
    punctuation = string.punctuation
    
    # Удаляем знаки пунктуации из текста
    no_punct = ''.join(char for char in text if char not in punctuation)
    
    return no_punct

def recognize(data):
    result = "мне нечего на это ответить"
    '''
    Анализ распознанной речи
    '''
    #Пропускаем все, если длина расспознанного текста меньше 7 символов
    print(data)
    if len(data) < 7:
        return result
    #если нет фразы обращения к ассистенту, то отправляем запрос альпаке
    lowdata = remove_punctuation(data.lower())
    print(lowdata)
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
    threshold = 0.09

    # Поиск наибольшей вероятности и выбор ответа, если он превышает порог
    max_probability = max(predicted_probabilities[0])
    print(max_probability)
    if max_probability >= threshold:
        answer = clf.classes_[predicted_probabilities[0].argmax()]
    else:
        return ("Команда не распознана")
    

    #получение имени функции из ответа из data_set
    func_name = answer.split()[0]

    #возврат ответа из модели data_set
    return(answer.replace(func_name, ''))

    #запуск функции из skills
    exec('commands.' + func_name + '()')
    



#Обучение модели на data_set 

print("stage1")
vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(list(words.data_set.keys()))
    
clf = LogisticRegression()
clf.fit(vectors, list(words.data_set.values()))

#инициализация большой языковой модели
alpaca_init()

#del words.data_set

# запуск бота
bot = Bot(token=MAIN_TOKEN)
dp = Dispatcher(bot)
print("stage2")

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("Привет!\nЯ умный бот - персональный ассистент!\nМеня зовут Кеша.\nЯ могу много чего.\nОтправь мне любое сообщение, а я тебе обязательно отвечу.")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
   await message.reply("Подсказка")

#@dp.message_handler(commands=['settings'])
#async def send_welcome(message: types.Message):
#   await message.reply("Настройки")
 
@dp.message_handler()
async def echo(message: types.Message):
   await message.answer(recognize(message.text))



if __name__ == '__main__':
     executor.start_polling(dp, skip_updates=True)
 

