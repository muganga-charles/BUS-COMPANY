#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int new_Amount = 0;
void setAmount(int amount){
    new_Amount = amount;
}
int getAmount(){
    return new_Amount;
}

int main()
{
    char username[10];
    char password[5];
    int choice,status;
    int seats,bustype,receiptno,amount;
    stop:
    printf("..................KK.BUS COMPANY..................\n");
    start:
    printf("Enter the Username\n");
    scanf("%s",&username);
    printf("Enter the password\n");
    scanf("%s",&password);
  if(strcmp(username,"Mukasa")==0 &&strcmp(password,"123") == 0)
  {
          top:
          do{
        printf("1.BUS BOOKINGSTATUS\n2.Bus booking\n3.Booking payment\n4.Booking reports\n5.sign out\n");
        scanf("%d",&status);
        if(status==2)
        {
            printf("'''''''''''''''BUS BOOKING'''''''''''\n");
            seat:
            printf("Enter the number of seats\n");
            scanf("%d",&seats);
            if(seats>60)
            {
                printf("Enter the right number of seats\n");
                goto seat;
            }
            do{
            printf("Enter the type of bus\n");
            printf("1.Ordinary\n2.Luxury\n");
            scanf("%d",&bustype);
            if(bustype==1)
            {
                int ordinary=25000;
                int cost=seats*ordinary;
                setAmount(cost);
                printf("The total cost is %d\n",cost);
                printf("Receipt no:%d%d%d%d\n",choice,status);
                printf("Bus type:Ordinary\n");
                printf("Number of seats:%d\n",seats);
               goto three;

            }else if(bustype==2)
            {
            int Luxury=50000;
             int cost=seats*Luxury;
             setAmount(cost);
             printf("The total cost is %d\n",cost);
             printf("Bus type:Luxury\n");
             printf("Number of seats :%d\n",seats);
             printf("Receipt no:%d%d%d%d%d",choice,status,bustype);
             goto three;
            }}
            while(bustype!=2);

        }
        else if (status==3)
        {
                three:
            printf("''''''Booking payments'''''''''''''\n");
            printf("Enter the receipt number\n");
            scanf("%d",&receiptno);
            printf("Enter the amount payed\n");
            scanf("%d",&amount);

            int costAmount = getAmount();
            int balance = costAmount-amount;

            printf("Balance:%d\n",balance);
        }
        if (status==5)
        {
            printf("SIGNOUT\n");
            return 0;

        }
        if (status==1)
        {
            printf("Enter the right choice\n");
            goto top;
        }

        }
        while(status==4);

      }
  else
  {
      printf("Wrong Username and password\n");
      goto start;
      goto stop;
  }



    return 0;
}
