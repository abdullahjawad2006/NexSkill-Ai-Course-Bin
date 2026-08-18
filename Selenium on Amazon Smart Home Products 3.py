from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv 
import pandas as pd
import time
from selenium.webdriver.support.ui import Select

url="https://www.amazon.com"

cService=webdriver.ChromeService(executable_path='C:\\Users\\Muhammad Abdullah\\Documents\\GitHub\\chromedriver-win64\\chromedriver.exe')

driver = webdriver.Chrome (service=cService)
driver.get(url)
time.sleep(3)

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("smart home gadgets", Keys.ENTER)
sort_by = driver.find_element(By.ID, "s-result-sort-select")
Select(sort_by).select_by_visible_text("Best Sellers")
time.sleep(5)

products = driver.find_elements(By.XPATH,"//div[@class='sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20 gsx-ies-anchor']")

product_name=[]
product_rating=[]
product_sold=[]
product_price=[]

for product in products:

    try:
        name = product.find_element(By.XPATH, ".//h2//span").text
    except:
        name=''
    try:
        rating = product.find_element(By.CSS_SELECTOR, "a[aria-label*='ratings']").get_attribute("aria-label")
    except:
        rating=''
    try:
        sold = product.find_element(By.XPATH, ".//span[@class='a-size-base a-color-secondary']").text
    except:
        sold=''
    try:
        price = product.find_element(By.CSS_SELECTOR, 'span.a-offscreen').get_attribute("textContent"); price = f"${float(price.replace('PKR','').replace(',','').strip())/277.75:.2f}"
    except:
        price=''
    product_name.append(name)
    product_rating.append(rating)
    product_sold.append(sold)
    product_price.append(price)

AmazonSmartHomeGadgets=pd.DataFrame({
    'Product_Name':product_name,
    'Product_Rating':product_rating,
    'Product_Sold':product_sold,
    'Product_Price':product_price
})

AmazonSmartHomeGadgets.to_csv('AmazonSmartHomeGadgets_selenium.csv',index=False)
print("Data Saved")


