#E-mail sending from python prompt.
#We can send email to one person and also to multiple person.

import smtplib as s
obj = s.SMTP('smtp.gmail.com' , 587) #gmail port no 587
obj.ehlo()
obj.starttls()
#so first created server's two function after login through the ID/PASSWORD.

obj.login('sendermail@gmail.com' , 'password') # First Mail Address , After Password
subject = "test python prompt to send email"
body = "Python is awesome programming language."
message = "subject:{}\n\n{}".format(subject , body)
'''Using the .formatting {} we can use if user input or already print data object.if we want we can change so.
For new line \n use note it.
 dot formatting use in two steps first {} then .format()'''

#after make new variable and give multiple or single mail address.
listadd = ['johndoe@email.com' ,
           "johndoe2@gmail.com"]
#if we want to select user mailID we can directly use by obj and also we can make new variable.

#for directly input
obj.sendmail('sendermail@gmail.com',listadd,message)
print("send email")
obj.quit() #to close server
