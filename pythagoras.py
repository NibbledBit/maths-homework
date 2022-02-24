import math


def pythagoras(a, b):
    print(f"A = {a}")
    print(f"B = {b}")

    a2 = a ** 2
    print(f"A² = {a2}")

    b2 = b ** 2
    print(f"B² = {b2}")

    c2 = a2 + b2
    print(f"C² = {c2}")

    c = math.sqrt(c2)

    print("A² + B² = C²")
    return c


print(f"Hypotenuse = {pythagoras(3, 4)}")
