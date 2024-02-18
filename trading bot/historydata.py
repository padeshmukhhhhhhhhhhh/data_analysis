from SmartApi import SmartConnect
import pyotp
from logzero import logger
import pandas as pd
import schedule
import time
import talib as ta
api_key="Fh7Yx6v6"
try:
    token = "BVRHBRPZV7XRLWEDB3GUK26YGA"
    totp = pyotp.TOTP(token).now()
except Exception as e:
    logger.error("Invalid Token: The provided token is not valid.")
    raise e

smartApi = SmartConnect(api_key)
username="V405113"
pwd='3792'
data = smartApi.generateSession(username, pwd,totp)







try:
        historicParam={
        "exchange": "NSE",
        "symboltoken": "3045",
        "interval": "FIVE_MINUTE",
        "fromdate": "2024-01-01 09:00", 
        "todate": "2024-02-09 03:15"
        }
        data=smartApi.getCandleData(historicParam)
        format_data=pd.DataFrame(data)
        #print(format_data["data"])
        
        new_data = pd.DataFrame(format_data["data"].apply(pd.Series),)
        new_data.rename(columns={0: "time",1:"open",2:"high",3:"low",4:"close",5:"volume"}, inplace=True)
        #new_data=pd.DataFrame(format_data["data"],columns = columns)
        new_data["rsi"]=ta.RSI(new_data["close"],timeperiod=14)
        print(new_data.to_markdown())
except Exception as e:
        logger.exception(f"Historic Api failed: {e}")
buy=[]
sell=[]
position=False
for i in range(14,len(new_data)):

    if position==False and new_data.iloc[i, new_data.columns.get_loc('rsi')] < 30:
        print("buy")
        position=True
        print(new_data.iloc[i, new_data.columns.get_loc('close')])
        buy.append(new_data.iloc[i, new_data.columns.get_loc('close')])
    elif position==True and new_data.iloc[i, new_data.columns.get_loc('rsi')] > 70:
        print("sell")
        position=False
        print(new_data.iloc[i, new_data.columns.get_loc('close')])
        sell.append(new_data.iloc[i, new_data.columns.get_loc('close')])
    else:
        pass
