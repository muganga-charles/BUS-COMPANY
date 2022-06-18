
import random
def amount(bus,seats):
    
    if bus==1:
        print("Bus type:Ordinarybus\n")
        print("Receipt number: OB"+str(random.randint(1,100)))
        if seats<=20:
            return seats*10000
        elif 20<seats<=40:
            return seats*150000
        elif 40<seats<=60:
            return seats*200000
        else:
            return seats*250000
    
    elif bus==2:
        print("Bus type:Luxury bus\n")
        print("Receipt number: LB"+str(random.randint(100,200)))
        if seats<=20:
            return seats*12000
        elif 20<seats<=40:
            return seats*18000
        elif 40<seats<=60:
            return seats*24000
        else:
            return seats*30000
    return amount