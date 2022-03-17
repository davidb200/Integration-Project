#David Betanzos
#A program that computes GDP,per capita and the change in GDP
import time
print("Hello user! Welcome to my integration project!")
print("It is a great pleasure to interact with you!")

#Greeting

name_of_user= input("Please enter your name: ")
print("Hey!",name_of_user, end = " ")
print("Welcome to my GDP calculator! Great to have you!")


#Getting information (variables for GDP)

#GDP Formula = consumption+investment+government purchases(gp)+net exports
#Net exports formula = exports - imports
#The numbers in the formula are usually whole numbers
country_name = input("Type the name of your country: ")#Country user types   
consumption= int(input("Enter consumption: "))#consumption user types 
investment = int(input("Enter investment: "))#invesment user types
gp_one = int(input("Enter gov purchases: "))#gp user types
exports = int(input("Enter exports: ")) #exports user types
imports = int(input("Enter imports: ")) #imports user types

#caclucations (GDP)

net_exports = exports - imports #Net exports = exports - imports
#the -(minus) sign subtracts the two numbers (exports - imports)
gdp = consumption + investment + gp_one + net_exports
#variables from GDP formula
#the + sign above adds all the values from the variables shown in this case

#What the user sees
print("Calculating results ...")
time.sleep(3)
print("The GDP for", country_name, "is", "$"+str(format(gdp,'.2f')),sep='-->')

#Growth of the country GDP (getting information)
print("Lets see how much",country_name, "is growing by if we changed the numbers!")
consumption_two = int(input("Enter new consumption: "))#new value of consumption
investment_two = int(input("Enter new investment: "))#new value of investment
gp_two = int(input("Enter new govt purchases: "))#new value of govt purchases
exports_two = int(input("Enter new exports: "))#new value of exports
imports_two = int(input("Enter new imports: "))#new value of imports
net_exports_two = exports_two - imports_two#newvalue of net exports
gdp_two = consumption_two+investment_two+gp_two+net_exports_two#new GDP value
print("Calculating new GDP value...")
time.sleep(3)
print("Your new GDP value is","$"+str(gdp_two))

#Calcuations(perecent change)
#percent change formula = [(new GDP - old GDP value)/old GDP value ] * 100
new_minus_old_value = gdp_two - gdp #new GDP - old GDP value
divide_by_old_value = new_minus_old_value / gdp#[(new - old value)/old value]
growth_rate = divide_by_old_value * 100 #[(new - old value)/old value] * 100

#What the user sees(after perecent change calaculation)
print("Calculating percent change between your old GDP and new GDP ...")
time.sleep(5)
if growth_rate < 0:
    print(country_name+"'s","GDP would decrease by", format(growth_rate,'.1f')+"%")
elif growth_rate > 0:
    print(country_name+"'s","GDP would grow by",format(growth_rate,'.1f')+"%")
elif growth_rate == 0:
    print(country_name+"'s","GDP has seemed to not change at all")
#Percent component of biggest number and samllest of GDP
def calculate_gdp_percent(user_gdp_input):
    gdp_one_list = [consumption, investment, gp_one, exports, imports]
    time.sleep(3)
    print("Your highest number that you put is",max(gdp_one_list))
    print("It would account for", format((max(gdp_one_list)/gdp) * 100, '.1f'), "% of the GDP")
    print("Your lowest number that you put is", min(gdp_one_list))
    print("It would account for", format((min(gdp_one_list)/gdp_two) * 100, '.1f'), "% of the GDP")
    print(min(gdp_one_list))
def calculate_gdptwo_percent(user_gdp_input):
    gdp_two_list = [consumption_two, investment_two, gp_two, exports_two, imports_two]
    time.sleep(3)
    print("Your highest number that you put is", max(gdp_two_list))
    time.sleep(3)
    print("It accounts for", format((max(gdp_two_list)/gdp_two) * 100, '.1f'), "% of the GDP")
    time.sleep(3)
    print("Your lowest number that you put is", min(gdp_two_list))
    time.sleep(3)
    print("It would account for", format((min(gdp_two_list)/gdp_two) * 100, '.1f'), " % of the GDP")
def main():
    user_gdp_input = input("Would you like to use your old or new GDP to find the biggest? ")
    if user_gdp_input == "old":
        calculate_gdp_percent(user_gdp_input)
    elif user_gdp_input == "new":
        calculate_gdptwo_percent(user_gdp_input)
main()




#Average GDP over the years

time.sleep(2)
print(country_name+"'s", "GDP tends to change a lot over the years")
time.sleep(1)
print('We can find the average GDP over the past X yrs of',country_name,'for example')
time.sleep(1)
print("Enter your old and new GDP value, then add some new values you find online")
time.sleep(1)
print("Type zero or a negative number to get out of the loop")
total = 0
counter = 0
gdp_number = int(input("Enter GDP: "))
while (gdp_number > 0):
    total += gdp_number
    counter += 1
    gdp_number = int(input("Enter GDP: "))
print("Calculating average GDP...")
time.sleep(5)
print("Average GDP for",country_name,"over", counter, "years",
      "is $"+str(format(total/counter,'.2f')))
time.sleep (2)

#Getting Information (GDP per capita = GDP/ population)
print("GDP per capita also measures economic growth!")
print("I am going to use your old GDP for this calculation")
population = int(input("Enter the population: "))

#Calcualtions (GDP per capita)
gdp_per_capita = gdp / population
# / sign divides value stored in GDP by the value stored in population
#it will output a floating point value.

#What the user sees (GDP per capita)
print("Calculating GDP per capita...")
time.sleep(3)
print(country_name + "'s", "GDP per capita is $" + str(format(gdp_per_capita, '.2f')))

# User guess for actual GDP of Argentina

time.sleep(2)
print("All the answers I computed for you is probably not the exact GDP of Argentina")
time.sleep(2)
print("I'll give you 3 guesses to figure out the actual GDP of Argentina")
time.sleep(2)
print("Hint(It is between 380 and 390 and the answer % 10 = 3)")
for answers in range (3): 
    guess = int(input("Enter Guess: "))
    if (guess >= 384) and (guess <= 390):
        print("Try a smaller number!")
    elif (guess >= 380) and (guess <= 382) :
        print("Try a bigger number!")
    elif guess < 380 or guess > 390:
        print("Remember to use the hint I gave you")
    elif guess == 383:
        print("Congratulations, you got it right!")
        break
time.sleep(2)
print("If you got the answer right or wrong Argentina's GDP is $383 billion.")
      
#Goodbye message
time.sleep(2)
print("Thanks, "+name_of_user,"for trying me out")
#the + operator cocatenates (mooshes them) Thanks, and input from name of user
#together
print("goodbye"*1)#the * operator prints goodbye 1 time

# Needed for project
time.sleep(5)
print("The rest is needed as part of my project")
time.sleep(1)
print("The % operator is the modulus operator. It takes the remainder from"
      "division. Example: 4 % 2 =", 4%2)
time.sleep(1)
print("The ** operator is the exponent operator. Example: 3**2 =", 3**2)
time.sleep(1)
print("The // operator is floor division which divides the numbers and rounds")
print("down to the nearest integers. Example: 16 //10 =", 16//10)
time.sleep(1)
print("The not boolean operator checks if the two values do not equal")
print("For example: not 3 == 4 will output", not 3 == 4,"because they don't equal")



























