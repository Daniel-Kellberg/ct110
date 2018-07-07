# CTI 110
# Python 5 Homework Kilometer Converter
# July 1, 2018
# Daniel Kellber

def main():

    def show_miles():
        kilometers = float(input( "Please enter the distance in kilometers: "))
        kilometersToMiles = kilometers * 0.6214
        print("The distance in miles is: "+ str( kilometersToMiles))

    show_miles()

main()

