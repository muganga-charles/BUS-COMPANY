
import credentials
import payment
import menu
import Bus_booking,Bill
username=''
credentials.username(username)
password=''
credentials.password(password)
print('Thank you for signing up')
import menu
m=menu.menu()
if m==2:
        n=Bus_booking.booking()
        o=Bus_booking.bus_type()  
        p=Bill.amount(o,n)
        print(p ,"is the total amount")
        print("Thank you for booking")
        q=payment.three(p)
elif m==3:
    print("You have not booked yet\nplease restart the program and go to bus bookig first(option 2)")
    print("You have signed out")

elif m==5:
    print("You have signed out")
    take=False


