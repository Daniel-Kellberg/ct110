#CTI 110
# P3T1 Area of Rectangles
# Daniel Kellberg
# June 21, 2018

length1 = int(input('Enter the length of rectangle1: '))
width1 = int(input ('Enter the width of rectangle 1: '))

length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the length of rectangle 2: '))

area1 = length1 * width1
area2 = length2 * width2

if area1 > area2:
    print ('Rectangle 1 has the greater area. ')
elif area2 > area1:
    print ('Rectangel 2 has the greater area ')
else:
    print ('Both have the same area. ')

