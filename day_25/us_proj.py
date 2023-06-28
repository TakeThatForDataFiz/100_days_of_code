"""
us_proj - script that 
        creates a US state quiz using
        pandas data frame and turtle libs
"""
import turtle
import pandas as pd

# create turtle screen with US image as GIF file
screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

coord_df = pd.read_csv("50_states.csv")
data = pd.read_csv("50_states.csv")
all_stes = data.state.to_list()
guessed_states = []
missing_states = []

while len(guessed_states) < 50:

    answr_ste = screen.textinput(
        title=f"Guess the State, {len(guessed_states)}/50 guessed", prompt="What's another state's name?"
    ).title()
    if answr_ste == 'Exit':
        break
    if answr_ste in all_stes:
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        ste_data = data[data.state == answr_ste]
        t.goto(x=int(ste_data.iloc[0].x), y=int(ste_data.iloc[0].y))
        t.write(answr_ste)
        guessed_states.append(answr_ste)


for state in all_stes:
    if state not in guessed_states:
        missing_states.append(state)
output_df = pd.DataFrame(missing_states)
output_df.to_csv('states_to_learn.csv')

screen.exitonclick()
