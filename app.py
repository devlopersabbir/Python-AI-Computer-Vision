from turtle import Screen, Turtle

class Drawing:
    turt:Turtle = Turtle()
    screen = Screen()
    def left_right(self, isLeft:bool):
        heading = self.turt.heading() + 20 if isLeft else self.turt.heading() - 20 # left right condision
        self.turt.setheading(heading)
        self.turt.forward(20)
    def forward_backward(self, isFor:bool):
        self.turt.forward(10) if isFor else self.turt.backward(10) # forward backward condision
    def clearScreen(self):
        self.turt.clear()  # Clears turtle drawings
        self.turt.penup()
        self.turt.home()  # Move the turtle to its home position (starting position)
        self.turt.pendown()
    def run(self):
        self.screen.listen()
        self.screen.onkey(lambda: self.left_right(True), "l")
        self.screen.onkey(lambda: self.left_right(False), "r")
        self.screen.onkey(lambda: self.forward_backward(True), "f")
        self.screen.onkey(lambda: self.left_right(False), "b")
        self.screen.onkey(self.clearScreen, "c")
        self.screen.mainloop()


game = Drawing()
game.run()
