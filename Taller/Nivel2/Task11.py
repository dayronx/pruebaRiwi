# Clasificador de notas (Excelente, Aprobado, Reprobado).

Score=float(input("What is your score in this subject?:  "))


Excellent=5.0
Passed=3.0


if Score==Excellent:

    print("Great, you got an excellent grade!")

if Score<Excellent and Score>=Passed:

    print("Passed")

if Score<Passed:

    print("Failed")






