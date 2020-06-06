#!/usr/bin/python3
"""made by https://github.com/CyberDemon-crypto"""
import time
nominal = [1, 2, 5, 10, 100, 500, 1000, 10000]


def stat():
    n = 0
    table = ""
    total = 0
    for n in nominal:
        a = input(f'Amount of money with value {n}Р: ')
        t = str(int(n) * int(a))
        total += int(t)
        table += f"|{toten(str(n)+'Р')}{toten(a)}{toten(t+'Р')}|\n"
    table += f"|            Total = {toten(str(total)+'Р')}|\n"
    return table


def toten(someinput):
    while len(someinput) < 10:
        someinput += " "
    return someinput


with open("wallet", "a") as money:
    money.write("\n ______________________________ \n"
                "|Value    Amount    Total      |\n"
                "|------------------------------|\n"
                f"{stat()}"
                f" ---{time.asctime(time.localtime())}--- \n")

