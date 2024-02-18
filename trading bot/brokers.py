from SmartApi import SmartConnect
import pyotp
from logzero import logger
from database import assests
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


class stock:
    def main(self,exchange, tradingsymbol, symboltoken):
        
        lastprice=smartApi.ltpData(exchange,tradingsymbol,symboltoken)
        
       
       
        print(f"{tradingsymbol}={lastprice['data']['ltp']}")
        

ob=stock()

from threading import Thread




    
    

def go():
    threads=[]
    for i in assests:
        thread = Thread(target=ob.main, args=i)
        thread.start()
        threads.append(thread)
    for j in threads:
        j.join()

       
    # Wait for all threads to complete
   



schedule.every(5).seconds.do(go)
while True:
    schedule.run_pending()
    time.sleep(1)
      