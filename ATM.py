print("welcome to ADC\n\nInsert ATM CARD")
password=1234
choice=0
balance=10000
pin=int(input("enter your 4 digit pin\n"))
if pin==password:
	while choice!=4:
	
		print("**** Menu ****")
		print("1--balance")
		print("2--deposit")
		print("3--withdraw")
		print("4--quit\n")
	
		choice=int(input("\nenter your choice"))
	
		if choice==1:
			print("Balance==Rs",balance)
		
		elif choice==2:
			drop=int(input("enter your deposit:Rs"))
			balance+=drop
			print("\n deposited amount:Rs",drop)
			print("balance=Rs",balance)	
			
		elif choice==3:
			withdraw=int(input("enter the amount to be withdraw:Rs"))
			balance-=withdraw
			print("\n withdraw amount:Rs",withdraw)
			print("balance=Rs",balance)
			
		elif choice==4:
			print("\nsession ended!! Goodbye")
		
		else:
			print("\ninvalid entry!!")
else:

	print("pin incorrect try again")
