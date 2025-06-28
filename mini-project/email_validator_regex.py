# Email Validation Using regex module

import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email =input('Enter  your Email : ')

if re.search(email_condition,user_email):
    print("Right Email")
else:
    print("Wrong Email")

#Working
'''Here in variable,email_condition check that it meets condition or not,
then check through te regex own funcationality (search),
it will search our input value/string in the variable(email_condition) which define and find condition,
if true then get result of (Right Email) 
or false then get (Wrong Email)
'''
#Condition's
'''a-z ramparmar@gmail.com
   0-9
   . And _ at a one time
   @ at a one time
   . in position from last 2 And 3'''