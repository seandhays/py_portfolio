#file: treeHeight.py
#author: sean (seanhays@bu.edu)
#description: demonstrates using a module to access its functions

#module: a fule containing pre-existing python code
#finction: a self-contained program, with inputs( parameters) and outputs
#
#syntax to access a function in a module:
#gen form: <var> = <module.<function>(<parameter>)
import math

def main():
    
    #input: collect the distance to the tree
    
    #input: collect the angle to the top 
    distance = eval(input("Enter your distance from the tree in meters: "))
    angle = eval(input("enter the angle to the top of the branches: "))
    
    #process: height = apply tan(theta) * distance
    angleRadians = math.radians(angle)
    height = math.tan(angleRadians) * distance
     
    #output: print out the height
    print('The tree is',height,'meters tall.')
    

main()
