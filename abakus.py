from time import sleep
import sys

from pyfiglet import figlet_format
xo = (figlet_format('Abakus  \n0 . 1', font='goofy'))
for x in xo:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.0003)


print('')
invalid_input = True
def start():
    broj1 = int(input("Prvi broj je: "))
    operator = input("Odaberite racunsku operaciju   +  -  *  /   : ")        
    broj2 = int(input("Drugi broj je: "))           
    if operator == "+":
        resenje = broj1 + broj2
    elif operator == "-":
        resenje = broj1 - broj2
    elif operator == "*":
        resenje = broj1 * broj2
    elif operator == "/":
        resenje = broj1 / broj2
    dada = ("Resenje je: " + str(resenje))

    for x in dada:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.03)
    print("")
    print("")
    ox = ("Hvala!")
    for x in ox:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.2)
    print("")
    print("")
    print("")
while invalid_input :
    start()
    
