

# utilizziamo queste keyword per "modificare" la gerarchia nella regola LEGB
# global: permette di mofidicare una variabile globale tramire modifiche alla variabile a livello locale 

# a = 10 
# def func():
#     global a 
#     a = 5 
#     return a 

# print(a)
# print(func())
# print(a)

# ottengo 10 5 5 

# nonlocal: ha lo stesso effetto di global ma viene utilizzato nell'enclosing namespace  (scope)

# def enclosing_func():
#     x = 1 
#     def func_interna():

#         x = 100
#     func_interna()
#     return x 
# print(enclosing_func()) # 1


# # ora modifico il codice per far si che x = 100 non sia piu locale alla funzione ma viva nel namespace enclosing 
# def enclosing_func():
#     x = 1
#     def func_interna():
#         nonlocal x # x non e piu local alla funzione interna 
#         x = 100

#     func_interna()
#     return x
# print(enclosing_func()) # 100



# esercizi :

# a = 10 
# def func():
#     print(a)
#     return None 

# func()


# a = 10

# def func():
#     #global a 
#     a = 5
#     print(a)
#     a = 'ciao' 
#     print(a)

# print(a)
# func()
# print(a)




