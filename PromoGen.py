import time
import os 
import sys
import random
import datetime
import art 
from art import *
import colorama
from colorama import Fore



chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabdefghijklmnopqrstuvwxyz0123456789"
discord = "https://discord.gift/"




print("Scraping 28731 Proxies")

time.sleep(0.5)

print("Connecting to Proxies")

time.sleep(5)

os.system('CLS')
tprint("bluestorm")
print("This Just For Fun it would probaly take like 12 billion codes are more to get an real one ")
promo = int(input("Amount of Promos code to generate:\n"))


for i in range(promo):
    code = ''.join((random.choice(chars) for i in range(16)))
    
    result =  '[+]' + discord + code
    
    
    
    print(Fore.CYAN + result)
    output = open("nitrocodes.txt", "a")
    output.write( result + "\n")

