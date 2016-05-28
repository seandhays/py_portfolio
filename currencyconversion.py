#file: currencyconversion
#author: sean(seanhays@bu.edu)
#description: Demonstrate the input-proccess-output design pattern

#design pattern: a re-usable model for creating a program.
#input-proccess-output pattern: the most basic model for a program which takes
#one or several inputs from the user, applies a computation proccess, and provides
#an output back to the user

def main():

    #collect an input
    pesos = eval(input('What is the price in pesos? '))
    
    
    # process the algorithm
    #16.77 PESOS == `1 US DOLLAR
    dollars = pesos / 16.77
    

    #provide output to user
    print('The price in dollars is',dollars)

main()
