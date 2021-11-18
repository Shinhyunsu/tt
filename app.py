#-*- coding:utf-8 -*-

import os
import json
import telegram
from flask import Flask, request, render_template
from flask_cors import CORS
import time
from datetime import datetime

app = Flask(__name__)
CORS(app)
dataBuffer = []
coinName =[]


#rint('hour',nowTime.hour)

@app.route('/',methods=['GET', 'OPTIONS'])
def welcome():
    
    return render_template('index.html')

@app.route('/webhook',methods=['POST'])
def whatever():
    global coinName
    nowTime = datetime.now()
   
    dataBuffer.append(json.loads(request.data))
    
     if nowTime.hour === 12 and  nowTime.minuate >= 40 and  nowTime.minuate <= 50 :
        trig = True;
    else:
        chkkk = False;
        chkkkk = False;
        trig = False;

    if trig = True:
        if len(dataBuffer) > 0 :
            readData = dataBuffer.popleft();
            print('Processing... data -> 'readData)
        else   
            trig = False;

        for keyread in readData.keys():
            if keyread == 'moving_exchange':
                chkkk = True
                chkkkk = False
            if keyread == 'maxVolume':
                chkkk = False
                chkkkk = True
    
        if chkkk == True:
            chkkk = False;
            totalString = '🔔 코인 : ' + readData['moving_exchange'] + ' 거래량 : ' + str(readData['volume']) + ' 금액 : ' + str(readData['price']) + ' 시간 : ' + str(readData['time'])
            print('MA send : ',totalString)

            bot = telegram.Bot(token='2105654811:AAEpHpQLLeE-e2qQ6s-kJ7MDeQV54iZJbo8')
            chat_id = '-1001678871735'
            bot.sendMessage(chat_id=chat_id, text=(totalString))

        elif chkkkk == True:
            chkkkk = False;
            totalString = '📈 거래량 Up 코인 : ' + readData['maxVolume_exchange'] + ' 거래량 : ' + str(readData['volume']) + ' 금액 : ' + str(readData['price']) + ' 시간 : ' + str(readData['time'])
            print('volume send : ',totalString)

            bot = telegram.Bot(token='2105654811:AAEpHpQLLeE-e2qQ6s-kJ7MDeQV54iZJbo8')
            chat_id = '-1001678871735'
            bot.sendMessage(chat_id=chat_id, text=(totalString))

    return {
        "code": "succss",
        "message": readData
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)