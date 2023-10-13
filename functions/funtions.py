"==================Функции==============="
# именованный блок кода, который может принимать аргументы и возвращать результат

# def func(x:int,y:int,c:int)-> None: # параметры
#     """
#     This function return x+y
#     """
#     return x + y # возвращаю результат
# func(5,4,6) # аргументы 

""" DRY - don`t repeat yourself """ 

# print(["1"].append("2")) # none

# def pif(x:int, y:int, z:int):
#     return (x**2 + y**2)**0.5

# print(pif(5,4,3))

# def my_len(x:str):
#     counter = 0
#     for i in x:
#         counter +=1
#     return counter

# print(my_len("safdsaf"))

# def func():
#     try:
#         return 0
#     finally:
#         return 1
    
# print(func()) # 1

# return value = 0
# return value = 1 

"======================Аргументы и параметры======================"
# параметры - переменные внутри функции, хначения которые мы задаем при вызове функции
# аргументы - значения, которые мы передаем при вызове функции

"======================Виды параметров============================"
# 1.Обязательные параметры
# 2.НЕ обязательные
# 2.1 по умолчанию(с дефолтом)
# 2.2 args (все позиционные аргументы в виде кортеже)
# 2.3 kwargs( все именованные аргументы в словарь)


def func(a, b=3, *args, **kwargs): # b тут дефолтное значение *args как накопитель **
    print(args) # (2,4)
    print(kwargs) 
    return a + b

print(func(a = 4, b = 4, c = 3))
