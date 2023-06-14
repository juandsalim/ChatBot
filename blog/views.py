from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot('chat',read_only=False,
              logic_adapters=[
                    {
                        'import_path':'chatterbot.logic.BestMatch',
                        # 'default_response':'Sorry, I dont know what that means',
                        # 'maximum_similarity_threshold':0.95
                               
                               
                               
                     }])

list_to_train=[
    "hi", 
    "hi, there", 
    "what´s your name?", 
    "i´m just a chatbot",
    "what is your fav food?",
    "I like cheese"
]

# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train)

ChatterBotCorpusTrainer = ChatterBotCorpusTrainer(bot) 

ChatterBotCorpusTrainer.train('chatterbot.corpus.english')

def index(request):
    return render(request,'blog/index.html')


def specific(request):
    return HttpResponse("this is the specific url")

  
def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)