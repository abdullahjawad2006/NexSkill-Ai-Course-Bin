import requests 
from bs4 import BeautifulSoup
import pandas as pd

with open('Alibaba.com.html','r',encoding='utf-8') as file:
    soup=BeautifulSoup(file,'html.parser')

products=soup.find_all('div',class_='fy26-product-card-content')

product_name=[]
product_price=[]
product_minimum_order=[]
product_sold=[]
product_company=[]
product_reviews=[]

for product in products:
    parent=product.find_parent('div')

    try:
     name=parent.find('h2',class_='searchx-product-e-title').get_text(strip=True)
    except:
     name=''
    try:
     price=parent.find('div',class_='searchx-product-price-price-main').get_text(strip=True)
    except:
     price=''
    try:
     minimum_order=parent.find('div',class_='searchx-moq').get_text(strip=True)
    except:
     minimum_order=''
    try:
     sold_product=parent.find('div',class_='searchx-sold-order').get_text(strip=True)
    except:
     sold_product=''
    try:
     company=parent.find('a',class_='searchx-product-e-company').get_text(strip=True)
    except:
     company=''
    try:
     reviews=parent.find('span',class_='searchx-product-e-review').get_text(strip=True)
    except:
     reviews=''

    product_name.append(name)
    product_price.append(price)
    product_minimum_order.append(minimum_order)
    product_sold.append(sold_product)
    product_company.append(company)
    product_reviews.append(reviews)

AlibabaAutoAccessoriesProducts=pd.DataFrame({
    'Product_Name':product_name,
    'Product_Price':product_price,
    'Product_Minimum_Order':product_minimum_order,
    'Product_Sold':product_sold,
    'Product_Company':product_company,
    'Product_Reviews':product_reviews
})
AlibabaAutoAccessoriesProducts.to_csv('Alibaba_Auto_Accessories_Products_bs4.csv',index=False)
print("Data Saved")