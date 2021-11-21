#-*- coding:utf-8 -*-

import os
import json
import telegram
from flask import Flask, request, render_template
from flask_cors import CORS
import time
from datetime import datetime
#from flask_apscheduler import APScheduler
#from apscheduler.schedulers.blocking import BlockingScheduler
import schedule
from threading import Thread

start_time = time.time()

def run_every_10_seconds():
    print("Running periodic task!")
    print ("Elapsed time: " + str(time.time() - start_time))

def run_schedule():
    
    while 1:
        
        schedule.run_pending()
        time.sleep(1)   


app = Flask(__name__)
#scheduler = APScheduler()
#scheduler = BlockingScheduler()

CORS(app)
dataBuffer = []
coinName =[]
readData = ""

def job():
    print('time ok')




@app.route('/',methods=['GET', 'OPTIONS'])
def welcome():
    
    return render_template('index.html')

@app.route('/webhook',methods=['POST'])
def whatever():
    global coinName
    global dataBuffer
    global readData
    nowTime = datetime.now()
    
    
    
    
    reqdata = json.loads(request.data)
    print('pint',nowTime.hour,nowTime.minute, reqdata)
    dataBuffer.append(reqdata)
    

    if nowTime.hour == 0 and  nowTime.minute >= 10 and nowTime.minute <= 20:
        trig = True;
        
    else:
        chkkk = False;
        chkkkk = False;
        trig = False;

    if trig == True:
        if len(dataBuffer) > 1:
            readData = dataBuffer.popleft();
            print('Processing... data -> ',readData)
        elif  len(dataBuffer) == 1:
            readData = dataBuffer.pop();
            print('Processing... data -> ',readData)
        else :
            trig = False;

        for keyread in readData.keys():
            if keyread == 'moving_exchange':
                chkkk = True
                chkkkk = False
            if keyread == 'maxVolume':
                chkkk = False
                chkkkk = True
            #if keyread == 'trigger_exchange':
                #if trigger == True


    
        if chkkk == True:
            chkkk = False;
            totalString = '🔔 코인 : ' + readData['moving_exchange'] + ' 거래량 : ' + str(readData['volume']) + ' 금액 : ' + str(readData['price']) + ' 시간 : ' + str(readData['time'])
            print("MA send : ",totalString)

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
    #scheduler.add_job(id="scheduler task", func = job, trigger='interval', minute =2)
    # scheduler.add_job(job, 'cron', second='*/60', id="test_1")
    #scheduler.add_job(func=job, trigger='cron', second='*/60')
    #scheduler.start()

    


    print("main play")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


schedule.every(10).seconds.do(run_every_10_seconds)
t = Thread(target=run_schedule)
t.start()