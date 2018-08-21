from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot(
    'My Chatbot',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

chatterbot = ChatBot("My Personal Assistant",storage_adapter="chatterbot.storage.SQLStorageAdapter")
chatterbot.set_trainer(ListTrainer)

chatterbot.train([
    "Hi!",
    "Hello!",
])

# Quick Testing
print("Hi!")
response = chatterbot.get_response("Hi!")
print(response)
