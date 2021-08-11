class Product:
    """Common base class for all Products"""
    price: object
    pcount = 0  # class variable shared by all instances

    def __init__(self, pid, pname , price , stock):  # constructor
        self.stock = stock
        self.pid = pid  # instance variable unique to each instance
        self.pname = pname
        self.price = price
        Product.pcount += 1

    def calTotalPrice(self):
        print('Total price =')
        print(self.price + 0.12*self.price)
    def DisplayStock(self):
        print('Stock size is =')
        print(self.stock)

prd1 = Product(2,'oil',100,10)
prd1.calTotalPrice()
prd1.DisplayStock()
prd2 = Product(3,'atta',1000,100)
prd2.calTotalPrice()
prd2.DisplayStock()