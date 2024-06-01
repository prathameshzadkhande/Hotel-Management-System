from hotel import Hotel 
from room import Room

# Admin class for managing hotel rooms
class Admin:
    def __init__(self):
        choice = 0
        hotel = Hotel()
        
        while choice != 10:
            print("\n\t\t\u25BA 1. Add Room")
            print("\n\t\t\u25BA 2. Display All Rooms")
            print("\n\t\t\u25BA 3. Delete Room by Room ID")
            print("\n\t\t\u25BA 4. Update Room by Room ID")
            print("\n\t\t\u25BA 10. Exit")
            choice = int(input("Enter a choice: "))
            
            if choice == 1:
                rid = int(input("Enter The Room ID: "))
                rtype = self.room_type()
                avail = input("Enter 1 if the room is available, else 0:")
                price = int(input("Enter Room Rent: "))
                room = Room(rid, rtype, avail, price)
                hotel.add_room(room, rid)
                
            elif choice == 2:
                hotel.showAllRooms()
                
            elif choice == 3:
                inp = int(input("Enter the Room ID: "))
                hotel.deleteRoomById(inp)
                
            elif choice == 4:
                inp = int(input("Enter the Room ID: "))
                hotel.editRoomById(inp)

            elif choice == 10:
                print("-------------End of Program------------")


    def room_type(self):
      print(f"""
          ____________________________________
               These Room Type Codes 
          ------------------------------------
          \u25BA To Book Single-Bed AC Room      : AC
          \u25BA To Book Double-Bed AC Room      : D-AC
          \u25BA To Book Single-Bed Non-AC Room  : NAC
          \u25BA To Book Double-Bed Non-AC Room  : D-NAC
                """)
      while True:  # Loop until a valid choice is entered
        choice = input("Enter the Room Type Code: ").upper()
        if choice not in ['AC', 'D-AC', 'NAC', 'D-NAC']:
            print("Please Enter a Valid Code ")
        else:
            return choice

            
