import requests
from bs4 import BeautifulSoup
import lxml
import json
from datetime import datetime as dt
import socket
import sys



def send_data(data):
    host='127.0.0.1'
    port=80
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((host, port))
    msg=data
    sock.send(msg.encode('utf-8'))
    sock.close()
    sys.exit(0)
    return 'send'



product1='https://www.amazon.in/s?k=iphone+13&rh=n%3A1389432031%2Cp_36%3A1000000-%2Cp_89%3AApple&dc&qid=1636524154&rnid=3837712031&ref=sr_nr_p_89_1'
header={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
'Accept-Language':'en-US,en;q=0.5'
}
response=requests.get(url=product1,headers=header)
webtx=response.text
soup=BeautifulSoup(webtx,'lxml')
price=soup.find_all(class_='a-price-whole')
title=soup.find_all(class_="a-size-medium a-color-base a-text-normal")
z= [{'p_name':i.getText()[:i.getText().index('(')].strip(),
                 'p_memory':i.getText()[i.getText().index('(')+1:i.getText().index(')')].strip(),
                 'p_color':i.getText()[i.getText().index('-')+1:].strip(),
                 'p_price':j.getText().replace(',','').strip()} for i,j in list(zip(title,price))
    ]

#y=json.dumps({dt.now().strftime('%Y-%m-%d %H:%M:%S'):z})
y=json.dumps(z)
print(y)
print(send_data(y))
