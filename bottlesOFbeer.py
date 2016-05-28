#file: bottlesOfBeer.py
#author: sean (seanhays@bu.edu)
#description: will print out the poem bottles of beer, as many times as specified

#define main function
def main():

#welcome user
    print("Welcome to Everybody's Favorite drinking song")
    
#collect input from user ( number of bottles of beer)
    bottles = eval(input("Please enter the largest number you can think of: "))
#use for loop to print poem as many times as bottles of beer
    for i in range(bottles):
    
        print(bottles,'of beer on the wall')
        print(bottles,'bottles of beer!')
        print('If on of those bottles should happen to fall...')
        print(bottles-1,'bottles of beer on the wall!')
        print()
        #edit bottles variable 
        bottles = bottles - 1 

    print('Thank you for waiting for the program to finish')
    

main()
