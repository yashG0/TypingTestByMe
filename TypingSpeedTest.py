import time
import random as rm
from turtle import speed


def mistake(parTest,userInput):
    error = 0
    for i in range(len(parTest)):
        try:
            if parTest[i] != userInput[i]:
                error+=1
        except:
            error+=1
    return error

def SpeedTime(time_start,time_end,userInput):
    time_delay = time_end - time_start
    time_roundOff_time = round(time_delay,2)
    speed = len(userInput)/time_roundOff_time
    return round(speed)

if __name__ == '__main__':
    while True:
        check = input("Ready for test (y,n): ")
        if check in 'y':
            test = ["This Line is only for Testing purpose Only! ","my name is yash gaurkar","This is my Project Based on Speed test"]

            test1 = rm.choice(test)
            print("     **** Typing Speed ****      ")
            print(test1)
            print()
            print()
            time1 = time.time()
            userInput = input("Enter : ")
            time2 = time.time()
            print("Speed: ",SpeedTime(time1,time2,userInput)*60," wpm")
            print("Mistake: ",mistake(test1,userInput)," errors")
        elif check in 'n':
            print("Thank you, Have a nice Day . . .")
            break
        else:
            print("Enter valid input! ")
            continue








