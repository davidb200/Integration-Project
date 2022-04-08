# David Betanzos
# A program that computes different things about GDP and countries
import time
import numpy as np


# Function that will halt the program
def sleep():
    time.sleep(1)


# If a string has double quotes within it, the program may not know when the string ends


greeting_string = """ 
                                                        Greeting
                                                        --------"""
print(greeting_string)
# The \ helps understand what part of the quotation is in the string
print("Hello, welcome to my \"integration project\"")
# Slicing strings
my_name = 'David'
# string functions .upper(), .isalpha(), .capitalize()
# strings that include apostrophes
my_name_capitalized = my_name.upper()
sleep()
print("The first '3' letters of my name are", my_name[0:2])
sleep()
print("The last '2' letters of my name are", my_name[2:5])
sleep()
print("Together that is", my_name_capitalized[0:3] + my_name_capitalized[3:5])
# Get Greeting
# The + operator cocatenates(mooshes) "Hello " with name the user entered
# Will output Hello name of user
name_of_user = input("Enter your name: ")
if name_of_user.isalpha():
    print("Thank you for giving a valid name")
else:
    print(
        "I do not think your name has special characters or numbers, but I will go with it")
# Triple quotes allows a multiline string
sleep()
print("Hello", name_of_user.capitalize(), "welcome to my GDP calculator!")
# User guesses programming language
user_language_guess = input(
    "Guess what higher level programming language I am using? ")
if user_language_guess == "Python" or user_language_guess == "python":
    print("Correct!")
else:
    print(
        "Sorry that was incorrect. I am using Python for my integration project")
# User guess number of countries in the world
sleep()
valid_number_countries = False
while not valid_number_countries:
    try:
        number_of_countries_guess = int(input("Enter how many countries are there:"))
    except ValueError:
        print("I want a number try again")
    else:
        if number_of_countries_guess == 196:
            print("Wow, I did not expect you to get that correct")
        valid_number_countries = True
print("There are actually a total of 196 countries around the world!")
sleep()
print("Each country has a different GDP")
sleep()
# Country user types
country_name = input("Enter a country you want to work with: ")


# Function that countdowns the time the user entered (in secs) to get an answer
# The countdown is set to 3 when computing an answer later on in the program
# When called will output(3 2 1), like a timer
# Will be used later on when doing calculations


def calculate_time():
    countdown = 3
    for timer in range(1, countdown + 1):
        print(countdown, end=" ")
        time.sleep(1)
        countdown -= 1


# Get valid variables old GDP and calculates GDP
# GDP formula = consumption + investment + government purchases(gov_purchases) + net exports
# Net exports = exports - imports
# The numbers in the formula are usually whole numbers
# The + numeric operator adds up the values the user inputted into the formula together
# The - numeric operator subtracts the imports from the exports the user entered (exports - imports)
string_calculating_gdp = """ 
                                                        Calculate GDP
                                                        -------------"""
print(string_calculating_gdp)
valid_variable_gdp = False
while not valid_variable_gdp:
    try:
        consumption = int(
            input("Enter consumption: "))  # consumption user types
        investment = int(input("Enter investment: "))  # investment user types
        gov_purchases = int(
            input("Enter government purchases: "))  # gp user types
        exports = int(input("Enter exports: "))  # exports user types
        imports = int(input("Enter imports: "))  # imports user types
    except ValueError:
        print("That was not a valid whole number try again")
    else:
        net_exports = exports - imports
        gdp = consumption + investment + gov_purchases + net_exports
        print("Calculating GDP...")
        calculate_time()
        # The print(f"{:, }" is another way to print a string that is a number with commas after every 3 numbers
        # Example: print(f"{1000:,}" outputs 1,000 instead of 1000
        print("\nYour GDP value for", country_name, "is $" + f"{gdp:,}")
        valid_variable_gdp = True

# Get valid variables new GDP
string_calculating_new_gdp = """ 
                                                        Calculate New GDP
                                                        -----------------"""
