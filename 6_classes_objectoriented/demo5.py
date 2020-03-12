class A:
    def __init__(self,name):   # constructor for python
         self.name = name
         print(self.name)
    def sayHello(self):
         print("I'm okay")
    def sayHi(self,value):
         self.value = value
         print("you entered :", self.value)

print("Outside function")

if __name__ == "__main__":
    print("Inside condition")
    print(__name__)
    x = A("python")
    x.sayHello()
    x.sayHi("Giri")



