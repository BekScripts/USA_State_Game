import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
states_data = pandas.read_csv("50_states.csv")
states_names = states_data["state"].to_list()



score = 0
game_is_on = True
answered_states = []
while game_is_on:

    answer_state = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state name?")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        break

    if answer_state in states_names:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row = states_data[states_data["state"] == answer_state]
        t.goto(int(row['x']), int(row['y']))
        score += 1
        t.write(answer_state)
        answered_states.append(answer_state)

    if score == 50:
        game_is_on = False

not_answered_states = []

for state in states_names:
    if state not in answer_state:
        not_answered_states.append(state)

df = pandas.DataFrame(not_answered_states)
csv_file = df.to_csv("not_answered_states")




turtle.mainloop()
screen.exitonclick()