print(string_calculating_new_gdp)
print("Lets see how much a country is growing by if we changed the numbers!")
valid_variable_GDP_two = True
while valid_variable_GDP_two:
    try:
        new_consumption = int(input("Enter new consumption: "))
        new_investment = int(input("Enter new investment: "))
        new_gov_purchases = int(input("Enter new gov purchases: "))
        new_exports = int(input("Enter new exports: "))
        new_imports = int(input("Enter new imports: "))
    except ValueError:
        print("That was not a whole number, try again")
    else:
        new_net_exports = new_exports - new_imports
        new_gdp = new_consumption + new_investment + new_gov_purchases + new_net_exports
        print("Calculating new GDP...")
        calculate_time()
        print("\nYour new GDP value for", country_name,
              "is $" + f"{new_gdp:,}")
        valid_variable_GDP_two = False


# Function that calculates percent change between old and new GDP and whether it grew,declined, or stayed
# the same
# percent change formula = [(new GDP - old GDP) / old GDP ] * 100
# Answer will be a percent to 1 decimal place
# The * numerical operator multiplies two numbers. In the function below it will multiply the
# number stored in the new_minus_old_value_over by 100 to get the percent
# The % is the modulus operator it takes the remainder from division of two numbers 3 % 3 = 0


def calculate_percent_change():
    string_percent_change = """
                                                        Percent change
                                                        --------------"""
    print(string_percent_change)
    if gdp == 0:
        print("I cant do the calculation")
    else:
        new_minus_old_value = new_gdp - gdp
        new_minus_old_value_over_old = new_minus_old_value / gdp
        percent_change = new_minus_old_value_over_old * 100
        print(
        "The program will now calculate the % change between your old and new GDP")
        print("Calculating percent change...")
        calculate_time()
        if percent_change > 0:
            print("\n" + country_name, "has grown by",
                  str(format(percent_change, '.1f')) + "%")
        elif percent_change < 0:
            print("\n" + country_name, "has declined by",
                  str(format(percent_change, '.1f')) + "%")
        elif percent_change == 3 % 3:
            print("\n" + country_name, "has not changed one bit")


def calculate_average_gdp():
    string_average = """ 
                                                            Average
                                                            -------"""
    print(string_average)
    print("GDP can change alot over the years")
    sleep()
    print("We can find the average GDP over X amount of years")
    sleep()
    print("Type your old and new GDP then enter values you find online")
    print("Type zero to get out of the loop")
    valid_gdp_number = False
    while not valid_gdp_number:
        try:
            counter = 0
            total = 0
            gdp_number = int(input("Enter GDP: "))
            while gdp_number != 0:
                total += gdp_number
                counter += 1
                gdp_number = int(input("Enter GDP: "))
        except ValueError:
            print("That was an invalid character. Start over")
        else:
            if gdp_number == 0 and counter == 0:
                print("There is no average GDP because you typed 0 first")
            else:
                print("Calculating average GDP...")
                calculate_time()
                print("\nAverage GDP for", "A", "over", counter,
                      "yrs is $" + format(total / counter, '.2f'))
            valid_gdp_number = True


# Function that calculates GDP per capita given if user wants old or new GDP
# GDP per capita formula = The gdp / population
# The / numeric operator is just division (divides two numbers)


def calculate_gdp_per_capita(population):
    string_gdp_per_capita = """ 
                                                        GDP per capita
                                                        ---------------"""
    print(string_gdp_per_capita)
    user_choice_gdp = input(
        "Would you like to use you old or new GDP (type old or new): ")
    if user_choice_gdp == "old":
        gdp_per_capita = gdp / population
        print("Calculating GDP per capita...")
        calculate_time()
        print("\nGiven your old GDP, GDP per capita is $" + str(
            format(gdp_per_capita, '.2f')))
    elif user_choice_gdp == "new":
        gdp_per_capita_two = new_gdp / population
        print("Calculating GDP per capita...")
        calculate_time()
        print("\nGiven your new GDP, GDP per capita is $" + str(
            format(gdp_per_capita_two, '.2f')))
    else:
        print(
            "I could not do the calculation because you gave me an invalid choice")


