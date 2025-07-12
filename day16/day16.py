from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.speed(1)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
timmy.backward(30)
timmy.setpos(30, 90)



tp = timmy.pos()
print(tp)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


