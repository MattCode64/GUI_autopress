import pyautogui as pag
import datetime


def tabulate(times, delay):
    for i in range(times):
        pag.press('tab')
        print("\033[92m" + "TAB" + "\033[0m")
        pag.sleep(delay)


def enter(times, delay):
    for i in range(times):
        pag.press('enter')
        print("\033[92m" + "ENTER" + "\033[0m")
        pag.sleep(delay)


def down_arrow(times, delay):
    for i in range(times):
        pag.press('down')
        print("\033[92m" + "DOWN ARROW" + "\033[0m")
        pag.sleep(delay)


def ctrl_w(times, delay):
    for i in range(times):
        pag.hotkey('ctrl', 'w')
        print("\033[92m" + "CTRL + W" + "\033[0m")
        pag.sleep(delay)


def save_file(delay, name):
    pag.sleep(delay)
    print("\033[92m" + "SAVE PDF FILE | PAGE : " + name.upper() + "\033[0m")
    pag.typewrite(name + " " + str(datetime.date.today()))
    pag.sleep(delay+0.5)
