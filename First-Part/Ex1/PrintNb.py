#!/bin/python3

def main():
    for i in range(101):
        if i % 3 == 0 and i % 5 == 0:
            print("threefive")
        elif i % 3 == 0:
            print("three")
        elif i % 5 == 0:
            print("five")
        else:
            print(i)
        

if __name__ == "__main__":
    main()