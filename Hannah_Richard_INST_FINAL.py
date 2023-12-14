# Hannah Richard Final INST Project

import requests
import re
import json # base.package to work with JSON data https://docs.python.org/3/library/json.html
makeup_page = requests.get("http://makeup-api.herokuapp.com/api/v1/products.json")
makeup_data = json.loads(makeup_page.content)

makeup_dict = {}
user_product = input("Which make product would you like to search for?\nYour options include: 'Blush', 'Bronzer', 'Eyeline', 'Eyebrow', 'Eyeshadow', 'Foundation', 'Lip Liner', 'Lipstick', 'Mascara', 'Nail Polish'\n").lower()
user_price = float(input("What is the maximum price you are willing to pay for a makeup product?\nEnter a number:\n"))

for idx in range(len(makeup_data)):
    product_id = makeup_data[idx]["product_type"]
    if product_id == user_product:
        product = str(makeup_data[idx]["name"])
        price = str(makeup_data[idx]["price"])
        makeup_dict[product] = price


print(makeup_dict)
for key, values in makeup_dict.items():
    if values == "None":
        product_price = 0.0
    else:
        product_price = float(values)
    if product_price < user_price:
        print("The item {}is in your price range and it costs: {}".format(key, values))



