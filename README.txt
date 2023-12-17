README


1. What this program does: 

In this program, it loads an API that is full of makeup data. This program will sort through the API using JSON to download it. 
Once the data is sorted from the API, it will be placed into a dictionary. 
This dictionary will include the makeup product and the price of that product.
All the prices contained in the dictionary will be searched. 
If the prices are less that the users budget, they will be printed out to the user as a suggested product to buy.
This program will give the user an output whcih contains the products a user could buy and how much they cost.
This same output that the user sees will also be saved to a file called "makeup_product_list.txt".
This file will then be searched through regular expressions to find and extract all the prices in the file.
The prices and the number of prices will be outputed in the form of a tuple and the tuple values will be assigned to variable of length and prices.
Then the program will use this data and find the mean value of all the prices.


2. How to use this program: 

The program will first ask the user for their budget through the use of the command line.
The user will enter a digit for their budget.
Then the program will ask the user if they are looking for a specific makeup product or jsut looking for makeup product in general.
If the user wants to search for a specific product, this program takes user input of a makeup product they want to search for and searches for that specific product.
If the user wants to search for all makeup products iwthin their budget, it sorts through all of the makeup products in the API.


