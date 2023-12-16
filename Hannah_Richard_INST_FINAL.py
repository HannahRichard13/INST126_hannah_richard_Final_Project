# Hannah Richard Final INST Project

# This program uses an API of makeup data
# It takes user input of a makeup product and a budget that they have for that product.
# This program loops through the API data and if the product matches the users intended product, it adds that product name and its cost to a dictionary
# Then the program loops through the new dictionary
# If the price of the product is within the users budget, it outputs to the user suggested products to buy


# CHECKLIST ITEMS:

# Fundamentals:
# In lines and : Checklist item 5.15 satisfied - You created a dictionary manually.
# In lines and : Checklist item 5.17 satisfied - You accessed the keys of a dictionary.
# In lines and : Checklist item 5.18 satisfied - You iterated through the items of a dictionary to access both keys and values.
# In line : Checklist item 5.19 satisfied - You updated values in a dictionary programmatically (i.e., using variables/loops, not manually)
# In line : Checklist item 5.12 satisfied - You created a tuple manually.
# In line : Checklist item 5.13 satisifed - You assigned tuple members to separate variables in one assignment statement.
# **** In line : Checklist item 5.14 satisfied - You used a tuple to return multiple values from a function.
# In lines : Checklist item 6.1 satisfied - You wrote documentation in the form of a README.
# In lines : Checklist item 6.2 satisfied - You wrote documentation in comments at the top of a script.
# In lines : Checklist item 6.5 satisfied - You wrote documentation sufficient to enable someone else to use your script/program.
# In lines : Chechlist item 6.7 satisfied - You chose an appropriate license for your program/script.

# Advanced Topics:
# - Regular Expressions
# Checklist item 7.5 satisfied - You used regular expressions with groupings to extract or change parts of a string.
# - Webscraping and JSON
# Checklist item 10.4 satisfied - You used an API to obtain JSON or other formatted data.
# Checklist item 10.5 satisfied - You extracted or manipulated values from JSON formatted data.
# - GIT
# Checklist item 9.1 satisfied - You created a git repo.
# Checklist item 9.2 satisfied - You added and committed at least 3 separate commits, with meaningful commit messages.
# Checklist item 9.4 satisfied - You cloned a git repo and committed your own changes.
# Checklist item 9.5 satisfied - You submitted a complete git repo or link to a git repo to submit your work.


# import modules
import requests # imports the API data link
import json # base.package to work with JSON data https://docs.python.org/3/library/json.html
import re # import re module

makeup_page = requests.get("http://makeup-api.herokuapp.com/api/v1/products.json") # load the API link
makeup_data = json.loads(makeup_page.content) # load the content

makeup_dict = {} # create an empty dictionary
makeup_tuple = ("blush", "bronzer", "eyeliner", "eyebrow", "eyeshadow", "foundation", "lip liner", "lipstick", "mascara", "nail polish") # tuple of all the makeup products in this makeup API
data_counter = 0 # create a variable to count how many products are within budget later in code

print("\nWelcome to the program! This program will help you sort which makeup products you can buy based on your budget.\n")

user_price = float(input("What is the maximum price you are willing to pay for a makeup product?\nEnter a number:\n$")) # collect user input on budget and converts it to a float
user_goal = input("Do you want to look for a specific product or are you looking for all products within a specific budget?: Enter either 'specific' or 'all' ").lower()


# if else statement based on if the user is looking for one product specifically, or all makeup products in general
if user_goal == "all": # if the user is looking for makeup product in general
    for element in range(len(makeup_tuple)): # this loops through the elements of the tuple makeup_tuple
        for idx in range(len(makeup_data)): # loops through each part of the list of makeup data which is a list made up of dictionaries
            product_id = makeup_data[idx]["product_type"] # for each dictionary of the list, it will look at the product_type key and set it to the variable product_id
            if product_id == makeup_tuple[element]: # checks to see if the product is the same as the element of the tuple
                product = str(makeup_data[idx]["name"]) # if the product matches, it collects the name of the product using the name key
                price = str(makeup_data[idx]["price"]) # if the product matches, it collects the price of the product using the price key
                makeup_dict[product] = price # adds the product key with the price value to the dictionary called makeup_dict
else: # if the user is looking for a specific makeup product
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

with open("makeup_product_list.txt", "w") as file:
    file.write("Here is a list of all the products in your budget of $ {}:\n\n".format(user_price)) # tells the user they are about to get a list of makeup products)
print("Here is a list of all the products in your budget of $ {}:\n\n".format(user_price)) # tells the user they are about to get a list of makeup products
for key, values in makeup_dict.items(): # this iterates through the dictionary makeup_dict
    try: # implemented a try, except because not all data values are floats
        product_price = float(values) # if there is a price data point, it converts it into a float
    except TypeError: # accepts the TypeEror and states there is no data in this box
        print("There is no data here")
        with open("makeup_product_list.txt", "a") as file:
            file.write("\nThere is no data here")
    if product_price < user_price: # if the price is less than the users budget, it will display that item to the user as an optino for them to buy
        data_counter += 1 # if product is in budget, the data counter will increase
        if product_price ==0: # if the price = 0, it will tell the user that this price is unknown
            print("The item {} has price N/A, but if you were interested in this cost you can use another source to find its price".format(key))
            with open("makeup_product_list.txt", "a") as file:
                file.write("\nThe item {} has price N/A, but if you were interested in this cost you can use another source to find its price".format(key))
        else: # output to the user the product and price
            print("The item {} is in your price range and it costs: ${}".format(key, values))
            with open("makeup_product_list.txt", "a") as file:
                file.write("\nThe item {} is in your price range and it costs: ${}".format(key, values))

if data_counter == 0: # if the data counter has no increase, there are no products available within the budget
    print("\nThere are no products available within this budget\n")
    with open("makeup_product_list.txt", "a") as file:
        file.write("\nThere are no products available within this budget\n")
else:
    print("\nThis is the end of the products within your budget\n")
    with open("makeup_product_list.txt", "a") as file:
        file.write("\nThis is the end of the products within your budget\n")


