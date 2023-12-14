print("Program to print a number is Positive / Negative") 
choice =1  
while(choice!=0):  
 number=int(input("Enter a Number :"))   
if number >0:   
    print("The Number",number,"is Positive")   
else:    
    print("The Number",number, "is negative")   
    choice=int(input("Do you wish to continue 1/0"))