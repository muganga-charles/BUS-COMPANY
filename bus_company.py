import random
def three(cost):
    print("---------Booking payment--------\n")
    receipt=input("enter receipt number")
    am=True
    while am==True:
        amount=int(input('enter amount to be payed'))
        if amount<cost:
            balance=cost-amount
            print("Balance:",balance)
            am=False
        else:
            print("enter an amount less than or equal to the cost")
            amount=int(input('enter amount to be payed'))
def five(choice):
    return 'thank you'

def main():

    password1="batlor"#the password is initialised assuming those where the registerd one
    user_name1="charles"#the user name is initialised assuming those where the registerd one
    print("enter user name")
    user_name=input("")
    print("enter password")
    password=input("")
    while user_name != user_name1 and password !=password1:#comparison of he entered credentials and the stored credentials
        user_name=input("enter username")
        password=input("enter password")
        print('enter correct user name and password')  
    while user_name != user_name1:#repeats the statement when wrong credentials are entered
        user_name=input("enter password")
    while password != password1:#repeats the statement when wrong credentials are entered
        password=input("enter password")

    print("-----------menu-----------\n")#this prints the menu of the bus company
    print("1.Bus booking status\n2.Bus booking\n3.Booking payment\n4.Booking report\n5.Sign out")
        
    choice=int(input("enter your choice"))
    while choice==4 or choice==1:#repeats the statement when wrong credentials are entered
        choice=int(input("please enter 2,3,5"))
        
    if choice==2:
        print("--------bus booking-------\n")
        seats=int(input("enter number of seats"))
        while seats>70:#repeats the statement when wrong credentials are entered
            seats=int(input("enter number of seats less than 70"))       
        bustype=int(input("enter 1.Ordinarybus\n2.Luxury bus"))              
        n=random.randint(112,9998)
        if bustype==1:
            cost=seats*25000#computes the amount for the ordinary bus
            print("Number of seats:",seats,"\n Bus type:Ordinary\nTotol cost:",cost,"\nReceipt number:OB",n)
        elif bustype==2:
            cost=seats*50000 #computes the amount for the Luxury bus
            print("Number of seats:",seats,"\n Bus type:Luxury\nTotol cost:",cost,"\nReceipt number:LB",n)
        else:
            print("enter a right bus type")  
        cost=three(cost)               
        n=five(choice)
        print(n)  
    elif choice==3:
        print("You have not booked yet\nplease restart the program and go to bus bookig first(option 2)")
        print(n)
    elif choice==5:
        print(n)   #prints the closing remarks of the program
    else:
       print("enter correct credentials")
            
main()
