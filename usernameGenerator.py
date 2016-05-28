#file: username Generator.py
#author: sean hays(seanhays@bu.edu)
#description: this will prompt the user for three inputs, give a greeting and crate a username

#define main function
def main():
    #take user input for firs, middle, and last name
    first = input('What is your first name? ')
    middle = input('What is your middle name? ')
    last = input(' What is your last name? ')
    print()
    #welcome user
    print('Welcome,',first,last)
    print()
    #print out username

    username = first[0] + middle[0] + last[:6]

    print('Your new user name is',username)


    
main()

    
