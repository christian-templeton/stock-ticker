#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys

# Gather our code in a main() function

def name():
    name = input('Hi, I\'m Rye and I\'m a serviceDoodle. What\'s your name?')
    print 'Nice to meet you', name + '!!!!!'


    mood = input('My job\'s to help people. You can message with me like you would your best friend... after all I am a dog. Are you feeling down?')
    if mood == ('yes') or ('yeah') or ('Yes') or ('a litte'):
        print input('Oh no! Want to pet me? I just got a haircut?') + '?...'
    else:
        print ('Oh good! Want to play?') + '?...'

 
    help = input('I\'ll be right over - my mom will attach a receipt to my collar and we can let her take care of billing later - is that okay?')
    if help == ('yes') or ('yeah') or ('Yes') or ('yes!') or ('Yes!'):
        print input('Great! See you soon') + ' ' + name
    else:
        print 'Ok let me get my mom'
    
  
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    name()
