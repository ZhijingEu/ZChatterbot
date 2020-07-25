from flask import Flask, render_template, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Friend') #create the bot 

trainer=ListTrainer(bot)

#Turn this back on if you rather use Chatterbot's pre-set corpus
#trainer.train("chatterbot.corpus.english") 

#If using your own data or chat history to train, leave this open
for knowledege in os.listdir('base'):
	BotMemory = open('base/'+ knowledege, 'r').readlines()
	trainer.train(BotMemory)



app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process',methods=['POST'])
def process():
	incoming_msg = request.values.get('Body', '').lower()
	resp = MessagingResponse()
	msg = resp.message()
	bot_response=bot.get_response(incoming_msg)
	msg.body(str(bot_response))
	return str(resp)

if __name__=='__main__':
	app.run(debug=True,port=5002)