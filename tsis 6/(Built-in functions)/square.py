import math
import threading

number = int(input("Give me a number: "))
ms = int(input("Give me ms: "))
ms/=1000
def sqr(number,ms):
    print("Square root of",number,"after",ms*1000,"miliseconds is",math.sqrt(number))

timer = threading.Timer(ms, sqr, args=(number,ms))
timer.start()
