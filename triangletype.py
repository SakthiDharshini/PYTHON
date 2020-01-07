A = int(input("A ="))
B = int(input("B ="))
C = int(input("C ="))
if A == B == C:
    print("Equilateral Triangle")
elif A == B or B == C or C == A:
    print("Isosceles Triangle")
else :
    print("Scalene Triangle")
