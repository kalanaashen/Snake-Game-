from turtle import Turtle
MOVE_DISTANCE=20
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for new_turtle in range(3):
            turtle = Turtle()
            turtle.color("white")
            turtle.shape("square")
            turtle.penup()
            turtle.speed(10)
            turtle.goto(-(new_turtle * 20), 0)
            self.segments.append(turtle)

    def snake_move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            temp_x = self.segments[seg - 1].xcor()
            temp_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(temp_x, temp_y)
        self.head.forward(MOVE_DISTANCE)
    def snake_up(self):
            if self.head.heading()!=270:
                self.head.setheading(90)
    def snake_down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)
    def snake_right(self):
        if self.head.heading()!=180:
           self.head.setheading(0)
    def snake_left(self):
        if self.head.heading()!=0:
           self.head.setheading(180)

    def new_part(self):
        for new_turtle in range(1):
            turtle = Turtle()
            turtle.color("white")
            turtle.shape("square")
            turtle.penup()
            turtle.speed(10)
            turtle.goto(-(new_turtle * 20), 0)
            self.segments.append(turtle)
            self.snake_move()
