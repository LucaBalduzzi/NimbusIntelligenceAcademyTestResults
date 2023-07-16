import random

def multiply():
    A = 0
    B = 0
    while True:
        A = random.randint(1,9)
        B = random.randint(1,9)
        C = A*B
        if C == 4:
            print("Success!")
            return
        print("Result: " + str(C))

if __name__ == "__main__":
    multiply()