import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# screen.setup(width=725, height=491)
# screen.bgcolor("lightblue")
# screen.tracer(0)  # Turn off animation for faster drawing

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()