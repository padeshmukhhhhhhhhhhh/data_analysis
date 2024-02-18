from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
data= []
path=r'C:\Users\admin\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
service= Service(executable_path=path)
url=input("enter url \n")

with webdriver.Chrome(service=service) as driver:
    wait=WebDriverWait(driver, 10)
    driver.get(url)
    driver.maximize_window()
for item in range(3):
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(keys.END)
    time.sleep(3)
for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"#comment #content-text"))):
    data.append(comment.text)
print("comment scraped")
                                                              
df=pd.DataFrame(data)
df.to_csv("comment.csv")
