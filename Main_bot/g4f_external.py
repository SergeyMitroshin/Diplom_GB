# модуль - заглушка для отладки на слабом ПК, где мы либо не можем запустить большую
# языковую модель, либо она работает медленно и мешает работе по отладке.

import g4f

from g4f.Provider import (
    AItianhu,
    Acytoo,
    Aichat,
    Ails,
    Bard,
    Bing,
    ChatBase,
    ChatgptAi,
    H2o,
    HuggingChat,
    OpenAssistant,
    OpenaiChat,
    Raycast,
    Theb,
    Vercel,
    Vitalentum,
    Ylokh,
    You,
    Yqcloud,
)






def llminit():
    response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    provider=g4f.Provider.Aichat,
    messages=[{"role": "user", "content": "Hello"}])
    for message in response:
        print(message)
    # print ("alpaca стартовала успешно")

def evaluate(instruction, input=None):
    response = instruction
    print(response)
    return(response)