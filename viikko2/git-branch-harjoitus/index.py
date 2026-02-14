# Added imports at the beginning
from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan")

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"The sum of {x} and {y} is {summa(x, y)}") # change in bugfix
print(f"The difference between {x} and {y} is {erotus(x, y)}") # change in bugfix

logger("lopetetaan")
print("goodbye!") # added in bugfix branch