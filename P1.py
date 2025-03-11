name = '\'xSeejx\''
print("Username: ", name)

print("Name Var. is a: ", type(name))

print(f"""
10 is a: {type(10)}
10.0 is a: {type(10.0)}
Hello is a: {type("Hello")}
True is a: {type(True)}
""")

#val = input("[input] Give a number : ")
try:    
    number = int(val)
    print(f"{val} --> {type(number)}")
except:
    print("You have not insert a number")
finally:
    print("This block will be always runned")

print("--------------------------------------------------------------")
a = 12
b = 6
c = 3
d = 1
print(a,b,c,d,sep=',')
#print(f"{a},{b},{c},{d}")
print(f"""
{a}/{b} = {a/b} [with /]
{a}//{b} = {a//b} [with //]

""")
print("hello\n"*3)

    
# For Cycles
print("--------------------------------------------------------------")

# Simple For Cycle
print("\n- Simple Cycle For -")
for i in range(10):
    print(i)
print("\n- Advanced Cycle For -")
# Advanced For Cycle
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n): # it will start from 2
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence # returns a list

# Print the first 10 Fibonacci numbers
for num in fibonacci(10): # it is a For-each
    print(num)
    



