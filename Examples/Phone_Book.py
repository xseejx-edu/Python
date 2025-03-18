import os
import sys

phone_book = {
    "name": ["Nexa", "Seej"],
    "age": [30, 24],
    "city": ["Japan", "Korea"],
    "Phone": [1234, 5678]
}
print(os.name)

def clear():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
    

def get_key():
    """Function to get key press from the user."""
    if sys.platform == "win32":
        import msvcrt
        key = msvcrt.getch()
        if key == b'\x00' or key == b'\xe0':  # Arrow keys start with these bytes
            key = msvcrt.getch()  # Get the actual arrow key code
        return key
    else:
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(1)
            if key == '\x1b':  # Arrow keys start with an escape character
                key += sys.stdin.read(2)  # Read two more characters
            return key
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    
# Ansi Code

RED = "\033[31m"
RESET = "\033[0m"


menu = ["Quit", "Add Contact", "Delete Contact", "Read Contact"]


if __name__ == "__main__":
    choose = -1
    while True:
        #clear()
        print("Menu:")
        for _ in menu:
            print("   ",menu.index(_), ".", _)

        key_pressed = get_key()

        if key_pressed == '\x1b[A' or key_pressed == b'\xe0H':  # Up arrow
            choose = choose % len(menu)
            print(choose)
        '''
        try:
            #print
            #choose = input("[✦] >> ")
        except KeyboardInterrupt:
            print(f"\n{RED}Write quit() or choose 0 to leave{RESET}")
            get_key()
        '''
        if choose == 0:
            break
        if choose == 1:
            clear()
            print("Adding")
            input("In")

        
        

