def menu():
    print("-----------menu-----------\n")#this prints the menu of the bus company
    print("1.Bus booking status\n2.Bus booking\n3.Booking payment\n4.Booking report\n5.Sign out")
        
    choice=int(input("enter your choice"))
    while choice==4 or choice==1:#repeats the statement when wrong credentials are entered
        choice=int(input("please enter 2,3,5"))
    return choice    