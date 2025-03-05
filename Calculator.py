name=input("Enter your Name : ") 
print("\nHello",name ,"Welcome to Your own World")

while True:
    print("\n\nSelect your operation")
    print(" 1.For Addition \n 2.For Subtraction \n 3.For Multiplication \n 4.For Division \n 5.For Square \n 0.For exit")
    opr=int(input("Select : "))
    if(opr==1 or opr==2 or opr==3 or opr==4 or opr==5):
        a=int(input("Enter the 1st number : "))
        b=int(input("Enter the 2nd number : "))
        if(opr==1):
            print("Sum =",a+b)
        elif(opr==2):
            print("Subtraction =",a-b)
        elif(opr==3):
            print("Multiplication =",a*b)
        elif(opr==4):
            print("Division =",a/b)
        elif(opr==5):
            print(" Square of",a,"is =",a*a,"\n Square of",b,"is =",b*b)
    elif(opr==0):
            print("Thank you",name,"\n 1.For Provide Feedback \n 2.For Not Provide ")
            f=int(input("Please Enter : "))
            if(f==1):
                print(" 1.For Normal \n 2.For Good \n 3.For Best")
                g=int(input("Select : "))
                if(g==1):
                    print("Do you want to Sujjest something so please :")
                    print(" 1.For Yes \n 2.For No")
                    q=int(input("Select : "))
                    if(q==1):
                        print("Thank you",name,"To help us we will work on that")
                        w=input("Please write : ")
                        break;
                    else:
                        print("Thank you",name,"We will try to improve")
                        break;
                elif(g==2):
                    print("Do you want to Sujjest something so please\n")
                    print("1.For Yes \n2.For No")
                    q=int(input("Select : "))
                    if(q==1):
                        print("Thank you",name,"To help us we will work on it")
                        w=input("Please write :")
                        break;
                    elif(q==2):
                        print("Thank you",name,"We will try to improve")
                        break;
                elif(g==3):
                    print("Thank you",name,"For your Feedback")
                    break;
            elif(f==2):
                print("Thank you",name)
                break;
    else:
        print("Please Select Correct Operation")
            



           


