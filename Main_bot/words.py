'''Тут слова на которые реагирует бот, что 
обращение было к нему. Его имя и команда могут быть сказаны
в любой последовательности и даже в перемешку и тд...,
'''

TRIGGERS = {'кеша','иннокентий','инокентий','кеш','кешенька','кешунчик'}



#Данные для модели ИИ

data_set = {
'какая погода': 'weather сейчас скажу',
'какая погода на улице': 'weather боишься замерзнуть?',
'что там на улице': 'weather сейчас гляну...',
'сколько градусов': 'weather можешь выглянуть в окно, но сейчас проверю',
'запусти браузер': 'browser запускаю браузер',
'открой браузер': 'browser интернет активирован',
'интернет открой': 'browser открываю браузер',
'посмотреть фильм': 'browser сейчас открою браузер',
'играть': 'game лишь бы баловаться',
'хочу поиграть в игру': 'game а нам лишьбы баловаться',
'запусти игру': 'game запускаю игру, а тебе лишь бы баловаться',
'выключи компьютер': 'offpc отключаю компьютер',
'отключись': 'offBot отключаюсь',
'как дела': 'passive да работаю я, не переживай',
'что делаешь': 'passive жду очередной команды от тебя',
'привет': 'passive и тебе привет',
'здравствуй': 'passive и тебе привет',
'расскажи анекдот': 'passive Вчера помыл окна, теперь у меня рассвет на два часа раньше...',
'работаешь': 'passive как видишь',
'ты тут': 'passive я всегда здесь',
'ты здесь': 'passive я всегда здесь',
'что ты умеешь': 'passive я умею узнавать погоду, могу открыть браузер, запустить exe файл, выключить пк, отключиться, рассказать анекдот и еще всё то, чему ты меня научишь',
'справка': 'passive я умею узнавать погоду, могу открыть браузер, запустить exe файл, выключить пк, отключиться, рассказать анекдот и еще всё то, чему ты меня научишь',
'включи свет': 'sw1on включаю свет',
'зажги свет': 'sw1on включаю свет',
'выключи свет': 'sw1off выключаю свет',
'погаси свет': 'sw1off выключаю свет',
'включи розетку': 'sw2on включаю розетку',
'выключи розетку': 'sw2off выключаю розетку'
}