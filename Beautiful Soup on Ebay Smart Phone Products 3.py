import requests
from bs4 import BeautifulSoup
import pandas as pd 

with open('Cell Phones & Smartphones _ eBay.html','r',encoding='utf-8') as file:
    soup=BeautifulSoup(file,'html.parser')

products=soup.find_all('div',class_='brwrvr__item-card__wrapper')

product_name=[]
product_company=[]
product_price=[]
product_shipping=[]
product_sold=[]
product_image=[]

for product in products:
    parent=product.find_parent('div')

    try:
        namewhol1=parent.find('div',class_='bsig brw-signal bsig--header bsig--full bsig--multiple-lines')
        namewhol=namewhol1.find('span',class_='bsig__title')
        name=parent.find('h3',class_='textual-display bsig__title__text').get_text(strip=True)
    except:
        name=''
    try:
        company=parent.find('span',class_='textual-display bsig__generic bsig__listingCondition').get_text(strip=True)
    except:
        company=''
    try:
        price_whol=parent.find('div',class_='bsig brw-signal bsig--primary')
        price=price_whol.find('span',class_='textual-display bsig__price bsig__price--displayprice').get_text(strip=True)
    except:
        price=''
    try:
        shipping=parent.find('span',class_='bsig__logisticsCost').get_text(strip=True)
    except:
        shipping=''
    try:
        sold=parent.find('span',class_='textual-display negative').get_text(strip=True)
    except:
        sold=''
    try:
        imgurl=parent.find('img',class_='brwrvr__item-card__image').get('src')
    except:
        imgurl=''
    product_name.append(name)
    product_company.append(company)
    product_price.append(price)
    product_shipping.append(shipping)
    product_sold.append(sold)
    product_image.append(imgurl)

EbaySmartPhoneProducts=pd.DataFrame({
    'Product_Name':product_name,
    'Product_Company':product_company,
    'Product_Price':product_price,
    'Prodcut_Shipping':product_shipping,
    'Product_Sold':product_sold,
    'Product_Image':product_image
})
EbaySmartPhoneProducts.to_csv ('Ebay_Smart_Phone_Products_bs4.csv',index=False)
print("Data Saved")



