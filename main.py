import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game by @Kushal Panchal")
image = "F:/Kushal/Programing/Python Programing/game/us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("F:/Kushal/Programing/Python Programing/game/us-states-game/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        #use list comperhernsion in line 20
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("F:/Kushal/Programing/Python Programing/game/us-states-game/states_to_learn.csv")
        break

    
    if answer_state:
        answer_state = answer_state.title()
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
  
turtle.mainloop()