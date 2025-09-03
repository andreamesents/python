
# proggettino snake 

# crea la nostra finestra 
# crea snake e fallo muovere (giu su destra sinistra) 
# crea il cibo per snake e fallo crescere ogni volta che lo mangia
# fermare il gioco ogni volta che lo snake tocca gli estremi della schermata 
# come tenere traccia del punteggio 



from turtle import Turtle, Screen 

from time import sleep

from random import randint 


from time import time, sleep
# ho aggiunto il tempo con copilot :)) 


screen = Screen() 
screen.setup(600,600)
screen.tracer(0)
posizioni = [(0,0),(-20,0), (-40,0)]


snake = []
for pos in posizioni: 
   
    s = Turtle("square")
    s.penup()
    s.goto(pos)
    snake.append(s) 
    
# creiamo il cibo 
food = Turtle("circle") 
food.color("blue") 
# creo coordinate random per il cibo
x_food = randint(-280,280)
y_food = randint(-280,280)
food.penup()
food.goto(x_food, y_food)

punti = 0    
score = Turtle ()
score.penup()
score.hideturtle()
score.goto(0,270)
score.write(f"Score: {punti}", align="center", font=("Arial", 22, "normal"))



start_time = time()
timer = Turtle () 
timer.penup() 
timer.hideturtle()
timer.goto(0, 240)




def up():
    if snake[0].heading() != 270:
        snake[0].setheading(90) # 90 gradi è su
def down():
    if snake[0].heading() != 90:
        snake[0].setheading(270) # 270 gradi è giu
def left():
    if snake[0].heading() != 0:
        snake[0].setheading(180) # 180 gradi è sinistra
def right():
    if snake[0].heading() != 180:
        snake[0].setheading(0) # 0 gradi è destra


def game_over():
    fine = Turtle()
    fine.penup()
    fine.hideturtle()
    fine.write("Game Over", align="center", font=("Arial", 22, "normal")) 


screen.listen() # aspetta che l'utente prema un tasto
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")
# ancora non le ho definite pero 
# lo farò usando setheading 

# def up():
#     snake[0].setheading(90) # 90 gradi è su
# def down():
#     snake[0].setheading(270) # 270 gradi è giu
# def left():
#     snake[0].setheading(180) # 180 gradi è sinistra
# def right():
#     snake[0].setheading(0) # 0 gradi è destra

# mi dava errore l'ho dovuto mettere sopra screen.listen()




start = True 
while start: 
     sleep(0.1)
     screen.update() 
     
     for num in range(len(snake)-1,0,-1):
        x = snake[num-1].xcor()
        y = snake[num-1].ycor()
        snake[num].goto(x,y)
     snake[0].forward(20)
        # snake[0].left(20)  # questo posso rimuoverlo cosi da adesso posso muoverlo con le 4 frecce 
     elapsed_time = int(time() - start_time)
     timer.clear() 
     if elapsed_time >= 60:
         minuti = elapsed_time // 60
         secondi = elapsed_time % 60
         timer.write(f"{minuti} minuto{'i' if minuti > 1 else ''} e {secondi} secondi", align="center", font=("Arial", 13, "normal"))
     else:
            timer.write(f"{elapsed_time} secondi", align="center", font=("Arial", 13, "normal"))
            
     
    
    # collisioni con bordo 
     if snake[0].xcor() > 290 or snake[0].xcor() < -290 or snake[0].ycor() > 280 or snake[0].ycor() < -280:
        start = False 
        game_over()

     # collisioni con se stesso 
     for q in snake[1:]:
         if q.distance (snake[0]) < 10:
             start = False 
             game_over()
     



     if snake[0].distance(food) < 15: 
         food.goto(randint(-280, 280), randint(-280, 280))

         # ora creo un'altra istanza del mio snake e la aggiungo nella coda
         quadrato = Turtle("square") 
         quadrato.penup()
         quadrato.goto(snake[-1].xcor(), snake[-1].ycor())
         snake.append(quadrato)
         punti += 1
         score.clear()
         score.write(f"Score: {punti}", align="center", font=("Arial", 22, "normal"))
     




s = Turtle("square")








screen.exitonclick() 