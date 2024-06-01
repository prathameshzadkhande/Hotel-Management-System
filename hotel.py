from exception import room_exist_err


import os
class Hotel:
    def add_room(self,e,rid):
        with open("Hotel_Rooms.txt","a") as fp:
            if self.check_room(rid) == True:
                print("Add other Room")
            else:
                fp.write(str(e)+ "\n")

    def showAllRooms(self):
        
        if os.path.exists("Hotel_Rooms.txt"):
         with open("Hotel_Rooms.txt", "r") as fp:
            data = fp.readlines()

            if len(data) == 0:
                print("The file is empty.")
            else:
                print(f"{'='*10} Hotel Rooms Information{'='*10}\n")
                for line in data:
                    room_details = line.strip().split(",")
                    room_number = room_details[0]
                    room_type = room_details[1]
                    available = room_details[2]
                    price = room_details[3]

                    print(f"Room {room_number}" ,end=" |")
                    print(f" Type  : {room_type}",end=" |")
                    print(f" Available : { available} ",end=" |")
                    print(f" Price  : {price}",end=" |" )

                    print("\n")
        else:
            print("The desired file does not exist")

    def deleteRoomById(self,rid):
        file_path = "Hotel_Rooms.txt"
    
        if os.path.exists(file_path):
           temp_room_data = []
           room_found = False
        
           with open(file_path, "r") as file:
            for room in file:
                if str(rid) not in room.strip():  
                    temp_room_data.append(room)
                else:
                    room_found = True
        
            if room_found:
                with open(file_path, "w") as file:
                    for room in temp_room_data:
                        file.write(room)
                print("Room with ID", rid, "has been successfully deleted.")
            else:
                print("Room with ID", rid, "was not found in the records.")
        else:
             print("The specified file does not exist.")


    def editRoomById(self,rid):
        if os.path.exists("Hotel_Rooms.txt"):
            allroom = []
            found = False
            with open("Hotel_Rooms.txt","r") as fp:
                for room in fp:
                    if str(rid) in room:
                        room = room.split(",")
                        ans = input("Do you wish to edit Room Type (y/n)?")
                        if ans.lower() == "y" :
                            room[1] = input("Enter new Room Type : ")
                        ans = input("Do you wish to edit Price (y/n)?")
                        if ans.lower() == "y" :
                            room[3] = input("Enter new Price : ")
                            room[3]+="\n"
                        room = ",".join(room)
                        found = True
                    allroom.append(room)
                
            if found: #Record is present so we need to edit it
                with open("Hotel_Rooms.txt","w") as fp:
                    for room in allroom:
                        fp.write(room)
            else:
                print("Room you want to Update is not present")
            

        else:
            print("Hotel is not present")

    def editRoomSlot(self,rid,code):
        if os.path.exists("Hotel_Rooms.txt"):
            allroom = []
            found = False
            with open("Hotel_Rooms.txt","r") as fp:
                for room in fp:
                    if str(rid) in room:
                        room = room.split(",")
                        inp = str(code)
                        room[2] = inp
                        room = ",".join(room)
                        found = True
                    allroom.append(room)
                
            if found: #Record is present so we need to edit it
                with open("Hotel_Rooms.txt","w") as fp:
                    for room in allroom:
                        fp.write(room)
            else:
                print("Room you want to Update is not present")

    def check_room(self,rid):
        try:
            if os.path.exists("Hotel_Rooms.txt"):
               with open("Hotel_Rooms.txt","r") as fp:
                  for room in fp:
                      if str(rid) in room:
                          raise room_exist_err(rid) 
                          
                      else:
                          pass
        except room_exist_err as r :
            print(r)
            return True
        except FileNotFoundError :
            print("The file 'Hotel_Rooms.txt' does not exist")






        