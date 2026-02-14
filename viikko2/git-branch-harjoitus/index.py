# Added imports at the beginning
from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan 1") # Change in main

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"{summa(x, y)}")
print(f"{erotus(x, y)}")

logger("lopetetaan")
print("goodbye!") # added in bugfix branch