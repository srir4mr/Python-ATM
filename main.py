#python atm simulation
#pin 0000

balance=0

print("\t\t\t Welcome to GIT bank\n");
print("\t\tPlease insert your CARD \n");
pin=int(input("\tenter your pin\n"));
while pin==0000 :
    print("Choose Your Option \n");
    opt=input("B->Balance Enquiry\nW->Withdrawl\nD->Deposit\nE->EXIT\n");
    if opt=="b" :
        print("Your current account balance is:",balance);
    if opt=="w" :
        wid=int(input("Enter the withdraw amount\n"));
        if wid>balance :
            print("insufficient fund\n");
        else:
            balance=balance-wid
        print("Please collect your cash\n");
    if opt=="d" :
        dep=int(input("enter the deposit amount\n"));
        balance=balance+dep
        print("Sucessfully deposited\n")
    if opt=="e":
        print("Thank you for banking with US :)\n")
        break 
else:
    print("Invalid pin");