def order_country_list_numerically(country_list):
    string_list_of_countries = """ 
                                                            List of countries
                                                            -----------------"""
    print(string_list_of_countries)
    print("Here are the top 3 countries with the highest consumption")
    calculate_time()
    print("--->", country_list[:])
    print("Now here are the top 5 countries with the highest consumption")
    calculate_time()
    country_list.append('France')
    country_list.insert(4, 'UK')
    print("--->", country_list[:])
    print("Now we have", len(country_list), "countries in the list")
    print("Looking at the top 2 we have...")
    calculate_time()
    print("--->", country_list[0:2])
    print("Looking at the last 2 we have...")
    calculate_time()
    print("--->", country_list[3:5])
    print("The US ranks...and the UK ranks...")
    calculate_time()
    print("--->", country_list.index('US') + 1, country_list.index('UK') + 1)


def order_country_list_aplhabetically(country_list):
    string_list_of_countries_alphabetically = """ 
                                            Countries in alphabetical order
                                            -------------------------------"""
    print(string_list_of_countries_alphabetically)
    print(
        "Looking at the countries in alphabetical order we have...")
    calculate_time()
    print("-->", sorted(country_list[:]))
    print("Just for curiosity...")
    letter_input = input('Type a letter and see if its in the list or not ')
    new_country_list = [country for country in country_list if
                        letter_input in country]
    calculate_time()
    print("Here is the revised list having your letter",
          letter_input + "--->", new_country_list[:])
    no_country = [country for country in country_list if letter_input not in
                  country]
    calculate_time()
    print("Here are the countries without your particular letter",
          letter_input, "-->", no_country)
    del new_country_list[:]


# .items() returns the key value pair (ex. [('Year' : 2021)]
# .keys returns the dictionaries key value pairs
# .values shows what is to the right of the keys


def create_dictionary_us():
    string_us_dictionary = """ 
                                                            US dictionary GDP
                                                            -----------------"""
    print(string_us_dictionary)
    us_dict = {"Year": "2021",
               "Consumption": "5000",
               "Investment": "10000",
               "Government Purchases": "20000",
               }
    print("The most important variables affecting US GDP are")
    sleep()
    print(us_dict.keys())
    sleep()
    print("The data is shown below")
    sleep()
    print(us_dict.values())
    sleep()
    print("The whole dictionary for US GDP is shown below")
    sleep()
    print(us_dict.items())


def main():
    calculate_percent_change()
    calculate_average_gdp()
    print("GDP per capita is also a useful tool for measuring GDP")
    valid_population = False
    while not valid_population:
        try:
            population = int(input("Enter the population: "))
        except ValueError:
            print("That was invalid try again")
        else:
            if population == 0 or population < 0:
                print("Sorry, I can't do the calculation")
            else:
                calculate_gdp_per_capita(population)
            valid_population = True
    country_list = ['US', 'China', 'Japan']
    order_country_list_numerically(country_list)
    order_country_list_aplhabetically(country_list)
    create_dictionary_us()


# call to main


main()

# User guesses top 2 countries from a file called country_name.txt
# User has to guess a number and not insert a letter
string_user_guess = """
                                            Read from a file and guess a number  
                                            -----------------------------------"""
print(string_user_guess)
country_names = open('country_names.txt')
print(
    "There is a text file with ten countries randomly sorted with the biggest GDPs")
print("Look at the countries and guess which 2 countries are the highest")
print(
    "Your answer will be a number (Example if I think its the UK first then China I will type 37")
valid_number = False
while not valid_number:
    try:
        user_countries_guess = int(input("Guess which countries are top 2: "))
    except ValueError:
        print("That was not a number")
    else:
        # The ~ bitwise operator is the binary ones complement (basically flipping all the bits)
        # The complement of a negative number is a positive and the other way around then subtract 1
        # ~ -28 would be 27 because -28 flipped is 28 and subtracting 1 = 27
        if (user_countries_guess > 26) and (user_countries_guess == ~-28):
            print("Congratulations! you are right")
        else:
            print("That was a hard question the answer was 27")
        valid_number = True
print("Thanks for trying me out. I hope you learned something about GDP",
      name_of_user)

# Goodbye message
print('goodbye' * 10)  # The * string operator prints goodbye 10 times

# Needed for project
print("The rest is needed as a part of my project")
sleep()
# Arithmetic operators
string_arithmetic_operators = """ 
                                                        Arithmetic operators
                                                        --------------------"""
