def booking():
    print("--------bus booking-------\n")
    seats=int(input("enter number of seats\n"))
    while seats>70:#repeats the statement when wrong credentials are entered
        seats=int(input("enter number of seats less than 70\n"))        
    return seats         

def bus_type():
    bustype=int(input("enter 1.Ordinarybus\n2.Luxury bus\n"))   
    while bustype>2 or bustype<1:#repeats the statement when wrong credentials are entered
        print("please enter 1 or 2\n")
        bustype=int(input("enter 1.Ordinarybus\n2.Luxury bus"))
    return bustype