#file: caesarcipher.py
#author: sean (seanhays@bu.edu)
#description: this will take inputs for a key and for a statement, and shift by the key 


#i(lowercase) if 'a' <= c <= 'z':

#define cipher function function
def cipher(plaintext,key): 
    #convert the plaintext to lowercase 

    plaintext = plaintext.lower()
    # establish the accumulator variable 
    ciphered = " " 

    #loop through all charecters in lowercase plaintext 
    for ch in plaintext:
        # if ch in the plaintext are in alphabetical range, apply the shift to it 
        if ch in 'abcdefghijklmnopqrstuvwxyz':

            # shift plaintext by the key 
            shifted = (ord(ch)+key)
            # if the shifted value is out of range, wrap around 
            if shifted > ord('z'):
                shifted = shifted  - 26
            
            elif shifted < ord('a'):
                shifted = shifted + 26

            decoded = chr(int(shifted))
            ciphered = ciphered + decoded 

        else:
            
            ciphered = ciphered + ch 

    
    
    return ciphered 

#####################################

def main():
    print('Welcome to the ceasar cipher')
    plaintext = input('Please input the plaintext that you would like to shift: ')
    key = eval(input('Please enter your Shift key: '))
    ciphered = cipher(plaintext, key)
    print(ciphered)
main()
