#creating a class named MyClass
class MyClass:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    #object method
    def myfunc(self):
        print("Hello my name is " + self.name)            

#creating an object of the class
p1=MyClass("john", 35)

#modify object
p1.age=40

print(p1.name)
print(p1.age)

p1.myfunc()   #calling the method


#inheritance
class Student(MyClass):
  def __init__(self, name, age):
    MyClass.__init__(self, name, age)

x = Student("Mike", 35)
x.myfunc()

