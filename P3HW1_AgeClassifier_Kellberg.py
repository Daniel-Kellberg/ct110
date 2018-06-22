# CTI-110
# P3HW1 - Age Classifier
# Daniel Kellberg
#June 21, 2018
#

def main(age):
    print( 'I do not know why I had to put this main function into this program. ')
    

age = int(input('What is your age? '))

if age <= 1:
    print('You are an infant' )

elif age <= 12:
    print('You are a child ')

elif age <= 19:
    print('You are a teenager ' )

else:
    print( 'You are an adult ')

main(age)


