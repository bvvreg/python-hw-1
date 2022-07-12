from ast import If
import sys
print ("\n********** CALCULATOR ***********")
print ("*     Арифметичні операції      *")
print ("*         (+, -, *, /)          *")
print ("*     з двома аргументами       *")
print ("*     заданими у вигляді:       *")
print ("*         X операція Y          *")
print ("*     в командній стрічці       *")
print ("*********************************\n")
Arg = sys.argv
KolArg = len(Arg)
if KolArg == 4:
    match Arg[2]:
        case "+":
            print ("Сума чисел:", int(Arg[1]) + int(Arg[3]))
        case "-":
            print ("Різниця чисел:", int(Arg[1]) - int(Arg[3]))
        case "*":
            print ("Добуток чисел:", int(Arg[1]) * int(Arg[3]))
        case "/":
            if int(Arg[3]) == 0:
                print ("Помилка: ділення на 0!")
            else:
                print ("Частка чисел:", int(Arg[1]) / int(Arg[3]))
else:
    print ("Недопустима кількість аргументів!")
print ("\n*********************************")
