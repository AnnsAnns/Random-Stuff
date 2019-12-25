import pyautogui
import string
import time

Alphabet = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

for letter in Alphabet:
    time.sleep(5)
    pyautogui.typewrite(("l", "4", "y", "o", "l", letter, "f", "w", "c", "g", "c", letter, "u", "z", "9", "s"), interval=0.2)