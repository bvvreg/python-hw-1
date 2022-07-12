from ast import If
import sys
print ("\n********** CALCULATOR ***********")
print ("*     Арифметичні операції      *")
print ("*         (+, -, *, /)          *")
print ("*  з двома цілими аргументами   *")
print ("*     заданими у вигляді:       *")
print ("*         X операція Y          *")
print ("*     в командній стрічці       *")
print ("*********************************\n")
SpysokArgumentiv = sys.argv
Operaciya = SpysokArgumentiv[2]

try:
    Argument1 = int(SpysokArgumentiv[1])
    Argument2 = int(SpysokArgumentiv[3])
    KilArg = len(SpysokArgumentiv)
    if KilArg == 4:
        match Operaciya:
            case "+":
                print ("Сума чисел:", int(Argument1) + int(Argument2))
            case "-":
                print ("Різниця чисел:", int(Argument1) - int(Argument2))
            case "*":
                print ("Добуток чисел:", int(Argument1) * int(Argument2))
            case "/":
                if int(Argument2) == 0:
                    print ("Помилка: ділення на 0!")
                else:
                    print ("Частка чисел:", int(Argument1) / int(Argument2))
    else:
        print ("Помилка: недопустима кількість аргументів!")
except ValueError:
    print ("Помилка:введіть числа!")
print ("\n*********************************")
