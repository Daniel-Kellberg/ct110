#Feet To Inches Project
#July 1, 2018
# CTI-110 P5T2_FeettoInches
#Daniel Kellberg
#
INCHES_PER_FOOT = 12

def main():
    feet = int(input('Enter a number of feet: '))

    print( feet, 'equals', feet_to_inches(feet), 'inches.')

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

main()
