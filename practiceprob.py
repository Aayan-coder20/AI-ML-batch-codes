class Product: 
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def get_info(self):
        print(f"Price of {self.name} is {self.price}")


pro1 = Product("Laptop",50_000)
pro2 = Product("Mobile",40_000)
pro3 = Product("iPad",25_000)

pro1.get_info()
pro2.get_info()
       