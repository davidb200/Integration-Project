"""Integration project (GDP calculator)"""
__author__ = "David Betanzos"
# David Betanzos
# A program that computes different things about GDP and countries GDP
import time
import numpy as np


def sleep():
    """Function that halts the flow of the program"""
    time.sleep(1)


def calculate_time():
    """Countdowns the time the user entered (in secs) to get an answer
    later on in the program. When called will output 3,2,1 like a timer
    .It is used later on when doing calculations"""
    countdown = 3
    for timer in range(1, countdown + 1):  # From 1 to 3
        print(countdown, end=" ")  # prints starting from 3 to 1 on the same
        # line
        time.sleep(1)  # Countdowns a second between each decrement
        countdown -= 1  # decrements the value by 1 until countdown = 1


def introduce_myself():
    """Introduces the name of the person who made the project in a unique
    way with strings."""
    # If a string has double quotes within it, the program may not know when
    # the string ends. The \' \' helps understand what part of the quotation
    # is in the string
    # The """ """ allows for a multiline string(Used for headings)
    greeting_string = """ 
                                                        Introduction
                                                        ------------"""
    print(greeting_string)
    print("Hello, welcome to my \"integration project\"")
    my_name = 'David'
    my_name_capitalized = my_name.upper()
    sleep()
    print("The first '3' letters of my name are", my_name[0:2])
    sleep()
    print("The last '2' letters of my name are", my_name[2:5])
    sleep()
    print("Together is", my_name_capitalized[0:3] + my_name_capitalized[3:5])


def get_greeting():
    """Asks the user to give a name and introduces them to the main part
    of my project. """
    greeting_string = """  
                                                         Greeting
                                                         --------"""
    print(greeting_string)
    name_of_user = input("Type your name then hit \'Enter\': ")
    if name_of_user.isalpha():  # Checks that the user typed only letters
        print("Hello " + name_of_user.capitalize())
        print("Welcome to my GDP calculator!")  # The + operator cocatenates
        # "Hello " with name the user entered. Will output Hello name of user
        # if the user types in all letters
    else:
        print(
         "I do not think your name has special characters or numbers")
        print("But I will still go with it")
        sleep()
        print("Hello,", name_of_user)
        print('Welcome to my GDP calculator!')


def get_user_guess_language():
    """User guesses what language I made my Integration Project in and tells
    them if they are right or wrong"""
    user_language_guess = input(
     "Guess the programming language I used, then hit \'Enter\': ")
    if user_language_guess.upper() == 'PYTHON' or user_language_guess == "me":
        print("Correct!")
    else:
        print("Incorrect, I am using Python for my Integration Project.")


def get_user_guess_number_of_countries():
    """User guesses the number of countries in the world and congratulates
    them if they got it right"""
    string_number_of_countries = """
                                            User Guesses number of countries
                                             ------------------------------
                                        """
    print(string_number_of_countries)
    print("You are going to guess how many countries there are in the world")
    print("Your answer should be a positive whole number")
    print(
     'If you type a float/special characters/letter(s) the program will say:')
    print(
        '---\'I Want a whole number try again\' until you give a whole number')
    print("If you type a whole number and get the answer wrong it will say:")
    print("The actual number of countries there are in the world")
    # Valid input validation for number of countries
    valid_number_countries = False
    while not valid_number_countries:
        try:
            number_of_countries_guess = int(input(
             "Type how many countries are there then hit \'Enter\': "))
        except ValueError:
            print("I want a whole number try again")
        else:
            valid_number_countries = True
            if number_of_countries_guess == 196:
                print("Wow, I did not expect you to get that correct!")
            print("There are a total of 196 countries around the world!")
            print("Each country has a different GDP")


