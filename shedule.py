import schedule
import time
class ab:
    def roj(self):
        print("you are human")


a=ab()

def rojj():
    print("you are male")

schedule.every(2).seconds.do(a.roj)
schedule.every(5).seconds.do(rojj)
while True:
    schedule.run_pending()
    time.sleep(1)
    
