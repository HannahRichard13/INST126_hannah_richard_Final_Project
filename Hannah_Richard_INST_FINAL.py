# Hannah Richard Final INST Project

# This program uses an API of makeup data
# It takes user input of a makeup product and a budget that they have for that product.
# This program loops through the API data and if the product matches the users intended product, it adds that product name and its cost to a dictionary
# Then the program loops through the new dictionary
# If the price of the product is within the users budget, it outputs to the user suggested products to buy


# CHECKLIST ITEMS:




# import modules
import requests # imports the API data link
import json # base.package to work with JSON data https://docs.python.org/3/library/json.html

makeup_page = requests.get("http://makeup-api.herokuapp.com/api/v1/products.json") # load the API link
makeup_data = json.loads(makeup_page.content) # load the content

makeup_dict = {} # create an empty dictionary
user_product = input("Which makeup product would you like to search for?\nYour options include: 'Blush', 'Bronzer', 'Eyeline', 'Eyebrow', 'Eyeshadow', 'Foundation', 'Lip Liner', 'Lipstick', 'Mascara', 'Nail Polish'\n").lower() # this will collect user input on their makeup product of choice
user_price = float(input("What is the maximum price you are willing to pay for a makeup product?\nEnter a number:\n")) # collect user input on budget and converts it to a float


for idx in range(len(makeup_data)): # loop through each part of the list of makeup data which is a list of dictionaries
    product_id = makeup_data[idx]["product_type"] # for each dictionary of the list, it will look at the product_type key and set it to the variable product_id
    if product_id == user_product: # checks to see if the product is the same as the users product of choice
        product = str(makeup_data[idx]["name"]) # if the product matches, it collects the name of the product using the name key
        price = str(makeup_data[idx]["price"]) # if the product matches, it collects the price of the product using the price key
        makeup_dict[product] = price # adds the product key with the price value to the dictionary called makeup_dict

for key, values in makeup_dict.items(): # this iterates through the dictionary makeup_dict
    if values == "None": # this accounts for places where no data is entered 
        product_price = 0.0 # if no data is entered for the price, it sets the price to 0
    else:
        product_price = float(values) # if there is a price data point, it converts it into a float
    if product_price < user_price: # if the price is less than the users budget, it will display that item to the user as an optino for them to buy
        if product_price ==0: # if the price = 0, it will tell the user that this price is unknown
            print("The item {} has price N/A, but if you were interested in this cost you can use another source to find its price".format(key))
        else: # output to the user the product and price
            print("The item {}is in your price range and it costs: ${}".format(key, values))



