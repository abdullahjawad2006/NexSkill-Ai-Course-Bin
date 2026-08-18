from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv 
import pandas as pd
import time
from selenium.webdriver.support.ui import Select

URL="https://www.daraz.pk/catalog/?location=Punjab&page=1&q=smart%20phones&sort=pricedesc"

cService=webdriver.ChromeService(executable_path='C:\\Users\\Muhammad Abdullah\\Documents\\GitHub\\chromedriver-win64\\chromedriver.exe')

driver = webdriver.Chrome (service=cService)
driver.get(URL)
time.sleep(3)

products = driver.find_elements(By.CSS_SELECTOR, '[data-qa-locator="product-item"]')

product_name=[]
product_price=[]

for product in products:
    try:
        name=product.find_element(By.XPATH,".//div[@class='RfADt']").text
    except:
        name=''
    try:
        price=product.find_element(By.XPATH,".//span[@class='ooOxS']").text
    except:
        price=''
    product_name.append(name)
    product_price.append(price)

DarazExpensiveMobiles=pd.DataFrame({
    'Product_Name':product_name,
    'Product_Price':product_price
})
DarazExpensiveMobiles.to_csv('DarazExpensiveMobiles_selenium.csv',index=False)
print("Data Saved")
