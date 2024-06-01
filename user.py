from user_hotel import User_hotel

# These is User interface 

class User :
    def __init__(self) :
        hotel = User_hotel()
        choice  = 0
        while (choice!= 9) :
            choice = int(input(f'''
                                  \n\t\t\033[1m{'-'*20} Welcome to Pratham Resort {'-'*20}\033[0m
                                   \n\t\t\u25BA To Book Single-Bed AC Room      : \U0001F6CC 1
                                   \n\t\t\u25BA To Book Double-Bed AC Room      : \U0001F6CC 2
                                   \n\t\t\u25BA To Book Single-Bed Non-AC Room  : \U0001F6CB 3
                                   \n\t\t\u25BA To Book Double-Bed Non-AC Room  : \U0001F6CB 4
                                   \n\t\t\u25BA To Check out                    : \U0001F6AA 5
                                   \n\t\t\u25BA To Exit Resort Menu             : \U0000274C 9
                                   Please enter your choice        :  '''))
            if choice==1:
               inp = 'AC'
               hotel.search_room_by_type(inp)
            elif choice ==2 :
               inp = 'D-AC'
               hotel.search_room_by_type(inp)
            elif choice == 3 :
               inp = 'NAC'
               hotel.search_room_by_type(inp)
            elif choice == 4 :
               inp = 'D-NAC'
               hotel.search_room_by_type(inp)
            elif choice == 5 :
               hotel.check_out()
            else:
               print("You are Exit From menu")