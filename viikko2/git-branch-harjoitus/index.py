# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan ohjelma")

x = int(input("luku 1: "))
y = int(input("luku 2: "))

print(f"{x} + {y} summa on {summa(x, y)}") # muutos merge konfliktissa
print(f"{x} - {y} erotus on {erotus(x, y)}") # muutos merge konfliktissa

logger("lopetetaan ohjelma")
print("goodbye!")