from turtle import *
import random

screen = Screen()
player = Turtle()
player.shape('turtle')
player.up()

def up():
    player.setheading(90)
    player.forward(5)
    dig()

def down():
    player.setheading(270)
    player.forward(5)
    dig()

def right():
    player.setheading(0)
    player.forward(5)
    dig()

def left():
    player.setheading(180)
    player.forward(5)
    dig()

def make_turtle():
    t = Turtle()
    t.shape("square")
    t.up()
    t.color("green")
    t.turtlesize(2)
    t.speed("fastest")
    return t

def create_map():
    ground = []
    for row in range(7):
        new_row = []
        for col in range(7):
            t = make_turtle()
            new_row.append(t)
        ground.append(new_row)
    return ground

def show_map(t_map):
    for row in range(7):
        for col in range(7):
            t_map[row][col].goto(col*42 - 142, row*42 -142)

def dig():
    global m, goal_row, goal_col
    for row in m:
        for square in row:
            if player.distance(square) < 15:
                square.color("chocolate")
                c = row.index(square)
                r = m.index(row)
                if goal_row  == r and goal_col == c:
                    square.color("gold")
                    square.shape("circle")
def main():
    global m, goal_row, goal_col
    m = create_map()
    show_map(m)
    player.goto(0,0)
    goal_row = random.randint(0,6)
    goal_col = random.randint(0,6)

    screen.onkey(up, "Up")
    screen.onkey(down, "Down")
    screen.onkey(left, "Left")
    screen.onkey(right, "Right")

    screen.listen()

main()
