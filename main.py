Hotel_rooms={'A01':"Available",'A02':"Available",'A03':"Available",'A04':"Available",
             'A05':"Available",'B01':"Available",'B02':"Available",'B03':"Available",
             'B04':"Available",'B05':"Available",'C01':"Available",'C02':"Available",
             'C03':"Available",'C04':"Available",'C05':"Available"}
def welcome():
  print("Welcome to Cherish hotels")
welcome()
def fuct():
  print("1, Book room")
  print("2, checkout room")
  print("3, show rooms")
def book_room():
    found=False
    for room in Hotel_rooms:
        if Hotel_rooms[room]=="Available":
          name=input("Enter the customer name ::")
          phone=input("Enter the phone number of the customer ::")
          aadhar=input("Enter the aadhar number of the customer ::")
          Hotel_rooms[room]=[name,phone,aadhar]
          print("Room",room,"has been booked successfully")
          found=True
          break
    if found==False:
        print("All rooms are booked")
        
def checkout_room():
  room_num=input("Enter room number to be checkout ::")
  if room_num in Hotel_rooms:
      if Hotel_rooms[room_num]=="Available":
          print("Room is already available")
      else:
          Hotel_rooms[room_num]="Available"
          print(room_num,"is now available")
          
  else:
      print("Wrong room number entered")
def show_room():
  print("List of all rooms availability")
  for room in Hotel_rooms:
      if Hotel_rooms[room]=="Available":
          print(room,"::",Hotel_rooms[room])
      else:
          print(room,"::","Booked")
while True:
  fuct()
  choice=input('''Enter number alternative to the fuction to be performed(1(Book room)),(2(Checkout room)),(3(Show room))''')
  if choice=="1":
    book_room()
  elif choice=="2":
    check_room()
  elif choice=="3":
    show_room()
  else:
    print("Entered wrong value please try again")
  choice_con=input("Do you want to continue ??(yes/no)::")
  if choice_con=="yes":
    continue
  else:
    print("Thank you visit our hotel")
    break 
    
  




  
    
  



