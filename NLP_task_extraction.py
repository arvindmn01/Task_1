import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
url=requests.get('https://www.pathologyoutlines.com/')

soup=BeautifulSoup(url.content,'html.parser')

s=soup.find(class_='home_content clearfix')
links=s.find_all('a')
dic={}
f_lis=[]

for i in links:
    link=i['href']
    url1=requests.get(link)
    soup1=BeautifulSoup(url1.content,'html.parser')
    all_d=soup1.find(class_='page_content')
    a_=all_d.find_all('a')
    lis=[]
    for j in a_:
        lis.append(j.text)
    dic[i.text]=lis
    f_lis.append([i.text,lis])


with open('key_values.json','w') as f:
    json.dump(dic,f)

df=pd.DataFrame(f_lis,columns=['Keys','Values'])
df.to_excel('key_values.xlsx',index=None)

