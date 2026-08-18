from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv 
import pandas as pd
import time
from selenium.webdriver.support.ui import Select
from urllib.parse import urlsplit, urlunsplit


cService = webdriver.ChromeService(
    executable_path=r"C:\Users\Muhammad Abdullah\Documents\GitHub\chromedriver-win64\chromedriver.exe"
)

driver = webdriver.Chrome(service=cService)

search_keyword = "iphone back cover"

driver.get("https://www.alibaba.com/")

time.sleep(5)

search_box = driver.find_element(
    By.CSS_SELECTOR,
    "textarea.header-tab-input-textarea"
)

search_box.clear()
search_box.send_keys(search_keyword)
search_box.send_keys(Keys.ENTER)

time.sleep(7)

products=driver.find_elements(By.XPATH,"//div[@class='fy26-product-card-wrapper gallery-card pro-search-bg fy26-product-card Q4TFX']")

product_name=[]
product_price=[]
product_minorder=[]
product_sold=[]
product_supplier=[]
product_reviews=[]
product_link=[]

for product in products:
    try:
        name=product.find_element(By.CSS_SELECTOR,"h2.searchx-product-e-title").text
    except:
        name=''
    try:
        price = product.find_element(By.CSS_SELECTOR, "div.searchx-product-price-price-main").get_attribute("textContent").strip()
    except:
        price=''
    try:
        minorder=product.find_element(By.CSS_SELECTOR,'div.searchx-moq').text
    except:
        minorder=''
    try:
        sold=product.find_element(By.CSS_SELECTOR,'div.searchx-sold-order').text
    except:
        sold=''
    try:
        supplier = product.find_element(By.CSS_SELECTOR, "a.searchx-product-e-company").text.strip().rstrip(",")
    except:
        supplier=''
    try:
        reviews=product.find_element(By.CSS_SELECTOR,'span.searchx-product-e-review').text
        reviews = " ".join(reviews.split())
    except:
        reviews=''
    try:
        link = product.find_element(By.CSS_SELECTOR, "a.searchx-product-e-slider__link").get_attribute("href")

        parsed_url = urlsplit(link)

        link = urlunsplit((
            parsed_url.scheme,
            parsed_url.netloc,
            parsed_url.path,
            "",
            ""
        ))
        link = link.strip()
    except:
        link=''
    product_name.append(name)
    product_price.append(price)
    product_minorder.append(minorder)
    product_sold.append(sold)
    product_supplier.append(supplier)
    product_reviews.append(reviews)
    product_link.append(link)

AlibabaiPhoneBackCovers = pd.DataFrame({

    "Product_Name": product_name,
    "Product_Price": product_price,
    "Product_MinOrder": product_minorder,
    "Product_Sold": product_sold,
    "Product_Supplier": product_supplier,
    "Product_Reviews": product_reviews,
    "Product_Link": product_link

})

AlibabaiPhoneBackCovers.to_csv('AlibabaiPhoneBackCovers.csv',index=False,encoding="utf-8-sig")
print("Data Saved")
