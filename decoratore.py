

# pensiamo all'analogia con un albero di natale e vogliamo aggiungere una stella quindi vogliamo decorare la nostra funzione originale 

# def func_decoratore(func_originale):
#     def wrapper(): 
#         print("io vorrei aggiungere una stella")
#         func_originale()
#         print("ho aggiunto la stella")
#     return wrapper 

# def albero ():
#     print("io sono un albero")    

# albero = func_decoratore(albero)

# albero()


# ottengo lo stesso facendo cosi :

# def func_decoratore(func_originale):
#     def wrapper():
#         print("io vorrei aggiungere una stella")
#         func_originale()
#         print("ho aggiunto la stella")
#     return wrapper

# @func_decoratore

# def albero():
#     print("io sono un albero")


# @func_decoratore

# def presepe():
#     print("io sono un presepe")




# albero()
# presepe()  



# decoratori con argomenti 

# def func_decoratore(func_originale):
#     def wrapper(*args, **kwargs):
#         print("io vorrei aggiungere una stella")
#         func_originale(*args, **kwargs)
#         print("ho aggiunto la stella")
#     return wrapper


# @func_decoratore
# def albero(colore):
#     print(f"io sono un albero {colore}")


# albero(colore = "verde")



# decoratori esempio pratico (timer)

from time import perf_counter 


def func(a,b):

    return a*b 

start = perf_counter()
func(10,10)

stop = perf_counter()

print(stop - start)


# metodi statici ??




# metodi __str__ e __repr__
# __str__: per fornire una rappresentazione di stringa del nostro oggetto facilmente comprensibile "informazioni user friendly"
# __repr__: per fornire "informazioni tecniche" utili al programmatore: di solito informazioni su come creare una istanza 


class SquadraCalcio ():
    def __init__(self, nome, città):
        self.nome = nome
        self.città = città
        


    def __str__(self):
        return f" Squadra'{self.nome}' della città : '{self.città}' "

    def __repr__(self):
        return f" SquadraCalcio('{self.nome}', '{self.città}') "  
    
s1 = SquadraCalcio("inter", "milano")

print(s1)

print(repr(s1))