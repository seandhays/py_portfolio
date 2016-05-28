#file: change04.py
#author: sean ( seanhays@bu.edu)
#description: This program will extend the functionality of change03.py by also finding the
#number of nickels and pennies. 
#date: September 8th, 2015
def main():
    price = 42
    change = 100 - price
    quarters = change // 25
    print('The price of your item is',price,'cents, and your change is',change,'cents.')
    change = change % 25
    dimes = change // 10
    change = change % 10
    nickels = change // 5
    change = change % 5
    pennies = change 
    print('Here is your change in coins:\n\tQuarters:',quarters,'\n\tdimes:',dimes,'\n\tnickels:',nickels,'\n\tpennies:',pennies)

main()
