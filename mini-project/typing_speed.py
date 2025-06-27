# Typing speed calculator/measure

from time import *
import random as r

def mistake(string_test,user_input):
    error = 0
    for i in range(len(string_test)):
        try:
            if string_test[i] != user_input[i]:
                error = error + 1
        except :
            error = error + 1
    return error

def speed_time(time_s,time_e,user_input):
    delay_time = time_e - time_s
    roundof_time = round(delay_time,2) #round the number of delay time in 2 digit's
    speed = len(user_input)/ roundof_time
    return round(speed)

if __name__ == '__main__': 
    while True:
        check = input(" Ready to test (yes / no) : ")
        if check == "yes":
            test = ["A paragraph is a self contained unit of discourse in writing dealing a particular point or idea",
                    "Here you can find random string which you have to type",
                    "After typing any of these string you get result of your typing speed"]
            random_string = r.choice(test) #It will find random string from test list
            print("    *****Typing speed*****")
            print(random_string)
            print()
            print()

            start_time = time() #starting time counter before user start typing
            test_input = input(" Enter above string : ")
            type_time = time() #user typing time counter

            print('Speed : ', speed_time(start_time,type_time,test_input),"w/sec") #Word per second
            print("Error : ", mistake(random_string,test_input))
        elif check == 'no':
            print()
            print(" Thank You ")
            break
        else:
            print(" Wrong Input")
