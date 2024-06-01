class Customer:
    def __init__(self, name, city, mob,date,rm_no):
        self.name = name
        self.city = city
        self.mob = mob
        self.date = date
        self.room_no = rm_no

    def show_details(self):
        print(f'''
                 ----------------  Customer Details -------------
                Name          :  {self.name}
                City          :  {self.city}
                Mobile Number :  {self.mob}
                Checkin Date  :  {self.date}
                Room Number   :  {self.room_no}''')

    def __str__(self):
        return f'{self.name},{self.city},{self.mob},{self.date},{self.room_no}'
