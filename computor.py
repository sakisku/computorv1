#!/usr/bin/env python3
import sys
import signal

def main():

    if len(sys.argv) < 2:
        try:
            signal.signal(signal.SIGINT,
                        lambda *_: (print("Interrupted by user"),
                                    exit(1)))
            equation = input("")
            # resolver(equation)
            print(equation)
        except Exception as e:
            print(f"Error: {e}")
            exit(1)
    elif len(sys.argv) > 2:
        print("Too many arguments")
        exit(1)
    else:
        equation = sys.argv[1]
        # resolver(equation)
        print(equation)

if __name__ == "__main__":
    main()