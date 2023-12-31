# Инкапсуляция:
# Ограничение доступа к методам и атрибутам(сокрытие данных)
# Сбор всех методов и атрибутов в одну капсулу(класс)

# 3 модификатора доступа
# public (публичный) используем где угодно  
# private (защищенный) использаем внутри классов
# protected (приватный) используем только в одном классе, в котором его создали

class A:
    public = 'публичный'
    _protected = "защищенный"
    __private = 'приватный'

    def public_func(self):
        self.__private_func()
    def _protected_func(self):
        pass
    def __private_func(self):
        pass

a = A()
a.public
print(a._protected) # мы не должны обращатся к защищенному атрибуту или методу через объект класса (на уровне соглашения)
#print(a.__private) # AttributeError: 'A' object has no attribute '__private'
# к приватному атрибуту я не могу обратится через объект и через дочерний класс
# _<название класса>__<название метода или атрибута> (так нельзя на уровне соглашения)

class B(A):
    def func(self):
        self.public
        self.__private_func()

b = B()
# b.func() не можем обратится к приватному методу.
print(b._A__private) # (так нельзя на уровне соглашения) 

class Person:
    name = 'Nikita'
    __last_name = 'Grebnev'

    def get_last_name(self):
        # return f"My name is {self.name}, My last name is {self.__last_name}" # так можем обращатся к приватному атрибуту (обращаемся через методы)
        return self.__last_name
    
    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name # так можем изменить приватный атрибут легальным способом
    

    
human = Person()
# human._Person__last_name = "Zhoroev" # (так нельзя на уровне соглашения)
# print(human.get_last_name())
# human.set_last_name("Zhoroev")
# print(human.get_last_name())


class Game:
    __level = 1
 
    # def get_level(self):
    #     return self.__level
    
    # def change_level(self, new_level):
    #     self.__level = new_level

    @property # декоратор, который превращает метод в атрибут
    def level(self):
        return self.__level
    
    @level.setter # позволяет изменить атрибут
    #__setattr__ - 
    def level(self, n):
        self.__level = n
    

g = Game()
# print(g.get_level())
# g.change_level(5)
# print(g.get_level())
# print(g._Game__level)
# g._Game__level = 90
# print(g._Game__level)
# print(g.level)
# g.level = 90
# print(g.level)

# property | getter


class Human:
    def __init__(self, name, age, last_name):
        self._name = name
        self.__age = age
        self.last_name = last_name

    @property
    def age(self):
        return self.__age
    
    @age.setter # срабатывает при использование = += -= *=
    def age(self, n):
        self.__age = n

human = Human("name", 78, "last_name")
# print(human.age)
# human.age = 7
# print(human.age)

# _create_user
# create_user
# create_superuser


# class A:
#     _a = 7
    # getter - переопределяет маг. метод __getattribute__
    # setter - переопределяет магюметод __setattr__
    # deletter - переопределяет маг. метод __delattr__
     

# a = A()
# print(a._a)
# print(a.__getattribute__("_a"))
# a._a = 5
# "||"
# a.__setattr__('_a', 5)
# print(a.__getattribute__("_a"))
# a.__setattr__("a", 6)
# "||"
# a.a = 10
# a.__delattr__("a")
# print(a.__getattribute__("a"))

class Human:
    def __init__(self,name) -> None:
        self.__name = name
    @property
    def name(self):
        return self.__name
    
    @name.deleter # срабатывает когда мы пишем оператор "del"
    def name(self):
        del self.__name

# human = Human("Nikita")
# del human.name
# print(human.name)
        

class Temp:
    
    def __init__(self, target_temp) -> None:
        self.__target_temp = target_temp
        self.__default_temp = 10 
        self.doiti_do_target_temp()

    def add_temp(self):
        self.__default_temp += 1
        if self.__default_temp == self.__target_temp:
            return "Вы достигли до плановой задачи"

    def minus_temp(self):
        self.__default_temp -= 1
        if self.__default_temp == self.__target_temp:
            return "Вы достигли до плановой задачи"
    
    def get_temp(self):
        return f"{self.__default_temp} - {self.counter} вызвали метод {self.method}"

    def doiti_do_target_temp(self):
        self.counter = 0
        if self.__default_temp < self.__target_temp:
            while self.__default_temp != self.__target_temp:
                self.add_temp()
                self.method  = self.add_temp.__name__
                self.counter += 1
            
        elif self.__default_temp > self.__target_temp:
            while self.__default_temp != self.__target_temp:
                self.minus_temp()
                self.method = self.minus_temp.__name__
                self.counter += 1
        else:
            self.counter = 0
            self.method = "ни разу, температуры равны"

temp = Temp(20)
print(temp.get_temp())

    

        

