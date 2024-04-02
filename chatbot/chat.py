from chatterbot import ChatBot

from chatterbot.trainers import ChatterBotCorpusTrainer

chat = ChatBot('bot')

trainer = ChatterBotCorpusTrainer(chat)
trainer.train('chatterbot.corpus.spanish.greetings')

while True:
    peticion = input ('Tú: ')
    respuesta = chat.get_response(peticion)
    print('BOT: ', respuesta)