def calculate_percent_change(gdp, new_gdp, country_name):
    """Calculates percent change between new and old GDP and whether
    it grew / declined or stayed the same. Percent change formula =
    [(new GDP - old GDP) / old GDP ] * 100. The answer will be a percent
    to 1 decimal place.
    Parameters:
    gdp (old gdp), new_gdp - Used in the % change formula
    country_name - The user can see how much their country that they typed
    grew or declined"""
    string_percent_change = """
                                                        Percent change
                                                        --------------"""
    print(string_percent_change)
    print(
     "I will now calculate the percent change between the old and new GDP")
    print(
     "% change allows to see how much", country_name, "is growing/declining")
    sleep()
    print("This is the formula I am using: ")
    print('Percent change formula = [new_gdp - old_gdp / old_gdp] * 100 ')
    print("The % change answer will be to 1 decimal place")
    sleep()
    print('If the % change is - then the program will say: ')
    print(
     '---', country_name, 'declined by X percent where X is the % change')
    sleep()
    print('If the % change is + then the program will say: ')
    print(
     '---', country_name, 'grew by X percent where X is the % change')
    sleep()
    print('If', country_name, ' GDP did not grow or decline (stayed the same)')
    print('In other words, the % change = \'0\' the program will say: ')
    print('---', country_name, "has not changed one bit")
    sleep()
    print(
     'If for some reason the value for the old GDP summed up to \"0\"')
    print('The program will say: ')
    print("---\"I can't do the calculation\")")
    print("---\"I can't divide by \"0\"")
    sleep()
    if gdp == 0:
        print("I can't do the calculation")
        print("I can't divide by \"0\"")
    else:
        new_minus_old_value = new_gdp - gdp
        new_minus_old_value_over_old = new_minus_old_value / gdp
        percent_change = new_minus_old_value_over_old * 100
        # The * numeric operator numerical operator multiplies two numbers.
        # Below it will multiply the number stored in
        # the new_minus_old_value_over_old by 100 to get the percent
        print("Calculating percent change...")
        calculate_time()
        if percent_change > 0:
            print("\n" + country_name, "has grown by",
                  str(format(percent_change, '.1f')) + "%")
        elif percent_change < 0:
            print("\n" + country_name, "has declined by",
                  str(format(percent_change, '.1f')) + "%")
        elif percent_change == 3 % 3:  # The % is the modulo operator which
            #  takes the remainder from division (3 % 3 = 0)
            print("\n" + country_name, "has not changed one bit")


def get_population(gdp, new_gdp):
    """Tries to get a valid population from the user and uses it to calculate
    GDP per capita (may or may not be called)
    Parameters:
    gdp, new gdp - If the population the user enters is valid,
    then the last else block which calculates gdp per capita will be called
    and will require gdp and new gdp"""
    string_get_population = """
                                                         Get population
                                                         ---------------"""
    print(string_get_population)
    print("GDP per capita is also a useful tool for measuring GDP")
    print("The formula for GDP per capita = GDP / population")
    print("In order for me to calculate GDP per capita you should")
    print("enter a positive whole number fot the population")
    sleep()
    print("If you type in a float/letter(s)/special character(s) it will say:")
    print("---\"That was invalid type a whole number\"")
    print("--- You try again")
    sleep()
    print("If you type in \"0\" or a - whole number, the program will say: ")
    print("---\"Sorry I can't do the calculation\"")
    print("---\"You may have typed in '0'\"")
    print("---\"I cannot divide by '0'\"")
    sleep()
    print("---\"You may have typed a - number\"")
    print('---\"The population cannot be a negative number\"')
    print('--- \"The program wont calculate GDP per capita\"')
    print('--- It will just move on to the next thing')
    sleep()
    print("If you type a positive whole number the program will then ask: ")
    print(
     "---\"Would you like to use your old or new GDP? (type 'old' or 'new')\"")
    print("---If you do not type \"old\" or \"new\", it will: ")
    print(
     "------Not do the calc. for GDP per capita and move on to the next thing")
    print("---If you type in \"old\" or \"new\" it will:")
    print("-----Calculate GDP per capita based off your new or old GDP answer")
    # While loop that checks for a valid population from user
    valid_population = False
    while not valid_population:
        try:
            population = int(
             input("Enter a positive whole number for the population:"))
        except ValueError:
            print("That was invalid. Type a whole number")
        else:
            valid_population = True
            if population == 0 or population < 0:  # If the user enters a '0'
                # or a - number, it will print what is below
                print("Sorry, I can't do the calculation")
                sleep()
                print("You may have typed in '0'")
                print("I cannot divide by '0'")
                sleep()
                print("You may have typed a - number")
                print('The population cannot be a - number')
            else:  # If the user enters a positive whole number then calculate
                # _gdp_per_capita function will get executed
                calculate_gdp_per_capita(population, gdp, new_gdp)


