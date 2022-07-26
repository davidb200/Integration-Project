"""Integration Project (GDP Calculator)"""

__author__ = "David Betanzos"

import time


def main():
    """
    The main body of the program. Does the calculations of GDP and GDP per
    capita from the numbers the user typed. All the other functions are used
    here.
    """

    # Greeting to user

    get_greeting()

    # Context about GDP

    print("GDP is great way to measure a country's economic growth")
    print("THe formula for GDP is: ")
    print("GDP=Consumption + Investment + Government purchases + net exports")
    print("Where the variables are a positive float number")
    print("Where net exports = exports - imports")

    # Get country name from user

    country_name = input("Enter a made up country: ")

    # Getting Numbers used to calculate GDP

    consumption = get_valid_float_input("Enter consumption: ")
    investment = get_valid_float_input("Enter investment: ")
    government_purchases = get_valid_float_input("Enter Government purchases:")
    exports = get_valid_float_input("Enter Exports: ")
    imports = get_valid_float_input("Enter Imports: ")

    net_exports = exports - imports

    gdp = consumption + investment + government_purchases + net_exports

    # Display GDP

    print("Calculating GDP:")
    countdown_timer()
    print(country_name + "'s", "GDP is $", format(gdp, '.2f'))

    # Percentage of GDP for each variable

    consumption_percentage = (consumption / gdp) * 100
    investment_percentage = (investment / gdp) * 100
    gp_percentage = (government_purchases / gdp) * 100
    net_exports_percentage = (net_exports / gdp) * 100

    # Display percentage of each variable GDP

    print("Breakdown of", country_name + "'s GDP")
    print("--------------------------")
    print("Consumption makes up", consumption_percentage, "% of GDP")
    print("Investment makes up", investment_percentage, "% of GDP")
    print("Government Purchases make up", gp_percentage, "% of GDP")
    print("Net Exports makes up", net_exports_percentage, "% of GDP")

    # GDP per capita Context

    print("GDP per capita is another method of measuring growth like GDP")
    print("THe formula for GDP per capita is:")
    print("GDP per capita = GDP / population")

    # Getting a valid population to do calculation for GDP per capita

    population = get_valid_population("Enter the population: ")

    gdp_per_capita = gdp / population

    # Display GDP per capita

    print("Calculating GDP per capita:")
    countdown_timer()
    print("GDP per capita is", format(gdp_per_capita, '.2f'))

    # Any feedback about my project

    get_feedback_from_user()


def get_greeting():
    """
    Asks the user running the project for their name and describes what
    my project is about
    Parameters : None
    Return : None
    """
    print("Hello! Welcome to my \"Integration Project\"")
    name_of_user = input("Please enter your name: ")
    print("Hello! " + name_of_user + " nice to meet you!")
    print("Welcome to my GDP calculator!")


def get_valid_float_input(prompt):
    """
    Gets valid float input from the user and returns a valid float.
    Parameters: A prompt asking the user to enter a number
    Return: A valid float
    """
    valid_float_input_from_user = False
    while not valid_float_input_from_user:
        try:
            valid_float = float(input(prompt))
        except ValueError:  # User enters letter or special character
            print("That was not a valid number. Try again")
        else:
            if valid_float <= 0:  # Anything the user enters
                # cannot be less than 0 (dealing with population)
                print("It can't be a negative number or 0 try again.")
                valid_float_input_from_user = False
            else:  # User enters a valid float to work with
                # valid_float_input_fro_user will return true
                return valid_float


def get_valid_population(prompt):
    """
    Gets a valid positive whole number for the population from the
    user. Population can not be a decimal, negative number, or
    zero.
    Parameters : A prompt asking the user to enter a number for a variable
    Return : A valid population number
    """
    valid_population_input_from_user = False
    while not valid_population_input_from_user:
        try:
            valid_population = int(input(prompt))
        except ValueError:  # User enters a letter,special character,
            # or decimal
            print("You did not give me a valid number. Try again.")
        else:
            if valid_population <= 0:  # The user does not enter a legitimate
                # number for the population
                print("Population can't be 0 or a - number. Try again")
                valid_population_input_from_user = False
            else:  # The user enters a legitimate number for the population
                # valid_input_validation_from_user will return true
                return valid_population


def countdown_timer():
    """
    Timer to show when the answers the computer calculates comes on the
    screen.
    Parameters: None
    Return : None
    """
    for seconds in range(5, 0, -1):
        print(seconds)
        time.sleep(1)


def get_feedback_from_user():
    """
    After the program is finished, I ask the user to give feedback about
    my program and their response will write to a file called feedback.txt
    Parameters: None
    Returns: None
    """
    feedback_file = open("feedback.txt.", 'a')
    userinput = input("Provide me some feedback: ")
    feedback_file.write(userinput)
    feedback_file.write("\n")


if __name__ == "__main__":
    main()
