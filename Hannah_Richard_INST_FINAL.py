# Hannah Richard Final INST Project

# This program uses an API of makeup data
# It takes user input of a makeup product and a budget that they have for that product.
# This program loops through the API data and if the product matches the users intended product, it adds that product name and its cost to a dictionary
# Then the program loops through the new dictionary
# If the price of the product is within the users budget, it outputs to the user suggested products to buy


# CHECKLIST ITEMS:

# In lines 24 and 35: Checklist item 5.15 satisfied - You created a dictionary manually.
# In lines 39 and 52: Checklist item 5.17 satisfied - You accessed the keys of a dictionary.
# In lines 37 and 42: Checklist item 5.18 satisfied - You iterated through the items of a dictionary to access both keys and values.
# In line 39: Checklist item 5.19 satisfied - You updated values in a dictionary programmatically (i.e., using variables/loops, not manually)

# import modules
import requests # imports the API data link
import json # base.package to work with JSON data https://docs.python.org/3/library/json.html

makeup_page = requests.get("http://makeup-api.herokuapp.com/api/v1/products.json") # load the API link
makeup_data = json.loads(makeup_page.content) # load the content

makeup_dict = {} # create an empty dictionary
makeup_tuple = ("blush", "bronzer", "eyeliner", "eyebrow", "eyeshadow", "foundation", "lip liner", "lipstick", "mascara", "nail polish")
data_counter = 0 # create a variable to count how many products are within budget later in code

print("Welcome to the program! This will help you sort which makeup products you can buy based on your budget\n")
user_price = float(input("What is the maximum price you are willing to pay for a makeup product?\nEnter a number:\n")) # collect user input on budget and converts it to a float

user_goal = input("Do you want to look for a specific product or are you looking for all products within a specific budget?: Enter either 'specific' or 'all' ").lower()
if user_goal == "all":
    for element in range(len(makeup_tuple)):
        for idx in range(len(makeup_data)): # loop through each part of the list of makeup data which is a list of dictionaries
            product_id = makeup_data[idx]["product_type"] # for each dictionary of the list, it will look at the product_type key and set it to the variable product_id
            if product_id == makeup_tuple[element]: # checks to see if the product is the same as the users product of choice
                product = str(makeup_data[idx]["name"]) # if the product matches, it collects the name of the product using the name key
                price = str(makeup_data[idx]["price"]) # if the product matches, it collects the price of the product using the price key
                makeup_dict[product] = price # adds the product key with the price value to the dictionary called makeup_dict
else:
    user_product = input("Which makeup product would you like to search for?\nYour options include: 'Blush', 'Bronzer', 'Eyeliner', 'Eyebrow', 'Eyeshadow', 'Foundation', 'Lip Liner', 'Lipstick', 'Mascara', 'Nail Polish'\n").lower() # this will collect user input on their makeup product of choice
    for idx in range(len(makeup_data)): # loop through each part of the list of makeup data which is a list of dictionaries
        product_id = makeup_data[idx]["product_type"] # for each dictionary of the list, it will look at the product_type key and set it to the variable product_id
        if product_id == user_product: # checks to see if the product is the same as the users product of choice
            product = str(makeup_data[idx]["name"]) # if the product matches, it collects the name of the product using the name key
            price = str(makeup_data[idx]["price"]) # if the product matches, it collects the price of the product using the price key
            makeup_dict[product] = price # adds the product key with the price value to the dictionary called makeup_dict

for key, values in makeup_dict.items(): # this iterates through the dictionary makeup_dict
    if values == "None": # this accounts for places where no data is entered 
        makeup_dict[key]=[0.0] # if no data is entered for the price, it changes the key value to the price 0.0

print("Here is a list of all the products in your budget of $ {}:\n\n".format(user_price))
for key, values in makeup_dict.items(): # this iterates through the dictionary makeup_dict
    try: 
        product_price = float(values) # if there is a price data point, it converts it into a float
    except TypeError:
        print("There is no data here")
    if product_price < user_price: # if the price is less than the users budget, it will display that item to the user as an optino for them to buy
        data_counter += 1 # if product is in budget, the data counter will increase
        if product_price ==0: # if the price = 0, it will tell the user that this price is unknown
            print("The item {} has price N/A, but if you were interested in this cost you can use another source to find its price".format(key))
        else: # output to the user the product and price
            print("The item {}is in your price range and it costs: ${}".format(key, values))

if data_counter == 0: # if the data counter has no increase, there are no products available within the budget
    print("\nThere are no products available within this budget")
else:
    print("\nThis is the end of the products within your budget")


