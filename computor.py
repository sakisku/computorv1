#!/usr/bin/env python3
import sys
import signal

def discriminant() -> int:
    return 0 #or -1 or 1

def reducer() -> str:
    return "reduced"
def polynomial_degree() -> str:
    return "1"
def resolver() -> str:

    # if polynomial() == "0":
    #     # do something
    # elif polynomial() == "1":
    #     # do something else
    # elif polynomial() == "2":
    #     # do something else
    # else:
    #     # no
    return "solution"

def display():

    print(f"Reduced form: {reducer()}")
    print(f"Polynomial degree: {polynomial_degree()}")
    print(f"{resolver()}")


def main():

    if len(sys.argv) < 2:
        try:
            signal.signal(signal.SIGINT,
                        lambda *_: (print("Interrupted by user"),
                                    exit(1)))
            equation = input("> ")
            # get_data(equation)
            display()
        except Exception as e:
            print(f"Error: {e}")
            exit(1)
    elif len(sys.argv) > 2:
        print("Too many arguments")
        exit(1)
    else:
        equation = sys.argv[1]
        # get_data(equation)
        display()

if __name__ == "__main__":
    main()