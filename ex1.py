import requests
from bs4 import BeautifulSoup
import pandas as pd
#pip install bs4
URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

products = soup.find_all('div', class_='thumbnail')

product_names = []
product_prices = []
for product in products:
    name = product.find('a', class_='title').text.strip()
    price = product.find('h4', class_='price').text.strip()

    product_names.append(name)
    product_prices.append(price)

df = pd.DataFrame({
    'Product Name': product_names,
    'Price': product_prices
})

df_cleaned = df.drop_duplicates()

df_cleaned.to_csv("scraped_products.csv", index=False)

print(df_cleaned)
