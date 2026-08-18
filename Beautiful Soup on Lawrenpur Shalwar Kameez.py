import requests
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np
with open("Lawrencepur Men's Shalwar Kameez _ Premium Pakistani Wear Online.html",'r',encoding='utf-8') as file:
    soup=BeautifulSoup(file,'html.parser')

products=soup.find_all('div',class_='t4s-product-info')

cloth_type=[]
shalwarkameez_type=[]
shalwarkameez_price=[]

for product in products:
    parent=product.find_parent('div')

    try:
        ctype=parent.find('div',class_='t4s-product-vendor').get_text(strip=True)
    except:
        ctype=''
    try:
        sktype=parent.find('h3',class_='t4s-product-title').get_text(strip=True)
    except:
        sktype=''
    try:
        skprice=parent.find('span',class_='money').get_text(strip=True)
    except:
        skprice=''
    cloth_type.append(ctype)
    shalwarkameez_type.append(sktype)
    shalwarkameez_price.append(skprice)

LawrencepurMenShalwarKameez=pd.DataFrame({
    'Cloth_Type':cloth_type,
    'ShalwarKameez_Type':shalwarkameez_type,
    'ShalwarKameez_Price':shalwarkameez_price
})
LawrencepurMenShalwarKameez.to_csv('LawrencepurMenShalwarKameez_bs4.csv',index=False)
print("Data Saved")



