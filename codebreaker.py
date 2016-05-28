#assignment: codebreaker.py
#author: seanhays (seanhays@bu.edu) 
#description: this code will break a caear shift

###############################################################
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
        # if the charaecter is not alphabetic, do not shift.
        else:
            
            ciphered = ciphered + ch 

    
    
    return ciphered
########################################################
def main():
    print('Welcome to code breaker: ')
    plaintext = input('Enter your coded phrase: ')

    for key in range(0,27,1):
        ciphered = cipher(plaintext, 26 -key)
        print(ciphered,'--->',key)

main()