print(string_arithmetic_operators)
sleep()
print("The ** is the exponent operator. Example: 3 ** 2 =", 3 ** 2)
sleep()
print("The * numerics operator multiply. Example 3 *2 =", 3 * 2)
sleep()
print(
    "The // is floor division it divides two numbers and rounds down to the nearest integer")
sleep()
print("Example: 16//10=", 16 // 10,
      "because this would equal 1.6 if you divided, but will round down to 1")
time.sleep(2)
# Shortcut operators
string_shortcut_operators = """ 
                                                        Shortcut Operators
                                                        ------------------"""
print(string_shortcut_operators)
print(
"The next program will show the highest power 2 can be to so it less than 500")
number = 2
power_counter = 1
while number < 500:
    number *= 2
    power_counter += 1
print("2 can raised to the", power_counter - 1, "and still be less than 500")
# Optional Sprint for project
# Simple lists
string_simple_lists = """ 
                                                        Simple lists
                                                        ------------"""
print(string_simple_lists)
# Constructing vectors
print("Vectors can be outputted horizontally or vertically")
horizontal_vector = np.array(['x', 'y', 'z'])  # outputs a horizontal array
column_vector = np.array([['x'], ['y'], ['z']])  # outputs a column array
print("Here is an example of a horizontal vector:", horizontal_vector)
print("Here is an example of a vectors displayed vertically", column_vector)
# Lists in detail
string_lists_in_detail = """ 
                                                        Lists in detail
                                                        ---------------"""
print(string_lists_in_detail)
# copying
numbers_list = [1, 2, 3, 4, 5]
new_number_list = numbers_list.copy()
print(new_number_list)  # .copy just returns the original list (not modified)
# Iterating lists with a for loop
letters_list = ['a', 'b', 'c']
sleep()
for count in range(
        len(letters_list)):  # prints the elements in the list horizontally without brackets
    print(letters_list[count], end=" ")
    # Will output a b c
# Initializing lists
random_list = ['Hello'] * 10  # multiplication is a way to initialize a list
print(random_list)
# Lists in lists (matrices and cubes)
lists_in_lists_string = """ 
                                                        Lists in lists (matrices and cubes)
                                                        -----------------------------------"""
print("This program will display a 3 by 3 matrix")
matrix = [[1, 2, 3],  # 3 by 3 matrix
          [4, 5, 6],
          [6, 7, 8]]
for index in range(0, 3):
    print(matrix[index])  # will print the matrix
print("The element on row 1 column 1 is", matrix[0][
    0])  # getting one element from matrix, rows & columns start at 0
# Data structures
string_data_structures_bitwise_operators = """ 
                                                    Data Structures (bitwise operators)
                                                    >> << & ^ |
                                                    -----------------------------------"""
print(string_data_structures_bitwise_operators)
# Optional sprint for project
sleep()
print("Lets use 20 and 21 for all these examples")
sleep()
print("20 in binary is",
      bin(20))  # bin() turns an integer into a binary number
sleep()
print("21 in binary is", bin(21))
sleep()
print("Looking at 20 and 21 in binary vertically...")


def get_binary_number_twenty():
    for digits_twenty in bin(20):
        print(digits_twenty, end=" ")


def get_binary_number_twenty_one():
    seperate_numbers = """    """
    print(seperate_numbers)
    for digits_twenty_one in bin(21):
        print(digits_twenty_one, end=" ")


def calculate_and_bitwise_operator():
    print(
        "The & is the and bitwise operator. It copies a bit if exists in both operands")
    print("The ones that are not similar will be changed to zeros")
    get_binary_number_twenty()
    get_binary_number_twenty_one()
    print("""\n--------------""")
    for digits in bin(20 & 21):
        print(digits, end=" ")
    print(
        "\n20 and 21 in binary share 1 0 1 0 going from left to right if you compare the numbers vertically")
    sleep()
    print("Converting", bin(20 & 21), "into decimal we get", 20 & 21)


calculate_and_bitwise_operator()


