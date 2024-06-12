# a = [1,2,3,4,5]
# print(type(a))
# b= a.__iter__()
# print(b)
# b.__next__()
# print(b.__next__())

# a={1:'a', 2:'b'}
# b=iter(a)
# print(next(b))


# class Simple:
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return 1
#         else:
#             raise StopIteration
#
# foo = Simple(5)
# for i in foo:
#     print(i)


# a = [1, 2, 3]
# b = [i + 10 for i in a]
# print(b)

# a = (i for i in range(2,8))
# print(a)
# for i in a:
#     print(i)

# def func(start, finish):
#     while start < finish:
#         yield start * 0.33
#         start += 1
# a = func(1,4)
# print(a)
# for i in a:
#     print(i)

# class AP:
#     def __init__(self,a1,d,size):
#         self.ele=a1
#         self.diff=d
#         self.len=size
#         self.count=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.count >= self.len:
#             raise StopIteration
#         elif self.count == 0:
#             self.count +=1
#             return self.ele
#         else:
#             self.ele +=self.diff
#             self.count +=1
#             return self.ele
#

# def foo():
#     x=2
#     print('первый yeild')
#     yield x
#
#     x += 1
#     print('второй yeild')
#     yield x
#
#     x += 1
#     print('третий yeild')
#     yield x
# iter=foo()

# class Fib:
#     def __init__(self,max_value):
#         self.max_value= max_value
#         self.a, self.b = 0,1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         fib = self.a
#         if fib > self.max_value:
#             raise StopIteration
#         self.a, self.b = self.b,self.a+self.b
#         return fib
# class Fib2:
#     def __init__(self,max_value):
#         self.max_value=max_value
#     def __iter__(self):
#         return Fib(self.max_value)
# max_number=int(input())
# fib_s=Fib2(max_number)
# for i in fib_s:
#     print(i)


# def cycle(n):
#     i = 0
#     while True:
#         yield i % n + 1
#         i += 1
# num= int(input())
# gen= cycle(num)
# for _ in range(num*5):
#     print(next(gen))

# class EvenNumbers:
#     def __init__(self, n):
#         self.n = n
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         result = self.n
#         self.n += 2
#         return result
# even = EvenNumbers(0)
# for i in even:
#     print(i)

# class EvenNumbers:
#     def __init__(self,n):
#         self.n=0
#
#     def generate(self):
#         while True:
#             yield self.n
#             self.n+=2
# even=EvenNumbers(0)
# for i in even.generate():
#     print(i)

# class Animal:
#     def __init__(self,eat,sleep,communicate):
#         self.eat=eat
#         self.sleep=sleep
#         self.comminicate = communicate
# class Dog(Animal):
#     def __init__(self,bark,fetch):
#         super().__init__(bark,fetch)
#         self.bark=bark
#         self.fetch=fetch
# animal=Dog(bark=True,fetch=True)
# print(animal.eat)
# print(animal.sleep)
# print(animal.comminicate)
# print(animal.bark)
# print(animal.fetch)


# class Shape:
#     def __init__(self,area,perimetr,draw):
#         self.area=area
#         self.perimetr=perimetr
#         self.draw=draw
# class Rectangle(Shape):
#     def __init__(self,width,height):
#         super().__init__(width*height,2*width+2*height,True)
#         self.width=width
#         self.height=height
#
#
# class Circle(Shape):
#     def __init__(self,radius):
#         super().__init__(3.14*radius**2,2*3.14*radius,True)
#         self.radius=radius
# rectangle=Rectangle(4,4)
# print(rectangle.area)
# print(rectangle.perimetr)
# print(rectangle.draw)
# circle=Circle(4)
# print(circle.area)
# print(circle.perimetr)
# print(circle.draw)

# class Employee:
#     def __init__(self,get_salary,get_position,work):
#         self.get_salary=get_salary
#         self.get_position=get_position
#         self.work=work
# class Manager(Employee):
#     def __init__(self,get_salary,get_position,work):
#         super().__init__(get_salary,get_position,work)
#         self.get_salary=get_salary
#         self.get_position=get_position
#         self.work=work
# class Developer(Employee):
#     def __init__(self,manage_team,write_code):
#         super().__init__(manage_team,write_code,True)
#         self.manage_team=manage_team
#         self.write_code=write_code
#         self.work=True
# manager=Manager(1000,'Manager',True)
# print(manager.get_salary)
# print(manager.get_position)
# print(manager.work)
# developer=Developer(1000,True,)
# print(developer.get_salary)
# print(developer.get_position)
# print(developer.work)

# class DataSource:
#     def fetch_data(self):
#         pass
#
# class Base:
#     def fetch_data(self):
#         print("a")
#
# class File:
#     def fetch_data(self):
#         print("b")
#
# class Network:
#     def fetch_data(self, c):
#         print(c)



