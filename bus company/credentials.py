import re


def username(username):
    temp=[]
    user_name=input("enter username")
    user_name=user_name.lower()
    temp.append(user_name)
    return temp
    
def password(password):
    tmp=[]
    password=input("enter password")
    tmp.append(password)
    return tmp

def username1(username):
    temp=[]
    for i in temp:
        if i in username:
            print("")
def password1(password):
    temp=[]
    for i in temp:
        if i in password:
            print("welcome")  
    return temp