def calculate_gdp_per_capita(population, gdp, new_gdp):
    """Calculates GDP per capita given if the user wants old or new GDP from
    the number the user entered for the population. GDP
    per capita forumla =  The GDP / population. Not all parameters will be used
    but below shows their role:
    Parameters:
    population - If the user does not enter a valid population from the get_
    population function, then this function won't be called. Else, it
    is going to use that population to divide based off whether the suer wants
    to use their old or new GDP.
    gdp - If the user wants to user their old_gdp(gdp), then it will calculate
    GDP per capita based off the value stored in gdp
    new_gdp - If the user wants to user their new gdp, then it will calculate
    GDP per capita based off the value stored in gdp
    """
    string_gdp_per_capita = """ 
                                                        GDP per capita
                                                        ---------------"""
    print(string_gdp_per_capita)
    user_choice_gdp = input(
     "You want your old or new GDP?(type 'old' or 'new') then hit \'Enter\':")
    if user_choice_gdp == "old":
        gdp_per_capita = gdp / population  # The / arithmetic operator divides
        # two numbers. In this case the gdp / population.
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
        print("I could not do the calculation")
        print("You did not type either \'old\' or \'new\'")


def calculate_average_gdp(country_name):
    """A while loop that calculates average GDP from a list of valid
    inputs the user enters
    Parameters:
    Country_name - Shows the user the average GDP for the country they
    typed in"""
    string_average = """ 
                                                            Average
                                                            -------"""
    print(string_average)
    print("GDP can change alot over the years")
    sleep()
    print("We can find the average GDP over X amount of years")
    sleep()
    print("For every prompt, you enter a whole number")
    print(
     'If you type a float/letter(s)/special character(s), program will say: ')
    print('---\"That was not a whole number \" and it will prompt again')
    sleep()
    print('Every new whole number you enter will be considered 1 year')
    sleep()
    print("Program will keep prompting for a whole number(GDP)")
    print("until you type \"0\" then hit \'Enter\' for one of the prompts")
    print(
     "From there, I will calc the average GDP based off the numbers you put")
    print("If you enter \"0\" for the 1st prompt, then the program will say: ")
    print("---There is no Average GDP because you typed \"0\" in first")
    sleep()
    print(
     'Ex:If you enter at least 1 valid number for a prompt then \"0\" in the')
    print('next prompt program will say:')
    print(
     '---Average GDP for', country_name, 'over 1 years is whatever you typed')
    sleep()
    print(
     'Ex:If you enter in 2 valid numbers for the 2 prompts then \"0\"')
    print("It will say: ")
    print('---Average GDP for', country_name, 'over 2 years is whatever the')
    print('--- average of the two numbers are')
    sleep()
    print("Enter your old and new GDP, then enter numbers you find online!")
    valid_gdp_number = False
    while not valid_gdp_number:
        try:
            counter = 0
            total = 0
            gdp_number = int(input(
             "Type a whole number (GDP) then hit \'Enter\': "))
            while gdp_number != 0:
                total += gdp_number  # Adds number user entered in gdp_number
                # to the total
                counter += 1  # Adds 1 to every time user types a number
                gdp_number = int(input(
                 "Type a whole number (GDP) then hit\'Enter\': "))
        except ValueError:
            print("That was not a whole number. Try again")
        else:
            if gdp_number == 0 and counter == 0:  # If user types 0, the loop
                # will stop running
                print("There is no average GDP because you typed 0 first")
            else:  # If the user gives at least 1 valid number
                print("Calculating average GDP...")
                calculate_time()
                print("\nAverage GDP for", country_name, "over", counter,
                      "yrs is $" + format(total / counter, '.2f'))
            valid_gdp_number = True


