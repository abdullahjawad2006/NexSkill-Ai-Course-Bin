import requests
from bs4 import BeautifulSoup
import pandas as pd

with open('Buy Smart Phones Online at Best Price in Pakistan - Daraz.pk.html','r',encoding='utf-8') as file:
    soup=BeautifulSoup(file,'html.parser')

products = soup.find_all('div',class_='qmXQo')

product_name=[]
product_price=[]
product_priceoff=[]
product_sold=[]
product_reviews=[]

for product in products:
    parent=product.find_parent('div')

    try:
        name=parent.find('div',class_='RfADt').get_text(strip=True).split('-')[0].strip()
    except:
        name=''
    try:
        price_whol=parent.find('div',class_='aBrP0')
        price=price_whol.find('span',class_='ooOxS').text.replace('Rs.','').strip()
    except:
        price=''
    try:
        price_off=parent.find('span',class_='IcOsH').get_text(strip=True)
    except:
        price_off=''
    try:
        product_soldno = parent.find('span', class_='_1cEkb').get_text(strip=True)
    except:
        product_soldno=''
    try:
        reviews = parent.find('span', class_='qzqFw').get_text(strip=True).replace('(', '').replace(')', '')
    except:
        reviews=''
    product_name.append(name)
    product_price.append(price)
    product_priceoff.append(price_off)
    product_sold.append(product_soldno)
    product_reviews.append(reviews)

DarazSmartPhoneProducts=pd.DataFrame({
    'Product_Name':product_name,
    'Product_Price':product_price,
    'Product_PriceOff':product_priceoff,
    'Product_Sold':product_sold,
    'Product_Reviews':product_reviews

})
DarazSmartPhoneProducts.to_csv ('Daraz_Smart_Phone_Products_bs4.csv',index=False)
print("Data Saved")


