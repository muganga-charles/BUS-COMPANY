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