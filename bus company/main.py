take=True
while take==True:
    print("Do you want to\n1.log in\n2.sign up\n3.exit")
    choice=int(input("Enter your choice"))
    while choice>3 or choice<1:
        print("Invalid choice")
        choice=int(input("Enter your choice"))
    if choice==1:
        import log_in
        n=log_in
    elif choice==2:
        import sign_up
        m=sign_up
    elif choice==3:
        take=False

    