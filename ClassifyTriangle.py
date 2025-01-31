def classify_triangle(a,b,c):
    if a <= 0 or b <= 0 or c <= 0 or (a+b<=c) or (a+c<=b) or (b+c<=a):
        return "Invalid parameters, not a triangle"
    elif a == b == c:
        triangle = "Equilateral Triangle"
    elif a == b or a == c or b == c:
        triangle = "Isosceles Triangle"
    else:
        triangle = "Scalene Triangle"
    if a**2 + b**2 == c**2:
        triangle = "Right Triangle"
    return triangle
    

