import os
import smtplib
import imghdr
from email.message import EmailMessage

import yfinance as yf
import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr

EMAIL_ADDRESS = os.environ.get('EMAIL.USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
start=dt.datetime(2018,12,1)
now = dt.datetime.now()

Crypto = "BTC"
TargetPrice= 30033
msg["Subject"]="Alert on"+Crypto
msg["From"]=EMAIL_ADDRESS
msg["To"]="satyajeet1234@gmail.com"
alerted= False

while 1:
    df = pdr.get_data_coinbase(stock,start,now)
    currentClose=df["Adj Close"][-1]

    condition = currentClose>TargetPrice
    if(condition and alerted == False):
        alerted= True
        message = stock +"Has activated the alert price of "+ str(TargetPrice) +\
            "\nCurrent Price: "+str(currentClose)
            msg.set_content(message)

            files=[r"C:\Users\Satyajeet\Documents\List.xlsx"]

            for file in files:
                with open(file,'rb') as f:
                    file_data=f.read()
                    file_name="List.xlsx"

                    msg.add_attachment(file_data, maintype="application",
                    subtype='ocetet-stream',filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465)as smtp:
                smtp.login(EMAIL_ADDRESS,EMAIL,PASSWORD)
                smtp.send_message(msg)

                print("completed")

    else:
        print("no new alerts")

    time.sleep(60)