import requests
from bs4 import BeautifulSoup
import pandas as pd

with open('Smart Home Devices & Systems.html','r',encoding='utf-8') as file:
    soup=BeautifulSoup(file,'html.parser')

products=soup.find_all('a',class_='a-color-base a-link-normal ucw-widget-product-card-image-link a-text-normal')

product_price=[]
product_name=[]
product_reviews=[]

for product in products:
    parent=product.find_parent('div')

    try:
        name=parent.find('span',class_='a-truncate-cut').get_text(strip=True).split('-')[0].strip()
    except:
        name=''
    try:
        price_whol=parent.find('span',class_='a-price')
        price=price_whol.find('span',class_='a-offscreen').text.replace('$','').strip()
    except:
        price=''
    try:
        reviews=parent.find('span',class_='a-size-base').get_text(strip=True)
    except:
        reviews=''
    product_price.append(price)
    product_name.append(name)
    product_reviews.append(reviews)

AmazonProducts=pd.DataFrame({
    'Product_Name':product_name,
    'Product_Price':product_price,
    'Product_Reviews':product_reviews
})

AmazonProducts.to_csv ('Amzon_Mobiles2_bs4.csv',index=False)
print("Data Saved")