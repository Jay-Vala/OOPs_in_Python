#Practice Operator Overloading by Creating a class for complex numbers
class Complex():

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def getNumber(self):
        print(f"{self.real}i + {self.img}j")

    #operator overloading for add(+) operator
    def __add__(self, num2):
        new_real = self.real + num2.real
        new_img = self.img + num2.img
        return Complex(new_real, new_img)
    
    
    #operator overloading for add(-) operator
    def __sub__(self, num2):
        new_real = self.real - num2.real
        new_img = self.img - num2.img
        return Complex(new_real, new_img)
    

number1 = Complex(4,5)
number1.getNumber()

number2 = Complex(8,3)
number2.getNumber()

number3 = number1+number2
number3.getNumber()

number4 = number1-number2
number4.getNumber()



class Order():

    def __init__(self, price):
        self.price = price
    
    # Operator Overloading for Greater than operator(>)
    def __gt__(self, ord2):
        return self.price > ord2.price
        
order1 = Order(599)
order2 = Order(1999)
order3 = Order(199)

print(order1>order2)
print(order1>order3)