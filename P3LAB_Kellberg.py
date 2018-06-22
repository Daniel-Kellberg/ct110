# CTI 110
# P3 Lab
# Daniel Kellberg
# June 22, 2018

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80-89
    C_score = 70-79
    D_score = 60-69
    F_score = 0 -50
    # TO DO: define the rest of the scores

    
    score = int(input('Enter grade: '))

    if score >= 90:
        print('Your grade is: A' )
    elif score >= 89:
        print('Your grade is: B')
    elif score >= 70:
        print('Your grade is: C')
    elif score >= 60:
        print ('Your grade is: D')
    else:
        print('Your grade is: F') # TO DO: finish this







# program start
main()