def order_country_list_numerically(country_list):
    """Modifies and orders a list of countries from the function main in
    numerical order based off GDP.
    Parameters:
    country_list - function will add things to the list of 3 countries in main
    """
    string_list_of_countries = """ 
                                       List of countries based off Consumption 
                                       -------------------------------------"""
    print(string_list_of_countries)
    print("Lets look at actual countries now")
    print("Remember consumption was a number used when calculating GDP!")
    sleep()
    print("Here are the top 3 countries with the highest consumption")
    calculate_time()
    print("--->", country_list[:])  # Indexes through the whole list in the
    # from the parameter country_list
    print("Now here are the top 5 countries with the highest consumption")
    calculate_time()
    country_list.append('France')  # Adds 'France' to the list
    country_list.insert(4, 'UK')  # Inserts the UK into the 4th index in the
    # list
    print("--->", country_list[:])
    print("Now we have", len(country_list), "countries in the list")
    # The len function shows the number of indexes in the list
    print("Looking at the top 2 we have...")
    calculate_time()
    print("--->", country_list[0:2])  # Slices through the list to output index
    # 0 and 1
    print("Looking at the last 2 we have...")
    calculate_time()
    print("--->", country_list[3:5])  # Slices through the list to output index
    # 3 and 4
    print("The US ranks...and the UK ranks...")
    calculate_time()
    print("--->", country_list.index('US') + 1, country_list.index('UK') + 1)
    # Adds 1 to the number index associated with US and UK


def order_country_list_alphabetically(country_list):
    """Orders the list of countries in alphabetical order and then checks
    to see if a letter the user inputted is in the list of countries
    Parameters:
    country_list - The country list in main shows 3 countries. This function
    will add some things to the original country list in main"""
    string_list_of_countries_alphabetically = """ 
                                               Countries in alphabetical order
                                               ---------------------------"""
    print(string_list_of_countries_alphabetically)
    print("Looking at the same countries in alphabetical order we have...")
    calculate_time()
    print("-->", sorted(country_list[:]))  # Sorts the list alphabetically
    print("Just for curiosity...")
    print(
     "Below you will type a letter and see if its in the list of 5 countries")
    sleep()
    print("Letters are case sensitive")
    print("If you type a letter: ")
    print("---It will only output the countries with that capital letter")
    print(
     "---It will not output the countries with the same letter lowercase")
    sleep()
    print(
     '--Ex: If you type \"C\", it will show countries with the letter \"C\"'
    )
    print("---It will not output countries with the letter \'c\'")
    print(
     "---Then, it will show the countries without that letter ")
    sleep()
    print("If you type any special characters/numbers then the program will: ")
    print("---Show a blank list([])")
    print("---Then show a list of all the countries")
    letter_input = input(
     'Type a letter to see if its in the list or not then hit \'Enter\': ')
    # List comprehension that checks if a letter is in the country list
    new_country_list = [country for country in country_list if
                        letter_input in country]
    calculate_time()
    print("Here is the revised list having your letter",
          letter_input + "--->", new_country_list[:])
    # List comprehension that checks if a letter is NOT in the country list
    no_country = [country for country in country_list if letter_input not in
                  country]
    calculate_time()
    print("Here are the countries without your particular letter",
          letter_input, "-->", no_country)
    del new_country_list[:]  # deletes the country list


