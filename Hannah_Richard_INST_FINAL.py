# Hannah Richard Final INST 126 Project

# This program uses an API of makeup data
# This program asks the user what their budget is for makeup products.
# This program asks the user if they want to search for a specific product or search through all makeup products.
# If the user wants to search for a specific product, this program takes user input of a makeup product they want to search for and searches for that specific product.
# If the user wants to search for all makeup products within their budget, it sorts through all makeup products in the API.
# This program loops through the API data and if the product matches the users intended product, it adds that product name and its cost to a dictionary.
# Then the program loops through the new dictionary.
# If the price of the product is within the users budget, it outputs to the user suggested products to buy to the users.
# It also saves the suggested products to a file called "makeup_product_list.txt"
# The program reads the file and uses regular expressions to find all the prices in the file and extracts them in the form of a tuple.
# The values of this tuple are saved to variables of 'length' and 'prices'
# Then the program turns the prices that are strings into integers.
# The program then places these values into an empty list and calculates the sum of the list
# Then the program finds the mean (average) price of the makeup products by dividing the sum of the prices by the amount of products.


# CHECKLIST ITEMS:

# Fundamentals:

# In line 129: Checklist item 3.13 satisfied - You used the format() string method or ’f-string’ operator to make output easier to read.
# In lines 74 and 103: Checklist item 5.15 satisfied - You created a dictionary manually.
# In lines 105, 112, and 129 : Checklist item 5.17 satisfied - You accessed the keys of a dictionary.
# In lines and 105 and 112: Checklist item 5.18 satisfied - You iterated through the items of a dictionary to access both keys and values.
# In line 107: Checklist item 5.19 satisfied - You updated values in a dictionary programmatically (i.e., using variables/loops, not manually)
# In line 75: Checklist item 5.12 satisfied - You created a tuple manually.
# In line 145: Checklist item 5.13 satisifed - You assigned tuple members to separate variables in one assignment statement.
# In line 69 and 144: Checklist item 5.14 satisfied - You used a tuple to return multiple values from a function.
# In lines 61: Checklist item 6.3 satisfied - You made appropriate use of a docstring in your function definition.
# In README : Checklist item 6.1 satisfied - You wrote documentation in the form of a README.
# In lines 3-16: Checklist item 6.2 satisfied - You wrote documentation in comments at the top of a script.
# Throughout program: Checklist item 6.5 satisfied - You wrote documentation sufficient to enable someone else to use your script/program.
# In LICENSE.txt: Chechlist item 6.7 satisfied - You chose an appropriate license for your program/script.

# Advanced Topics:

# - Regular Expressions
# In lines 161-162: Checklist item 7.2 satisfied - You used a backslash in a string to ’escape’ a special character.
# In lines 159: Checklist item 7.3 satisfied - You used a ’raw’ string in a string to avoid needing to use backslashes.
# In lines 61-69 and 144: Checklist item 7.4 satisfied - You used a regular expression in order to check that a string matched a certain pattern.
# In lines 142 and 145: Checklist item 7.5 satisfied - You used regular expressions with groupings to extract or change parts of a string.

# - Webscraping and JSON
# In line 71: Checklist item 10.4 satisfied - You used an API to obtain JSON or other formatted data.
# In lines 72 and 88-104: Checklist item 10.5 satisfied - You extracted or manipulated values from JSON formatted data.

# - GIT
# satisfied through program
# Checklist item 9.1 satisfied - You created a git repo.
# Checklist item 9.2 satisfied - You added and committed at least 3 separate commits, with meaningful commit messages.
# Checklist item 9.4 satisfied - You cloned a git repo and committed your own changes.
# Checklist item 9.5 satisfied - You submitted a complete git repo or link to a git repo to submit your work.

# import modules
import requests # imports the API data link
import json # base.package to work with JSON data https://docs.python.org/3/library/json.html
import re # import re module

def find_all(pattern, text): # Checklist item 6.3 satisfied
    """
    uses re.findall() to get a list of occurrences of the pattern in text string. 
    This returns a tuple of: count of matches to string pattern, the list of all matches
    """
    pattern_object = re.compile(pattern) # Checklist item 7.4 satisfied
    search_result = pattern_object.findall(text)
    found = len(search_result)
    return found, search_result #Checklist item 5:14 satisifed 

makeup_page = requests.get("http://makeup-api.herokuapp.com/api/v1/products.json")# Checklist item 10.4 satisfied # load the API link
makeup_data = json.loads(makeup_page.content) # Checklist item 10.5 satisfied # load the content

makeup_dict = {} # Checklist item 5.15 satisfied # create an empty dictionary 
makeup_tuple = ("blush", "bronzer", "eyeliner", "eyebrow", "eyeshadow", "foundation", "lip liner", "lipstick", "mascara", "nail polish") # Checklist item 5.12 satisfied # tuple of all the makeup products in this makeup API
data_counter = 0 # create a variable to count how many products are within budget later in code
price_list = []
print("\nWelcome to the program! This program will help you sort which makeup products you can buy based on your budget.\n")