# class Vehicle:
#     def __init__(self,start,stop,move):
#         self.start=start
#         self.stop=stop
#         self.move=move
# class Car(Vehicle):
#     def __init__(self,start,stop,move,drive,pedal):
#         super().__init__(start,stop,move)
#         self.start=start
#         self.stop=stop
#         self.move=move
#         self.drive=drive
#         self.pedal=pedal
# class Bicycle(Vehicle):
#     def __init__(self,start,stop,move,drive,pedal):
#         super().__init__(start, stop, move)
#         self.start=start
#         self.stop=stop
#         self.move=move
#         self.drive=drive
#         self.pedal=pedal
# car=Car(1,2,3)
# print(car.start)
# print(car.stop)
# print(car.move)
# print(car.drive)
# print(car.pedal)
# bicycle=Bicycle(1,2,3)
# print(bicycle.start)
# print(bicycle.stop)
# print(bicycle.move)
# print(bicycle.drive)
# print(bicycle.pedal)



# class Book:
#     def __init__(self,read,write,info):
#         self.read=read
#         self.write=write
#         self.info=info
# class Novel(Book):
#     def __init__(self,read,write,info,plot,subject):
#         super().__init__(read,write,info)
#         self.plot=plot
#         self.subject=subject
#         self.read=read
#         self.write=write
#         self.info=info
#         self.plot=plot
#         self.subject=subject
# class TextBook(Book):
#     def __init__(self,read,write,info,subject,plot,)
#         super().__init__(read,write,info)
#         self.subject=subject
#         self.read=read
#         self.write=write
#         self.info=info
#         self.subject=subject
#         self.plot=plot
# novel=Novel(read=True,write=True,info=True,plot=True,subject=True)
# print(novel.read)
# print(novel.write)
# print(novel.info)
# print(novel.plot)
# print(novel.subject)
# textbook=TextBook(read=True,write=True,info=True,subject=True,plot=True)
# print(textbook.read)
# print(textbook.write)
# print(textbook.info)
# print(textbook.subject)
# print(textbook.plot)

# class Logger(ABC):
#     @abstractmethod
#     def log(self,message):
#         pass
# class ConsoleLogger(Logger):
#     def log(self,message):
#         print(message)
# class FileLogger(Logger):
#     def log(self,message):
#         with open('log.txt''w')as f:
#             f.write(message)
#             f.close()
# class EmailLogger(Logger):
#     def log(self,message):
#         with open('log''w')as f:
#             f.write(message)
#             f.close()
# console_l=ConsoleLogger()
# file_l=FileLogger()
# email_l=EmailLogger()
# console_l.log('hello')
# file_l.log('hello')
# email.log('hello')


# class GeometricShapes(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#         self.area = 3.14 * radius ** 2
#         self.perimeter = 2 * 3.14 * radius
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.area = width * height
#         self.perimeter = 2 * (width + height)
#
# class Triangle:
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#         self.area = 0.5 * base * height
#         # Assuming equilateral triangle for simplicity in perimeter calculation
#         self.perimeter = 3 * base
#
# circle = Circle(4)
# print("Circle Area:", circle.area)
# print("Circle Perimeter:", circle.perimeter)
#
# rectangle = Rectangle(4, 4)
# print("Rectangle Area:", rectangle.area)
# print("Rectangle Perimeter:", rectangle.perimeter)
#
# triangle = Triangle(4, 4)
# print("Triangle Area:", triangle.area)
# print("Triangle Perimeter:", triangle.perimeter)



# class DataType(ABC):
#     @abstractmethod
#     def process(self):
#         pass
# class Number(DataType):
#     def __init__(self,number):
#         self.number=number
#     def process(self):
#         return self.number
# class String(DataType):
#     def __init__(self,string):
#         self.string=string
#     def process(self):
#         return self.string
# class Lists(DataType):
#     def __init__(self,list):
#         self.list=list
#     def process(self):
#         return self.list
# number=Number(10)
# print(number.process())
# string=String('hello')
# print(string.process())
# list=Lists([1,2,3,4,5,6,7])
# print(list.process())



# class System(ABC):
#     @abstractmethod
#     def fetch_data(self):
#         pass
#
# class DataBase(System):
#     def fetch_data(self):
#         print("ф")
#
# class FileSystem(System):
#     def fetch_data(self):
#         print("ы")
#
# class Network(System):
#     def fetch_data(self):
#         print("в")
#
# data = DataBase()
# file = FileSystem()
# network = Network()
# data.fetch_data()
# file.fetch_data()
# network.fetch_data()






import itertools
def permute(nums):
    return list(itertools.permutations(nums))
nums = [1, 2, 3]
print(permute(nums))