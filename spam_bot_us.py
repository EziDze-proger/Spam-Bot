
import time as t
import pyautogui as pag

def start():
    print("SPAM BOT")
    print()
    print("1 - spam word")
    print("2 - hold down the key")
    user_answer = input()
    return user_answer

def word():
    """first check"""
    word = input("What word do you want to spam?: ")
    return word

def quantity():
    """first check"""
    while True:
        try:
            quantity = int(input("How many times do you want to call the word?: "))
            break
        except (ValueError):
            print("indicate the number")
            print()
    return quantity

def time_word():
    """first check"""
    while True:
        try:
            time_word = int(input("How many seconds do you want to activate the spam bot?: "))
            break
        except (ValueError):
            print("indicate the number")
            print()
    return time_word

def interval():
    """first check"""
    interval = input("What spacing between letters do you want to make?: ")
    return interval

def spam(word, quantity, interval, time_word):
    """first check"""
    num = 0
    t.sleep(time_word)
    while num < quantity:
        num += 1
        pag.write(word, interval)
        pag.press("enter")

def key():
    """second check"""
    key = input("Which key do you want to hold?: ")
    return key

def quantity_key():
    """second check"""
    while True:
        try:
            quantity_key = int(input("How many letters on one line do you want to print?: "))
            break
        except (ValueError):
            print("indicate the number")
            print()
    return quantity_key

def time():
    """second check"""
    time = input("What spacing between letters do you want to make?: ")
    return time

def time_key():
    """second check"""
    while True:
        try:
            time_key = float(input("How many seconds do you want to activate the spam bot?: "))
            break
        except (ValueError):
            print("indicate the number")
            print()
    return time_key

def quantity_for_key():
    """second check"""
    while True:
        try:
            quantity_for_key = int(input("How many lines do you want to print?: "))
            break
        except (ValueError):
            print("indicate the number")
            print()
    return quantity_for_key

def spam_key(key, quantity_key, quantity_for_key, time, time_key):
    """second check"""
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
        print("Sorry, I don't understand autis(")

proverka(start())