def calculate_xor():
    sleep()
    print(
        "The ^ is the XOR operator it copies a bit if it is in only one operand but not both")
    sleep()
    print("If the bit exists in both operand it will return", 0)
    sleep()
    get_binary_number_twenty()
    get_binary_number_twenty_one()
    print("\n-------------")
    sleep()
    print("0 b 0 0 0 0 1")
    sleep()
    print("Python translates this value to...")
    sleep()
    for digits in bin(20 ^ 21):
        print(digits, end=" ")
    print("\nConverting to a decimal we get", 20 ^ 21)


calculate_xor()
sleep()
print(
    "| is the bitwise or operator, if one or both bits are 1 output is (1 | 0),(0|1)",
    1 | 0)
print("Else if both bits are zero (0 | 0) it will equal", 0 | 0)
sleep()


def calculate_right_shift_bitwise_operator():
    print("The >> is the binary right shift bitwise operator.")
    print(
        "This bitwise operator Shifts the number in binary to the right by whatever you tell it")
    print("Lets calculate 20 >> 1")
    for digits_twenty in bin(20):
        print(digits_twenty, end=" ")
    print("\n-------------")
    for arrow_right_answer in bin(20 >> 1):
        print(arrow_right_answer, end=" ")
    print("\nConverting it to decimal equals", 20 >> 1)


calculate_right_shift_bitwise_operator()
sleep()


def calculate_left_shift_bitwise_operator():
    print("The << is the binary shift left bitwise operator")
    sleep()
    print("It shifts the number in binary to the left by whatever you tell it")
    print("Lets calculate 20 << 1")
    for digits_twenty in bin(20):
        print(digits_twenty, end=" ")
    print("\n---------------")
    for left_arrow_answer in bin(20 << 1):
        print(left_arrow_answer, end=" ")
    print("\nConverting it to decimal equals", 20 << 1)


sleep()
calculate_left_shift_bitwise_operator()
string_tuples = """ 
                                                    Tuples/ Tuples vs. Lists
                                                    ------------------------"""
print(string_tuples)
# Tuples/ Tuples vs lists
print(
    "Tuples are another way to store data like lists, however a tuple cannot be changed (immutable)")
sleep()
print("A list can change")
sleep()
print("You can reassign tuples if you want to modify it")
sleep()
print(
    "Instead of brackets the elements in the set are surrounded by parenthesis")
tuple_numbers = (1, 2, 3, 4)
sleep()
print("All the numbers in this tuple are", tuple_numbers[:])
sleep()
print("Indexing the last value in the tuple will output", tuple_numbers[-1])
tuple_numbers = (2, 3, 4, 5)  # Tuples can be reassigned
sleep()
print("I changed the original tuple a bit so now it outputs", tuple_numbers)
# Lists within tuples
list_in_tuple = (1, 2, 3, [4, 5])
sleep()
print("We can change things that are mutable (like lists) inside a tuple")
list_in_tuple[3][0] = 10
sleep()
print(list_in_tuple)
sleep()
# Tuples within lists
list_letters = ['a', 'b', 'c', ('d', 'e')]
print(list_letters)
print(
    "I cannot change the assigned values in the tuple above unless a reassigned it like so")
sleep()
print("['a','b', 'c', ('f','g')]")
sleep()
list_letters = ['a', 'b', 'c', ('f', 'g')]
print(list_letters)
string_dictionaries = """ 
                                                    Dictionaries
  
                                                    ------------"""
print(string_dictionaries)
sleep()
print("Here is a dictionary for a meal")
meal = {'Food': 'Pizza', 'Drink': 'Water', 'complements': 'Breadsticks'}
print(meal)
meal['desert'] = 'Chocolate cake'  # Adds key to the dictionary meal
print(meal)
meal.pop('complements')  # Removes the key appetizer and outputs breadsticks
# Indexes the key to find the value associated (Pizza)
search_key = 'Food'
answer = list(meal.keys()).index(search_key)
print("Value index that correlates with pizza is", answer)
iterate_meal_dictionary = meal.__iter__()  # Iterates through a dictionary
print(iterate_meal_dictionary)
for key in meal.keys():  # Iterating through keys
    print(key)
for value in meal.values():  # Iterating though values
    print(value)
# Checking key existence
find_key = 'Food'
if find_key in meal:
    print("Key exists")
else:
    print(find_key, "does not exist")
