# Added imports at the beginning
from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan 1") # change in main

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"{x}+{y}={summa(x, y)}") # change in main
print(f"{x}-{y}={erotus(x, y)}") # change in main

logger("lopetetaan")
print("goodbye!") # added in bugfix branch