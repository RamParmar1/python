#Basic Email Validator
email = input("Enter your Email : ")
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper(): # w== W==W
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                        
                if k==1 or j==1 or d==1:
                    print("Wrong Email 5, Space")
                else:
                    print("Right Email : ",email)
            else:
                print("Wrong Email 4, 1.-4^-3")
        else:
            print("Wrong Email 3, 1@")
    else:
        print('Wrong Email 2, 1stCharacter')
else:
    print("Wrong Email 1, 6Character")

#Here Wrong Email Index start from 1 And so on.
#if any of these condition false then it will give error.
