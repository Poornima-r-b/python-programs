user_name="divya"
user_password=1234
name=input("enter your name")
if name== user_name:
    for i in range(1,4):
        password=int(input("enter your password"))
        if password==user_password:
            print("welcome")
            break
        else:
            print(i," attempts is done")
            print(3-i, "attempts remaining")
        if i==3:
            print("account is block")
else:
        print("enter valid name")