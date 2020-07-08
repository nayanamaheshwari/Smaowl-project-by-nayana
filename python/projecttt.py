distmn=500
distmp=300
distmd=600
distmk=500
pkbc=8000
pkec=5000
print("welcome to Nayana Airways")
print("Hello user,we have flights going from Mumbai to Nagpur, Mumbai to Pune,Mumbai to Delhi and Mumbai to Kolkata  ")
print("1.Mumbai to Pune")
print("2.Mumbai to Nagpur")
print("3.Mumbai to Delhi")
print("4.Mumbai to Kolkata")
ch=int(input("ENTER YOUR CHOICE"))
if(ch==1):
       seattype=input("ENTER SEAT TYPE(BUSINESS/ECONOMY)")
       nopass=int(input("ENTER THE NUMBER OF PASSENGERS"))
       for i in range (1,nopass+1):
            print("ENTER NAME OF PASSENGER ",i)
            name=input()
            print("ENTER AGE OF PASSENGER",i)
            age=input()
       if(seattype=="business class"):
            fare=nopass*distmp*pkbc
            print("fare", fare)
       elif(seattype=="economy class"):
            fare=nopass*distmp*pkec
            print("fare", fare)

elif(ch==2):
       seattype=input("ENTER SEAT TYPE(BUSINESS/ECONOMY")
       nopass=int(input("ENTER THE NUMBER OF PASSENGERS"))
       for i in range (1,nopass+1):
                    print("ENTER NAME OF PASSENGER ",i)
                    name=input( )
                    print("ENTER AGE OF PASSENGER",i)
                    age=input( )
       if(seattype=="business class"):
             fare=nopass*distmn*pkbc
             print("fare", fare)
       elif(seattype=="economy class"):
            fare=nopass*distmn*pkec
            print("fare", fare)



if(ch==3):
       seattype=input("ENTER SEAT TYPE(BUSINESS/ECONOMY")
       nopass=int(input("ENTER THE NUMBER OF PASSENGERS"))
       for i in range (1,nopass+1):
                    print("ENTER NAME OF PASSENGER ",i)
                    name=input( )
                    print("ENTER AGE OF PASSENGER",i)
                    age=input( )
       if(seattype=="business class"):
             fare=nopass*distmd*pkbc
             print("fare", fare)
       elif(seattype=="economy class"):
            fare=nopass*distmd*pkec
            print("fare", fare)

elif(ch==4):
       seattype=input("ENTER SEAT TYPE(BUSINESS/ECONOMY")
       nopass=int(input("ENTER THE NUMBER OF PASSENGERS"))
       for i in range (1,nopass+1):
                    print("ENTER NAME OF PASSENGER ",i)
                    name=input( )
                    print("ENTER AGE OF PASSENGER",i)
                    age=input( )
       if(seattype=="business class"):
             fare=nopass*distmk*pkbc
             print("fare", fare)
       elif(seattype=="economy class"):
            fare=nopass*distmk*pkec
            print("fare", fare)


     
            

