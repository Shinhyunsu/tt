#-*- coding:utf-8 -*-

import os
import json
import telegram
from flask import Flask, request, render_template
from flask_cors import CORS
import time
import schedule
import threading

app = Flask(__name__)

CORS(app)
dataBuffer = []
readData = ""


def schedule_job():
    print('okkkk')
    while len(dataBuffer) != 0:
        if len(dataBuffer) >= 1:
            readData = dataBuffer.pop();
            print('Processing... data -> ',readData)
        
        for keyread in readData.keys():
            if keyread == 'moving_exchange':
                chkkk = True
                chkkkk = False
            if keyread == 'maxVolume':
                chkkk = False
                chkkkk = True

        if chkkk == True:
            chkkk = False;
            totalString = 'π μ½μΈ : ' + readData['moving_exchange'] + ' κ±°λλ : ' + str(readData['volume']) + ' κΈμ‘ : ' + str(readData['price']) + ' μκ° : ' + str(readData['time'])
            print("MA send : ",totalString)

            bot = telegram.Bot(token='2105654811:AAEpHpQLLeE-e2qQ6s-kJ7MDeQV54iZJbo8')
            chat_id = '-1001678871735'
            bot.sendMessage(chat_id=chat_id, text=(totalString))

        elif chkkkk == True:
            chkkkk = False;
            totalString = 'π κ±°λλ Up μ½μΈ : ' + readData['maxVolume_exchange'] + ' κ±°λλ : ' + str(readData['volume']) + ' κΈμ‘ : ' + str(readData['price']) + ' μκ° : ' + str(readData['time'])
            print('volume send : ',totalString)

            bot = telegram.Bot(token='2105654811:AAEpHpQLLeE-e2qQ6s-kJ7MDeQV54iZJbo8')
            chat_id = '-1001678871735'
            bot.sendMessage(chat_id=chat_id, text=(totalString))

@app.route('/',methods=['GET', 'OPTIONS'])

def welcome():
    return render_template('index.html')

@app.route('/webhook',methods=['POST'])
def whatever():
    #global dataBuffer
    #global readData
    
    
    readData = json.loads(request.data)
    #reqdata = json.loads(request.data)
    #dataBuffer.append(reqdata)
    
    totalString = 'π μ½μΈ : ' + readData['moving_exchange'] + ' κ±°λλ : ' + str(readData['volume']) + ' κΈμ‘ : ' + str(readData['price']) + ' μκ° : ' + str(readData['time'])
    

    bot = telegram.Bot(token='2105654811:AAEpHpQLLeE-e2qQ6s-kJ7MDeQV54iZJbo8')
    chat_id = '-1001678871735'
    bot.sendMessage(chat_id=chat_id, text=(totalString))
    print("Send : ",totalString)

    return {
        "code": "succss",
        "message": readData
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


"""
def schedule_alarm():
    schedule.every().hour.at(":10").do(schedule_job)
    while True:
        schedule.run_pending() # pendingλ Jobμ μ€ν
        time.sleep(1)
 

alarm_thread = threading.Thread(target=schedule_alarm)
alarm_thread.start()
"""
 