try:
    user_price = float(input("What is the maximum price you are willing to pay for a makeup product?\nEnter a number:\n$")) # collect user input on budget and converts it to a float
except ValueError:
    user_price = float(input("You did not enter a digit for your budget, please enter your budget in a digit form:\n$")) # if user doesnt enter a number, it will ask them again
user_goal = input("Do you want to look for a specific product or are you looking for all products within a specific budget?: Enter either 'specific' or 'all' ").lower()

# if else statement based on if the user is looking for one product specifically, or all makeup products in general
# Checklist item 10.5 satisfied
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
            makeup_dict[product] = price #Checklist item 5.15 satisfied # adds the product key with the price value to the dictionary called makeup_dict

for key, values in makeup_dict.items(): # Checklist item 5.17 and 5.18 satisfied # this iterates through the dictionary makeup_dict
    if values == "None": # this accounts for places where no data is entered 
        makeup_dict[key]=[0.0] # Checklist item 5.19 satisfied # if no data is entered for the price, it changes the key value to the price 0.0

with open("makeup_product_list.txt", "w") as file:
    file.write("Here is a list of all the products in your budget of $ {}:\n\n".format(user_price)) # tells the user they are about to get a list of makeup products)
print("Here is a list of all the products in your budget of $ {}:\n\n".format(user_price)) # tells the user they are about to get a list of makeup products
for key, values in makeup_dict.items(): # Checklist item 5.17 and 5:18 satisfied # this iterates through the dictionary makeup_dict 
    try: # implemented a try, except because not all data values are floats
        product_price = float(values) # if there is a price data point, it converts it into a float
    except TypeError: # accepts the TypeEror and states there is no data in this box
        print("There is no data here")
        with open("makeup_product_list.txt", "a") as file:
            file.write(str("\nThere is no data here"))
    if product_price < user_price: # if the price is less than the users budget, it will display that item to the user as an optino for them to buy
        data_counter += 1 # if product is in budget, the data counter will increase
        if product_price ==0: # if the price = 0, it will tell the user that this price is unknown
            print("The item {} has price N/A, but if you were interested in this cost you can use another source to find its price".format(key))
            with open("makeup_product_list.txt", "a") as file: # save data to a file 
                file.write(str("\nThe item {} has price N/A, but if you were interested in this cost you can use another source to find its price".format(key)))
        else: # output to the user the product and price
            print("The item {} is in your price range and it costs: ${}".format(key, values))
            with open("makeup_product_list.txt", "a") as file:
                file.write(str("\nThe item {} is in your price range and it costs: ${}".format(key, values))) #Checklist item 3.13 and 5:17 satisfied

if data_counter == 0: # if the data counter has no increase, there are no products available within the budget
    print("\nThere are no products available within this budget\n")
    with open("makeup_product_list.txt", "a") as file: # save data to file
        file.write("\nThere are no products available within this budget\n")
else:
    print("\nThis is the end of the products within your budget\n")
    with open("makeup_product_list.txt", "a") as file: # save data to file
        file.write("\nThis is the end of the products within your budget\n")

with open("makeup_product_list.txt", "r") as file:
    file_contents = file.read() # reads the file and saves it to a variable
pattern1 = r"\$[0-9]+\.[0-9]+" #Checklist item 7.3, 7.4, and 7.5 satisfied

tuple_of_prices = find_all(pattern1, file_contents) # Checklist item 5.14, 7.4, and 7.5 satisfied # returns prices found in pattern in the form of a tuple
length, prices = tuple_of_prices #Checklist item 5.13 satisfied # storing the tuple values to variables

for element in prices: # iterates through the list of prices in the tuple
    price = str(element) # turns the price into a string
    price_value = price[1:] # separates the $ from the number
    price_int_value = int(float(price_value)) # turns the number into an int
    price_list.append(price_int_value) # appends the int into a list

try:
    mean_of_prices = sum(price_list) / length # takes the sum of the list and divides it by number of prices
    print("\nThe average cost of the makeup products are ${} \n ".format(round(mean_of_prices, 2)))  # outputs to user the mean
except ZeroDivisionError: # if there is no data, you cannot divide by zero, so this prevents the error
    print("There is no data available\n")
string_input = input("Would you like to have your file name printed to you using raw string code or regular string code? Enter 'raw' or 'regular' :\n").lower()
if string_input == 'raw': # asks the user if they want the string raw or regular, even though the output is the same (this is more for a grading purposes)
    print(r"If you would like to accces the file name containing your information to add into your file path, copy and paste \makeup_product_list.txt\ ") #Checklist item 7.3 satisfied
else:
    print(""" If you would like to accces the file name containing your information to add into your file path, copy and paste\n\\makeup_product_list.txt\\""") # Checklist item 7.2 satisfied 
