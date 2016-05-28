#!/usr/bin/python

#file: helloWeb.py
#author: sean hays (seanhays@bu.edu)
#description: this program will 
import time
import random 


# the main section of the program
if __name__ == "__main__":

    # HTTP headers
    print "Content-type: text/html"
    print
     #pick some letters and a number
    
    quotes = ('We will not tire, we will not falter, and we will not fail.',
          'Freedom itself was attacked this morning by a faceless coward,and freedom will be defended.',
          'I can hear you, the rest of the world can hear you and the people who knocked these buildings down will hear all of us soon.',
          'Its clearly a budget. Its got a lot of numbers in it.',
          'To those of you who received honours, awards and distinctions, I say well done. And to the C students, I say you, too, can be president of the United States.')

    
    pictures = ('http://i.usatoday.net/communitymanager/_photos/the-oval/2011/07/13/bush-world%20seriesx-large.jpg',
                'http://www.usnews.com/cmsmedia/3e/d07fa8ab4e693d9657bcc69b7223dd/40985FE_DA_130425bush2001.jpg',
                'http://yaleherald.com/wp-content/uploads/2012/08/george-bush.jpeg',
                'https://upload.wikimedia.org/wikipedia/commons/8/80/Bush_Addresses_the_Nation_on_Immigration_Reform.jpg',
                'http://crooksandliars.com/files/primary_image/15/09/george-w-bush-waving-facebook.jpg')

    quote = random.choice(quotes)
    picture = random.choice(pictures)
    
        
    print """
<html>
<head>Quote of the Day - by George W. Bush
<p>
</head>

<body>
%s
<p>
<img src="%s" width=200 height= 200 >
</body>
</html>

""" % (quote,picture)
    
