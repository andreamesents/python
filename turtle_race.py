



# from turtle import Turtle, Screen


# t = Turtle(shape="turtle")
# t.color("red") 

# for x in range(4):
#     t.forward(100)
#     t.right(90)


# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)




# screen = Screen()
# screen.exitonclick()




# ora aggiungo random e tolgo i valori fissi 
from turtle import Turtle, Screen
from random import randint 


screen = Screen()
screen.setup(width = 500, height = 400)
puntata = screen.textinput(title = "puntata", prompt = "su chi vuoi  puntare: ")
print(puntata)

colori = ["red", "orange", "yellow", "green", "blue", "purple"]                
pos_y = [0, -25, -50, 25, 50, 75]    
              

turtles = [ ] 
for num in range(6):
    t = Turtle(shape="turtle")
    t.color(colori[num])
    t.penup()
    t.goto (x = -240, y = pos_y[num])
    turtles.append(t)

start = True 
for i in range(80):
    for turtle in turtles:
        if turtle.xcor() >230:
            start = False 
            if puntata == turtle.pencolor():
                print("hai vinto")
            else:
                print("hai perso")
        turtle.forward(randint(0,10))

        

screen = Screen()
screen.exitonclick()



# for x in range(20):
#     t.forward(randint(20,50))
#     t.right(randint(0,360)) 




