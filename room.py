class Room:
    def __init__(self,rid,rtype,available,price) :
        self.rid= rid
        self.rtype = rtype 
        self.available = available
        self.price = price

    def display(self):
        print(f""" 
                Room ID : {self.rid}
                Room Type : {self.rtype}
                Available : {self.available}
                Price     : {self.price}
                                        """)
        
    def __str__(self):
        data = str(self.rid)+","+self.rtype+","+str(self.available)+","+str(self.price)
        return data