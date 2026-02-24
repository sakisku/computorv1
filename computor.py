#!/usr/bin/env python3
import sys
import signal
import re

equation = ""

def discriminant() -> int:
    return 0 #or -1 or 1

def reducer():
    global equation

    left, right = equation.split("=")
    pattern = r'([+-]?\s*\d*\.?\d+)\s*\*\s*X\^(\d+)'

    coeffs = {}
    for coef, power in re.findall(pattern, left):
        coef = float(coef.replace(" ", ""))
        power = int(power)
        coeffs[power] = coeffs.get(power, 0) + coef
    for coef, power in re.findall(pattern, right):
        coef = float(coef.replace(" ", ""))
        power = int(power)
        coeffs[power] = coeffs.get(power, 0) - coef
    if not coeffs:
        return "0 * X^0 = 0"

    max_degree = max(coeffs.keys())
    result = []
    for power in range(max_degree + 1):
        coef = coeffs.get(power, 0)
        sign = "+" if coef >= 0 else "-"
        coef_abs = abs(coef)
        term = f"{coef_abs:g} * X^{power}"
        if result:
            result.append(f" {sign} {term}")
        else:
            result.append(term if sign == "+" else f"-{term}")
    return "".join(result) + " = 0"

def polynomial_degree() -> int:
    global equation
    exponents = re.findall(r"X\^(\d+)", equation)
    if not exponents:
        return 0
    return int(max(exponents))

def resolver() -> str:
    degree = polynomial_degree()
    if degree == 0:
        return "constant function"
    elif degree == 1:
        return "linear function"
    elif degree == 2:
        return "quadratic function"

def display():
    degree = polynomial_degree()
    print(f"Reduced form: {reducer()}")
    print(f"Polynomial degree: {degree}")
    if degree > 2:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
        exit(1)
    print(f"{resolver()}")


def main():
    global equation
    if len(sys.argv) < 2:
        try:
            signal.signal(signal.SIGINT,
                        lambda *_: (print("Interrupted by user"),
                                    exit(1)))
            data = input("> ")
            equation = data
            display()
        except Exception as e:
            print(f"Error: {e}")
            exit(1)
    elif len(sys.argv) > 2:
        print("Too many arguments")
        exit(1)
    else:
        equation = sys.argv[1]
        display()

if __name__ == "__main__":
    main()