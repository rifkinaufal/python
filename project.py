#project 1
def replace_word():

    str="namaku rfki"
    word_to_replace = input("enter word to replace")
    word_replacement = input("enter word replacement")
    print(str.replace( word_to_replace,  word_replacement))

replace_word()

#project 2
def add(a, b):
    answer = a + b
    print(str(a)+ "+" + str(b) + "=" + str(answer))

def sub(a, b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer) )

def mul(a, b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer) )

def div(a, b):
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer) )

while True:
    print("A. Addition")
    print("B. Substraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

choice = input ("input your choice:" )

if choice == "a" or choice == "A":
    print("Addition")
    a = int(input("input first number:")/n)
    b = int(input("input second number:"))
    add (a,b)
elif choice == "b" or choice == "B":
    print("Substraction")
    a = int(input("input first number:")/n)
    b = int(input("input second number:"))
    sub (a,b)
elif choice == "c" or choice == "C":
    print("Multiplication")
    a = int(input("input first number:")/n)
    b = int(input("input second number:"))
    mul (a,b)
elif choice == "d" or choice == "D":
    print("Division")
    a = int(input("input first number:")/n)
    b = int(input("input second number:"))
    div (a,b)
elif choice == "e" or choice == "E":
    print("Ended")
    quit()