def read_and_guess_from_file():
    """User reads from a file called country_names.txt and guesses a number"""
    string_user_guess = """
                                          Read from a file and guess a number  
                                          ---------------------------------"""
    print(string_user_guess)
    country_names = open('country_names.txt')
    print("There is a text file with ten countries randomly sorted")
    print("Here is the text file below: ")
    for countries in country_names:  # Prints all the country names from a
        # file called country_names.txt
        print(countries.strip())
    print('-------------')
    sleep()
    print(
     'Look at the countries above'
    )
    print("Guess which 2 countries have the highest GDP")
    print("Your answer should be a positive whole number")
    sleep()
    print("Ex:If I think its the UK 1st then US 2nd I will type 75")
    print("Another Ex: If I think its Italy 1st then Canada, I type 12")
    print("If you type a special character(s)/float/ letter(s) it will say:")
    print("---\"I want a whole number. Try again.\"")
    # Checks for a valid humber the user enters
    valid_number = False
    while not valid_number:
        try:
            user_countries_guess = int(input("Which countries are top 2: "))
        except ValueError:
            print("I want a whole number. Try again.")
        else:
            valid_number = True
            if (user_countries_guess > 26) and (user_countries_guess == ~-28):
                # The ~ bitwise operator flips the number and adds 1 (~-28 =27)
                print("Congratulations! you are right")
            else:
                print("That was a hard question the answer was 27")
            country_names.close()


def get_goodbye():
    """Says goodbye to the user and is the last function in the program. The
    * string operator prints 'goodbye' 10 times"""
    print("""
                                                            Goodbye Message
                                                            ---------------""")
    print("Thanks for trying me out. I hope you learned something about GDP")
    print('goodbye' * 10)  # The * string operator prints goodbye 10 times
# Needed for project


