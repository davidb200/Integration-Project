# David Betanzos
# A program that computes different things about GDP
import time
# Get Greeting
# The + operator cocatenates(mooshes) "Hello " with name the user entered
# Will output Hello name of user
print("Hello welcome to my integration project!")
name_of_user = input("Enter your name: ")
print("Hello " + name_of_user, "its great to interact with you")
# User guesses programming language
user_language_guess = input("Guess what higher level programming language I am using? ")
if user_language_guess == "Python" or user_language_guess == "python":
    print("Correct!")
else:
    print("Sorry that was incorrect. I am using Python for my integration project")
# User guess number of countries in the world
number_of_countries_guess = int(input("Enter how many countries are there: "))
if number_of_countries_guess == 196:
    print("Wow, I did not expect you to get that correct")
print("There are actually a total of 196 countries around the world!")
print("Each country has a different GDP")
# Country user types
country_name = input("Enter a country you want to work with: ")
# Function that countdowns the time the user entered (in secs) to get an answer
# The countdown is set to 3 when computing an answer later on in the program
# When called will output(3 2 1), like a timer
# Will be used later on when doing calculations


def calculate_time():
    countdown = 3
    for count in range(1, countdown + 1):
        print(countdown, end=" ")
        time.sleep(1)
        countdown -= 1


# Get valid variables old GDP and calculates GDP
# GDP formula = consumption + investment + government purchases(gov_purchases) + net exports
# Net exports = exports - imports
# The numbers in the formula are usually whole numbers
# The + numeric operator adds up the values the user inputted into the formula together
# The - numeric operator subtracts the imports from the exports the user entered (exports - imports)

valid_variable_GDP = False
while not valid_variable_GDP:
    try:
        consumption = int(input("Enter consumption: "))  # consumption user types
        investment = int(input("Enter investment: "))  # investment user types
        gov_purchases = int(input("Enter government purchases: "))  # gp user types
        exports = int(input("Enter exports: "))  # exports user types
        imports = int(input("Enter imports: "))  # imports user types
    except ValueError:
        print("That was not a whole number. Try again")
    else:
        net_exports = exports - imports
        gdp = consumption + investment + gov_purchases + net_exports
        print("Calculating GDP...")
        calculate_time()
        print("\nThe GDP for", country_name, "is $" + str(format(gdp, '.2f')), sep="-->")
        valid_variable_GDP = True
# Get valid variables new GDP
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
        print("\nYour new GDP value for", country_name, "is $"+str(format(new_gdp, '.2f')))
        valid_variable_GDP_two = False

# Function that calculates percent change between old and new GDP and whether it grew,declined, or stayed
# the same
# percent change formula = [(new GDP - old GDP) / old GDP ] * 100
# Answer will be a percent to 1 decimal place
# The * numerical operator multiplies two numbers. In the function below it will multiply the
# number stored in the new_minus_old_value_over by 100 to get the percent


def calculate_percent_change():
    new_minus_old_value = new_gdp - gdp
    new_minus_old_value_over_old = new_minus_old_value / gdp
    percent_change = new_minus_old_value_over_old * 100
    print("The program will now calculate the % change between your old and new GDP")
    print("Calculating percent change...")
    calculate_time()
    if percent_change > 0:
        print("\n"+country_name, "has grown by", str(format(percent_change, '.1f')) + "%")
    elif percent_change < 0:
        print("\n"+country_name, "has grown by", str(format(percent_change, '.1f')) + "%")
    elif percent_change == 0:
        print("\n"+country_name, "has not changed one bit")


def calculate_average_gdp():
    print("GDP can change alot over the years")
    time.sleep(1)
    print("We can find the average GDP over X amount of years")
    time.sleep(1)
    print("Type your old and new GDP then enter values you find online")
    print("Type zero to get out of the loop")
    gdp_number = int(input("Enter GDP: "))
    counter = 0
    total = 0
    while gdp_number != 0:
        total += gdp_number
        counter += 1
        gdp_number = int(input("Enter GDP: "))
    print("Calculating average GDP...")
    calculate_time()
    print("\nAverage GDP for", country_name, "over", counter, "years is $" + str(format(total/counter, '.2f')))

# Function that calculates GDP per capita given if user wants old or new GDP
# GDP per capita formula = The gdp / population
# The / numeric operator is just division (divides two numbers)


def calculate_gdp_per_capita(population):
    user_choice_gdp = input("Would you like to use you old or new GDP (type old or new): ")
    if user_choice_gdp == "old":
        gdp_per_capita = gdp / population
        print("Calculating GDP per capita...")
        calculate_time()
        print("\nGiven your old GDP, GDP per capita is $"+str(format(gdp_per_capita, '.2f')))
    elif user_choice_gdp == "new":
        gdp_per_capita_two = new_gdp / population
        print("Calculating GDP per capita...")
        calculate_time()
        print("\nGiven your new GDP, GDP per capita is", format(gdp_per_capita_two, '.2f'))
    else:
        print("I could not do the calculation because you gave me an invalid choice")


def main():
    calculate_percent_change()
    calculate_average_gdp()
    print("GDP per capita is also a useful tool for measuring GDP")
    population = int(input("Enter the population: "))
    calculate_gdp_per_capita(population)

# call to main


main()
# User guesses top 2 countries from a file called country_name.txt
# User has to guess a number and not insert a letter
country_names = open('country_names.txt')
print("There is a text file with ten countries randomly sorted with the biggest GDPs")
print("Look at the countries and guess which 2 countries are the highest")
print("Your answer will be a number (Example if I think its the UK first then China I will type 37")
valid_number = True
while valid_number:
    try:
        user_countries_guess = int(input("Guess which countries are top 2: "))
    except ValueError:
        print("That was not a number")
    else:
        if user_countries_guess > 26 and user_countries_guess % 3 == 0:
            print("Congratulations! you are right")
        else:
            print("That was a hard question the answer was 27")
            valid_number = False
print("Thanks for trying me out. I hope you learned something about GDP", name_of_user)
# The % is the modulus operator it takes the remainder from division of two numbers
# The answer I am looking for %3 = 0 in this case because 3 goes into 27 9 times with no remainder
# Goodbye message
print('goodbye' * 10)  # The * string operator prints goodbye 10 times
# Needed for project
print("The rest is needed as a part of my project")
time.sleep(1)
print("The ** is the exponent operator. Example: 3 ** 2 =", 3**2)
time.sleep(1)
print("The * numerics operator multiply. Example 3 *2 =", 3*2)
time.sleep(1)
print("The // is floor division it divides two numbers and rounds down to the nearest integer")
time.sleep(1)
print("Example: 16//10=", 16//10, "because this would equal 1.6 if you divided, but will round down to 1")
print("The next program will show the highest power 2 can be to so it less than 500")
number = 2
power_counter = 1
while number < 500:
    number *= 2
    power_counter += 1
print("2 can raised to the", power_counter-1, "and still be less than 500")
