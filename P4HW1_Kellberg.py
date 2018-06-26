# CTI 110
# P4 HW1 Distance Traveled
# Daniel Kellberg
# June 25, 2018
def main():
    speed = int(input('What is the speed of the vehicle in mph?'))
    time = int(input('How many hours has it traveled?'))

    print(speed)
    print(time)

    for time in range(1, 1+ time):
        DistanceTraveled= speed * time
        print(time, '/t', DistanceTraveled, 'miles')

main()
