password=input("Enter your Password.")
if (len(password)>=8) and (len(password)<=15):
    print("congratulation your password is sucessfully done.")
elif (len(password)>=1) and (len(password)<=7):
    print("please enter strong password.")
elif (len(password)>=0) and (len(password)<=0):
    print("enter valid password")
else:
    print("enter valid password.")

