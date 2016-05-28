#file: generateBMITable.py
#author: sean (seanhays@bu.edu)
#description: This will create a BMI table  

##############################################################
def calculateBMI(height,weight):

   # describe function
    """ takes two parameters for height and weight and returns Body Mass Index"""

    # convert values 

    kg = weight * .4536
    meters = height * .0254 

    #calculate BMI

    bmi = (kg / (meters*meters))

    #return, exit function

    return bmi
#########################################################
def printBMITable(startHeight,endHeight,startWeight,endWeight):
    #describe function 
    """ this function will print out a table within the bounds of the specified parameters"""
    
    #initialize loop for height
    

    for x in range(startHeight,endHeight+1):
        print(x,' ', end="")
         #initialize loop for weight
        for y in range(startWeight,endWeight,10):
            
            print("%.2f" % calculateBMI(x,y), end=" ")

            
        #line break
        print()
   
        
                   
    return
#########################################################
def main():
  print('This program will collect lower and upper bounds for height and weight,\n and produce a table with the corresponding BMI values') 
  print()
  x = eval(input('What is starting height: '))
  y = eval(input('What is ending height: '))
  z = eval(input('What is the start weight: '))
  d = eval(input('What is the end weight: '))
  print('Height Weight ---->')
  l = range(z,d,10)
  print(*l,sep='   ')
  printBMITable(x,y,z,d)
  
    

main()
