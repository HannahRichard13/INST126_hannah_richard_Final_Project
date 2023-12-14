# Hannah Richard Final INST Project

import requests
import re
import json # base.package to work with JSON data https://docs.python.org/3/library/json.html
makeup_page = requests.get("http://makeup-api.herokuapp.com/api/v1/products.json")
makeup_data = json.loads(makeup_page.content)


user_brand = input("Which makeup brand woudl you like to search for?\nYour options include: 'almay', 'alva', 'clinique', 'benefit', 'covergirl', 'e.l.f.', 'essie', 'fenty', 'gossier', iman', 'marcelle', 'maybelline', 'misa', 'mistura', 'revlon', smashbox'\n")
user_product = input("Which make product would you like to search for?\nYour options include: 'Blush', 'Bronzer', 'Eyeline', 'Eyebrow', 'Eyeshadow', 'Foundation', 'Lip Liner', 'Lipstick', 'Mascara', 'Nail Polish'\n")
user_price = float(input("What is the maximum price you are willing to pay for a makeup product?\nEnter a number:\n"))


type(makeup_data)
len(makeup_data)
print(makeup_data[0])


for idx in range(len(makeup_data)):
    brand_id = makeup_data[idx]["brand"]
    print(brand_id)

    

