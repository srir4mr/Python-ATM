#python atm simulation
#pin 0000
bal==0
print(/t/t/t"Welcome to GIT bank"\n);
print(\t\t"Please insert your "\n);
pin=int(input(\t"enter your pin"\n);
While pin=="0000" :
 print("Choose Your Option "\n);
 opt=input("B->Balance Enquiry"/n"W->Withdrawl"/n"D->Deposit"/n");
if opt==b :
 print("Your current account balance is:",bal\n);
if opt==w :
 wid=int(input("Enter the withdraw amount"\n));
 if wid>bal :
  print("insufficient fund"\n);
 else:
  bal=bal-wid
  print("Please collect your cash"\n);
if opt==d :
 dep=int(input("enter the deposit amount"\n);
 bal=bal+dep
else:
print("Invalid pin);
