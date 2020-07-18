
import time as t
import pyautogui as pag

def start():
    print("СПАМ БОТ")
    print()
    print("1 - спамить слово")
    print("2 - зажать букву")
    user_answer = input()
    return user_answer

def word():
    """первая проверка"""
    word = input("Какое слово вы хотите заспамить?: ")
    return word

def quantity():
    """первая проверка"""
    while True:
        try:
            quantity = int(input("Сколько раз вы хотите вызвать слово?: "))
            break
        except (ValueError):
            print("укажите число")
            print()
    return quantity

def time_word():
    """первая проверка"""
    while True:
        try:
            time_word = int(input("Через сколько вы хотите активировать спам бота?: "))
            break
        except (ValueError):
            print("укажите число")
            print()
    return time_word

def interval():
    """первая проверка"""
    interval = input("Какой интервал между буквами вы хотите сделать?: ")
    return interval

def spam(word, quantity, interval, time_word):
    """первая проверка"""
    num = 0
    t.sleep(time_word)
    while num < quantity:
        num += 1
        pag.write(word, interval)
        pag.press("enter")

def key():
    """вторая проверка"""
    key = input("Какую букву вы хотите зажать?: ")
    return key

def quantity_key():
    """вторая проверка"""
    while True:
        try:
            quantity_key = int(input("Cколько букв в одной строке вы хотите напечатать?: "))
            break
        except (ValueError):
            print("укажите число")
            print()
    return quantity_key

def time():
    """вторая проверка"""
    time = input("Какой интервал между буквами вы хотите сделать?: ")
    return time

def time_key():
    """вторая проверка"""
    while True:
        try:
            time_key = float(input("Через сколько секунд вы хотите активировать спам бота?: "))
            break
        except (ValueError):
            print("укажите число")
            print()
    return time_key

def quantity_for_key():
    """вторая проверка"""
    while True:
        try:
            quantity_for_key = int(input("Сколько строк вы хотите напечатать?: "))
            break
        except (ValueError):
            print("укажите число")
            print()
    return quantity_for_key

def spam_key(key, quantity_key, quantity_for_key, time, time_key):
    """вторая проверка"""
    num1 = 0
    t.sleep(time_key)
    while num1 < quantity_for_key:
        keys = ""
        for x in range(quantity_key):
            keys += key
        pag.write(keys, time)
        pag.press("enter")
        num1 += 1

def proverka(user_answer):
    if user_answer == "1":
        print()
        spam(word(), quantity(), interval(), time_word())

    elif user_answer == "2":
        print()
        spam_key(key(), quantity_key(), quantity_for_key(), time(), time_key())

    else:
        print()
        print("Сорян, аутистов не понимаю(")

proverka(start())
