import math

def area(radius):
    return math.pi * radius ** 2

if __name__ == "__main__":
    radius = float(input("Введите радиус: "))
    print(f"Площадь круга: {area(radius)}")
