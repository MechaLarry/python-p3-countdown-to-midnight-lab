# your code goes here!
# import time
# bash = 10
# def countdown():
#     while bash > 0:
#         print(f'{bash} SECOND(S)')
#         bash -= 1
#     return "HAPPY NEW YEAR!"

# def countdown_with_sleep(bash):
#     while bash > 0:
#         print(f'{bash} SECOND(s)')
#         time.sleep(1)
#         bash -= 1
#         print("HAPPY NEW YEAR!")

import time

bash =10
def countdown(bash):
    for i in range(bash, 0, -1):
        print(f"{i} SECOND(S)!")
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(bash):
    for i in range(bash, 0, -1):
        print(f"{i} SECOND(S)!")
        time.sleep(1)
    print("HAPPY NEW YEAR!")
