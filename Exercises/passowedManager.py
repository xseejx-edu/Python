import random
import os

def newPasswordfile(password_number=1, pass_length=10):
    word_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()" 
    pass_list = []
    for _ in range(password_number):
        pass_list.append("".join(random.choice(word_list) for _ in range(pass_length)))
    print("[+] Generated Passwords:")
    for password in pass_list:
        print(password)    
    fileName = input("[?] Insert name of file > ")
    manageFile(filePath=fileName, mode="w", list=pass_list)

def manageFile(filePath=None, mode="r", list=None):
    try:
        with open(file=filePath, mode=mode) as file:
            if mode == "w":
                for _ in list:
                    file.write(_[::-1]+"\n")
            elif mode == "r":
                print(file.read())
    except Exception as e:
        print(e)

if __name__ == "__main__":
    mode = 0
    while mode != 4:
        try:
            mode = int(input("""
                        [1] Generate password file
                        [2] Read password file
                        [3] Clear password file 
                        [4] Exit\n
                        [i] >> """))
        except Exception as e:
            print(e)
            continue
        if mode==1:
            password_number = 0
            pass_length = 0
            while password_number<1 or password_number>50:
                try:
                    password_number = int(input("[?] Insert number of passwords [1-50] >>  "))
                except Exception as e:
                    print(e)
                    
            while pass_length<10 or pass_length>20:
                try:
                    pass_length = int(input("[?] Insert length of passwords [10-20] >>  "))
                except Exception as e:
                    print(e)
                  
            newPasswordfile(password_number=password_number, pass_length=pass_length)
        elif mode==2:
            fileName = input("[?] Insert name of file > ")
            manageFile(filePath=fileName, mode="r")
        elif mode==3:
            fileName = input("[?] Insert name of file > ")
            manageFile(filePath=fileName, mode="w", list=[" " for _ in range(50)])