def get_arithmetic_operators():
    """Needed for project. Some arithmetic operators explaining their use
    and examples"""
    string_arithmetic_operators = """ 
                                                        Arithmetic operators
                                                        --------------------"""
    print(string_arithmetic_operators)
    sleep()
    print("The ** is the exponent operator. Example: 3 ** 2 =", 3 ** 2)
    sleep()
    print("The * numerics operator multiply. Example 3 *2 =", 3 * 2)
    sleep()
    print("The // is the floor division arithmetic operator")
    print("It divides two numbers and rounds down to the nearest integer")
    sleep()
    print("Example: 16//10=", 16 // 10)
    sleep()
    print("This would equal 1.6 if you divided, but will round down to 1")


def get_shortcut_operator():
    """Needed for project. This function shows the highest power 2 can
    be so it less than 500. Uses the *= shortcut operator"""
    string_shortcut_operators = """ 
                                                        Shortcut Operators
                                                        ------------------"""
    print(string_shortcut_operators)
    number = 2
    power_counter = 1
    while number < 500:
        number *= 2  # Multiplies by 2 every time
        power_counter += 1
    print(
        "2 can raised to the", power_counter - 1, "and still be less than 500")
# Optional sprint for project


def get_simple_lists():
    """Function that shows the simple things you can do with lists like
    constructing vertical / horizontal vectors"""
    string_simple_lists = """ 
                                                        Simple lists
                                                        ------------"""
    print(string_simple_lists)
    print("Vectors can be outputted horizontally or vertically")
    horizontal_vector = np.array(['x', 'y', 'z'])
    column_vector = np.array([['x'], ['y'], ['z']])
    print("Here is an example of a horizontal vector: ", horizontal_vector)
    print("Here is an example of a vectors displayed vertically: ")
    print(column_vector)


def get_lists_in_detail():
    """Goes more in depth about strings (copying/ cloning), iterating through
    lists, and initializing lists"""
    string_lists_in_detail = """ 
                                                        Lists in detail
                                                        ---------------"""
    print(string_lists_in_detail)
    print("Here is an example of copying a list")
    numbers_list = [1, 2, 3, 4, 5]
    new_number_list = numbers_list.copy()
    print(new_number_list)
    print("We can iterate through lists with a for loop")
    letters_list = ['a', 'b', 'c']
    sleep()
    for count in range(len(letters_list)):
        print(letters_list[count], end=" ")
    random_list = ['Hello'] * 10
    print(random_list)


def get_lists_in_lists():
    """Shows what a list inside a list looks like (matrices and cubes)"""
    lists_in_lists_string = """ 
                                        Lists in lists (matrices and cubes)
                                        -----------------------------------"""
    print(lists_in_lists_string)
    print("This program will display a 3 by 3 matrix")
    matrix = [[1, 2, 3],  # 3 by 3 matrix
              [4, 5, 6],
              [6, 7, 8]]
    for index in range(0, 3):
        print(matrix[index])  # will print the matrix
    print("The element on row 1 column 1 is", matrix[0][
        0])


def get_binary_number_twenty():
    """Converts the number 20 into binary and displays it horizontally.
    Will be used when doing bitwise operator calculations"""
    for digits_twenty in bin(20):  # Prints the number 20 in binary with spaces
        print(digits_twenty, end=" ")


def get_binary_number_twenty_one():
    """Converts the number 21 into binary and displays it horizontally"""
    seperate_numbers = """    """
    print(seperate_numbers)
    for digits_twenty_one in bin(21):
        print(digits_twenty_one, end=" ")


def calculate_and_bitwise_operator():
    """Shows what the & (and) bitwise operator does in a visual way"""
    print("\n& operator")
    print("----------")
    sleep()
    print("& is the and bitwise operator")
    print("It copies a bit if exists in both operands")
    print("The ones that are not similar will be changed to zeros")
    get_binary_number_twenty()
    get_binary_number_twenty_one()
    print("""\n--------------""")
    for digits in bin(20 & 21):
        print(digits, end=" ")
    sleep()
    print("\nConverting", bin(20 & 21), "into decimal we get", 20 & 21)


def calculate_xor():
    """Shows what the ^ bitwise operator does in a visual way"""
    print(" ^ Operator")
    print("------------")
    sleep()
    print(
     "The ^ is the XOR operator it copies a bit if it is in only one operand ")
    print("But not both")
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


def calculate_or_bitwise_operator():
    """Shows what the or bitwise operator does and gives examples"""
    print("| operator")
    print("----------")
    sleep()
    print("| is the bitwise or operator")
    print("if one or both bits are 1 output(1 | 0),(0|1) is", 1 | 0)
    print("Else if both bits are zero (0 | 0) it will equal", 0 | 0)


def calculate_right_shift_bitwise_operator():
    """Shows what the right shift bitwise operator shows >> in a visual
    way
    """
    print(">> operator")
    print("------------")
    print("The >> is the binary right shift bitwise operator.")
    print(
        "It shifts the number in binary to the right by whatever you tell it")
    print("Lets calculate 20 >> 1")
    for digits_twenty in bin(20):
        print(digits_twenty, end=" ")
    print("\n-------------")
    for arrow_right_answer in bin(20 >> 1):
        print(arrow_right_answer, end=" ")
    print("\nConverting it to decimal equals", 20 >> 1)


def calculate_left_shift_bitwise_operator():
    """Shows what the left shift bitwise operator << does in a visual way"""
    print("<< operator")
    print("-----------")
    sleep()
    print("The << is the binary shift left bitwise operator")
    sleep()
    print("It shifts the number in binary to the left by whatever you tell it"
          )
    print("Lets calculate 20 << 1")
    for digits_twenty in bin(20):
        print(digits_twenty, end=" ")
    print("\n---------------")
    for left_arrow_answer in bin(20 << 1):
        print(left_arrow_answer, end=" ")
    print("\nConverting it to decimal equals", 20 << 1)


def get_tuples_vs_lists():
    """Outlines what tuples are the difference between tuples and lists and
    shows some simple things that can be done with tuples"""
    string_tuples = """ 
                                                Tuples/ Tuples vs. Lists
                                                ------------------------"""
    print(string_tuples)

    print('Tuples are another way to store data like lists')
    print('A tuple cannot be changed (immutable)')
    sleep()
    print("A list can change")
    sleep()
    print("You can reassign tuples if you want to modify it")
    sleep()
    print(
        'Instead of brackets elements in the set are surrounded by parenthesis'
    )
    tuple_numbers = (1, 2, 3, 4)
    sleep()
    print("All the numbers in this tuple are", tuple_numbers[:])
    sleep()
    print("Indexing the last value in the tuple will output",
          tuple_numbers[-1])
    tuple_numbers = (2, 3, 4, 5)
    sleep()
    print("I changed the original tuple a bit so now it outputs",
          tuple_numbers)


def get_lists_within_tuples():
    """Shows how a list can be mutable even if its inside a tuple"""
    list_in_tuple = (1, 2, 3, [4, 5])
    sleep()
    print("We can change things that are mutable (like lists) inside a tuple")
    list_in_tuple[3][0] = 10
    sleep()
    print(list_in_tuple)
    sleep()


def get_tuples_within_lists():
    """Shows a tuple inside a list, and shows that the only way you can change
    them is if you reassgin them. Example is done with letters"""
    list_letters = ['a', 'b', 'c', ('d', 'e')]
    print(list_letters)
    print(
     'I cannot change the assigned values in the tuple unless I reassigned it')
    sleep()
    print("['a','b', 'c', ('f','g')]")
    sleep()
    list_letters = ['a', 'b', 'c', ('f', 'g')]
    print(list_letters)


def show_dictionary():
    """Shows things that can be done with a dictionary (iterating, adding
    keys, iterating through keys and values, and checking key existence with
    an example of a meal"""
    string_dictionaries = """ 
                                                    Dictionaries

                                                    ------------"""
    print(string_dictionaries)
    sleep()
    print("Here is a dictionary for a meal")
    meal = {'Food': 'Pizza', 'Drink': 'Water', 'complements': 'Breadsticks'}
    print(meal)
    meal['desert'] = 'Chocolate cake'  # Adds keys
    print(meal)
    meal.pop('complements')  # pops keys
    search_key = 'Food'
    answer = list(meal.keys()).index(search_key)
    print("Value index that correlates with pizza is", answer)
    for key in meal.keys():
        print(key)


def get_feedback_from_user():
    """"Gets feedback from the user about my project
    and writes it to a file called feedback.txt"""
    feedback_file = open('feedback.txt', 'a')
    user_feedback = input("Give me some feedback about my project: ")
    feedback_file.write("\n"+user_feedback)
    feedback_file.close()


def main():
    """Combines all the calculations about GDP and other
     functions which are needed for the project above and puts
     it all in this function. The main body of the program. After the function
     get_goodbye is called,the rest of the functions that are called are needed
     or an optional part of the Integration Project."""
    introduce_myself()
    get_greeting()
    get_user_guess_language()
    get_user_guess_number_of_countries()
    country_name = input(
     "Type a made up country you want to work with then hit \'Enter\': ")
    string_get_valid_variables_gdp = """ 
                                                    Get valid variables GDP
                                                    -----------------------"""
    print(string_get_valid_variables_gdp)
    print("GDP is a great indicator for economic growth in a country")
    sleep()
    print("The formula for GDP is: ")
    sleep()
    print(
     'GDP = Consumption + investment + government purchases + net exports')
    print("Net exports = Exports - imports")
    sleep()
    print("The variables used in the formula are whole numbers")
    print("You should type a + whole number for each variable you see below")
    print('I will not ask you for net exports')
    sleep()
    print(
     'In total the program will ask you to type a whole number in 8 times')
    print('---4 for the variables Old GDP')
    sleep()
    print('---4 for the variables New GDP')
    print("Both old GDP and New GDP still follow the same formula for GDP")
    print(
     "The reason I included both is that we are going to do some calculations")
    print("where I need both of them (% change, GDP per capita,)")
    print('If you type a whole number for every input, the program will:')
    print(
     '---Calculate the \'Old\' GDP you for the 1st numbers you put in ')
    print(
     '---Then Calculate the \'New\' GDP for the new numbers you put in')
    sleep()
    print(
     "If you type a letter/special character/float for any prompt:")
    print("---You have to try again")
    sleep()
    valid_variables_gdp = False
    while not valid_variables_gdp:
        try:
            print("Old GDP")
            print("-------")
            consumption = int(input(
             "Type a whole number for consumption then hit \'Enter\': "))
            investment = int(input(
             "Type a whole number for investment then hit \'Enter\': "))
            gov_purchases = int(input(
             'Type a whole number for government purchases then hit \'Enter\':'
            ))
            exports = int(input(
             "Type a whole number for exports then hit \'Enter\': "))
            imports = int(
             input("Type a whole number for imports then hit \'Enter\': "))
            print("New GDP")
            print("-------")
            new_consumption = int(input(
             "Type a whole number for new consumption then hit \'Enter\': "))
            new_investment = int(
                input(
                    "Type a whole number for investment then hit \'Enter\': "))
            new_gp = int(input(
             "Type a whole number for new gov purchases then hit \'Enter\': ")
            )  # gp is the same as government purchases
            new_exports = int(input(
             "Type a whole number for new exports then hit \'Enter\': "))
            new_imports = int(input(
             "Type a a whole number for new imports then hit \'Enter\': "))
        except ValueError:
            print("That was not a whole number. Try again")
        else:
            valid_variables_gdp = True
            print("Calculating Old GDP...")
            # The - arithmetic operator subtracts the value stored in imports
            # from exports (exports - imports)
            net_exports = exports - imports
            # The + arithmetic operator adds the values stored in consumption
            # , investment, government, purchases, and net exports and adds
            # them up to calculate GDP
            gdp = consumption + investment + gov_purchases + net_exports
            calculate_time()
            print("\nOld GDP value for", country_name, "is $" +
                  format(gdp, '.2f'))
            print("Calculating New GDP...")
            new_ne = new_exports - new_imports  # new_net_exports
            new_gdp = new_consumption + new_investment + new_gp + new_ne
            calculate_time()
            print(
                "\nNew GDP value for", country_name,
                "is $" + format(new_gdp, '.2f'))
            calculate_percent_change(gdp, new_gdp, country_name)
            get_population(gdp, new_gdp)
    calculate_average_gdp(country_name)
    country_list = ['US', 'China', 'Japan']
    order_country_list_numerically(country_list)
    order_country_list_alphabetically(country_list)
    read_and_guess_from_file()
    sleep()
    get_goodbye()
    string_needed_for_project = """ 
                                                         Needed for project
                                                         -------------------
                                                                            """
    print(string_needed_for_project)
    get_arithmetic_operators()
    get_shortcut_operator()
    string_data_structures_bitwise_operators = """ 
                                                               Data 
                                                            Structures
                                                        (bitwise operators)
                                                            >> << & ^ |
                                                        -------------------"""
    print(string_data_structures_bitwise_operators)
    sleep()
    print("Lets use 20 and 21 for all these examples")
    sleep()
    print("20 in binary is", bin(20))  # bin prints the number 20 in binary
    sleep()
    print("21 in binary is", bin(21))
    sleep()
    print("Looking at 20 and 21 in binary vertically...")
    get_binary_number_twenty()
    get_binary_number_twenty_one()
    calculate_and_bitwise_operator()
    calculate_xor()
    calculate_or_bitwise_operator()
    calculate_right_shift_bitwise_operator()
    calculate_left_shift_bitwise_operator()
    get_tuples_vs_lists()
    get_lists_within_tuples()
    get_tuples_within_lists()
    show_dictionary()
    get_feedback_from_user()
# call to main


if __name__ == "__main__":
    main()
