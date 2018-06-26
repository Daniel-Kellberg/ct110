# CTI 110
# P4 Lab
# Daniel Kellberg
# June 25, 2018

def main():
    import turtle
    def draw_star(size):
        angle = 120
    
        for side in range(5):
            turtle.forward(size)
            turtle.right(angle)
            turtle.forward(size)
            turtle.right(72 - angle)
        turtle.end_fill()
        return

    draw_star(100)


main()
