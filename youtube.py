import requests
from bs4 import BeautifulSoup

url=input("input video url\n")

ws=requests.get(url)
data=BeautifulSoup(ws.text,"html.parser")
data1=data.find('meta',property='og:image')
thumbnail=data1['content']
image=requests.get(thumbnail)
file=open("video.jpg",'wb')
file.write(image.content)
file.close()
print("thumgnail downloaded")
 
