from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from urllib.parse import urlsplit, urlunsplit


# ==========================================
# CHROME DRIVER
# ==========================================

cService = webdriver.ChromeService(
    executable_path=r"C:\Users\Muhammad Abdullah\Documents\GitHub\chromedriver-win64\chromedriver.exe"
)

driver = webdriver.Chrome(service=cService)


# ==========================================
# LISTS
# ==========================================

product_name = []
product_price = []
product_reviews = []
product_sold = []
product_link = []


# ==========================================
# PAGE 1 TO 3
# ==========================================

for page in range(1, 4):

    URL = f"https://www.ebay.com/b/Apple-Cell-Phones-Smartphones/9355/bn_319682?_dmd=2&mag=1&rt=nc&_pgn={page}"

    driver.get(URL)

    print("\n==============================")
    print("Scraping Page:", page)
    print("==============================")

    time.sleep(7)


    # ==========================================
    # GET PRODUCTS
    # ==========================================

    products = driver.find_elements(
        By.CSS_SELECTOR,
        "li.brwrvr__item-card"
    )

    print("Cards found:", len(products))


    # ==========================================
    # EACH PRODUCT
    # ==========================================

    for product in products:

        # --------------------------------------
        # PRODUCT NAME
        # --------------------------------------

        try:
            name = product.find_element(
                By.CSS_SELECTOR,
                "h3.bsig__title__text"
            ).text.strip()
        except:
            name = ""


        # Blank cards skip
        if not name:
            continue


        # --------------------------------------
        # PRICE
        # --------------------------------------

        try:
            price = product.find_element(
                By.CSS_SELECTOR,
                "span.bsig__price--displayprice"
            ).get_attribute("textContent").strip()
        except:
            price = ""


        # --------------------------------------
        # REVIEWS
        # --------------------------------------

        try:
            reviews = product.find_element(
                By.CSS_SELECTOR,
                "span.bsig__product-review__count"
            ).text.strip()
        except:
            reviews = ""


        # --------------------------------------
        # SOLD
        # --------------------------------------

        sold = ""

        try:

            hotness = product.find_elements(
                By.CSS_SELECTOR,
                ".bsig__item-hotness .negative"
            )

            for item in hotness:

                text = item.text.strip()

                if "sold" in text.lower():
                    sold = text
                    break

        except:
            sold = ""


        # --------------------------------------
        # LINK
        # --------------------------------------

        try:

            link = product.find_element(
                By.CSS_SELECTOR,
                "a.bsig__title__wrapper"
            ).get_attribute("href")

            # Remove ?epid=... etc.
            parsed_url = urlsplit(link)

            link = urlunsplit((
                parsed_url.scheme,
                parsed_url.netloc,
                parsed_url.path,
                "",
                ""
            ))

        except:
            link = ""


        # --------------------------------------
        # SAVE
        # --------------------------------------

        product_name.append(name)
        product_price.append(price)
        product_reviews.append(reviews)
        product_sold.append(sold)
        product_link.append(link)


        print(name)


# ==========================================
# DATAFRAME
# ==========================================

eBayAppleiPhones = pd.DataFrame({

    "Product_Name": product_name,
    "Product_Price": product_price,
    "Product_Reviews": product_reviews,
    "Product_Sold": product_sold,
    "Product_Link": product_link

})


# ==========================================
# REMOVE DUPLICATES
# ==========================================

eBayAppleiPhones = eBayAppleiPhones.drop_duplicates(
    subset=["Product_Link"]
)


# ==========================================
# SAVE CSV
# ==========================================

eBayAppleiPhones.to_csv(
    "eBayAppleiPhones_selenium.csv",
    index=False,
    encoding="utf-8-sig"
)


print("\n==============================")
print("Data Saved Successfully")
print("==============================")

print("Total Products:", len(eBayAppleiPhones))


# ==========================================
# CLOSE
# ==========================================

driver.quit()

















