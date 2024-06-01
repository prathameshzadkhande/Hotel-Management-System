import os
from hotel import Hotel
from customer import Customer
from datetime import datetime

# to import the Admin hotel functions 
c1 = Hotel()

# create the user hotel class
class User_hotel:
    def search_room_by_type(self, room_type):   # for searching the room is available or not 
        if os.path.exists("Hotel_Rooms.txt"):
            room_found = False  
            with open("Hotel_Rooms.txt", "r") as fp:   
                for room in fp:
                    if room_type in room:
                        rm = room.split(',')
                        if rm[2] == '1' and rm[1]==room_type :  
                            rm_no = rm[0]
                            print("Room is Available")
                            c1.editRoomSlot(rm_no,0)
                            self.Customer_details(rm_no)  
                            print(f"Room Number : {rm_no} is Alloted")
                            room_found = True  
                            break  
                if not room_found:  
                    print("Room is not Available")
        else: 
            print("The desired file does not exist")

    def Customer_details(self,rm_no): # imported these class from Customer module
        name = input("Enter Your name : ")
        city = input("Enter Your City Name : ")
        mob =  input("Enter the Moblie Number :")
        date = input("Enter Date in yyyy-mm-dd :")
        self.room_no = rm_no
        c1 = Customer(name,city,mob,date,self.room_no)
        with open("Hotel_cust.txt","a") as fp:
            fp.write(f"{c1} \n")


    
    def check_out(self):  # Modified method to include date validation
        rm_no = input("Enter your Room No: ")
        out_date = input("Enter Check Out Date in yyyy-mm-dd: ")

        if os.path.exists("Hotel_cust.txt"):
            cust_found = False
            with open('Hotel_cust.txt', 'r') as rd:
                for cust in rd:
                    if rm_no in cust:
                        cm = cust.split(',')
                        
                        book_d = datetime.strptime(cm[3], '%Y-%m-%d')
                        check_out_date = datetime.strptime(out_date, '%Y-%m-%d')
                        
                        if check_out_date < book_d:  # Validate check-out date against booking date
                            print("Invalid check-out date. It must be later than the booking date.")
                            return  # Return to avoid further processing if date is invalid

                        diff = check_out_date - book_d
                        days = diff.days
                        print(f"Number of days stayed: {days}")
                        self.bill(days, rm_no)
                        c1.editRoomSlot(rm_no, 1)
                        cust_found = True
                        break
                        
                if not cust_found:
                    print("Invalid Room ID")
        else:
            print("The Desired File Does Not Exist")

    

    def bill(self, day, rno):   # to generate the bill
     if os.path.exists("Hotel_Rooms.txt"):
        
        with open("Hotel_Rooms.txt", "r") as fp:
            for room in fp:
                if rno in room:
                    rm = room.split(",")
                    per_day = int(rm[3])  # Convert the per_day to an integer
                    ex_charge = int(input("Enter the Amount of Additional Hotel Charges : "))
                    gst = per_day // 10  # Calculate extra charges per day
                    total_bill = day * per_day + gst * day + ex_charge  # Calculate total bill
                    print(f"""
                          {'='*40}
                           \t  Total Days Stay           : {day}
                           \t  Room Number               : {rno}
                           \t  Room Type                 : {rm[1]}
                           \t  Room Rent Per Day         : {per_day}
                           \t  GST Per Day               : {gst}
                          {'-'*40}
                           \t  Your Total Bill            : {total_bill}
                          {'='*40}
                         """)
                    inp = input("Press 1 to Pay: ")
                    if inp == '1':
                        print(f"Amount {total_bill} has been paid successfully.")
                        print("Thank you for your payment. Visit Again!")
                        self.deleteCustById(rno)         # when the payment is successfull we delete the customer data
                    else:
                        print("Wrong entry. Please press 1.")
     else:
        print("The desired file could not exist")


    def deleteCustById(self,cid):  # to delete the customer data
        if os.path.exists("Hotel_cust.txt"):
            allcust = []
            found = False
            with open("Hotel_cust.txt","r") as fp:                
                for cust in fp:
                    if str(cid) not in cust:
                        allcust.append(cust)
                    else:
                        found = True                      
               
            
            if found: #Record is present so we need to delete it
                with open("Hotel_cust.txt","w") as fp:
                    for cust in allcust:
                        fp.write(cust)
            else:
                print("Customer you want to delete is not present")
               
        else:
            print("The desired file does not exist")




