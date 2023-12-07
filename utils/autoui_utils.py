import datetime

import pyautogui as pag


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


def ctrl_w(times, delay, os_system):
    if os_system == "linux":
        for i in range(times):
            pag.hotkey('ctrl', 'z')
            print("\033[92m" + "CTRL + W" + "\033[0m")
            pag.sleep(delay)

    elif os_system == "windows":
        for i in range(times):
            pag.hotkey('ctrl', 'w')
            print("\033[92m" + "CTRL + W" + "\033[0m")
            pag.sleep(delay)

    else:
        print("OS not supported")


def win_tab(times, delay):
    pag.sleep(delay + 1)
    for i in range(times):
        pag.hotkey('win', 'tab')
        print("\033[92m" + "WIN + TAB" + "\033[0m")
        pag.sleep(delay)


def alt_tab(times, delay):
    for i in range(times):
        pag.hotkey('alt', 'tab')
        print("\033[92m" + "ALT + TAB" + "\033[0m")
        pag.sleep(delay)


def win(times, delay):
    for i in range(times):
        pag.press('winleft')
        pag.press('winright')
        pag.press('win')
        print("\033[92m" + "WIN" + "\033[0m")
        pag.sleep(delay)


def save_file(delay, name):
    pag.sleep(delay + 3)
    print("\033[92m" + "SAVE PDF FILE | PAGE : " + name.upper() + "\033[0m")
    pag.write(name + " " + str(datetime.date.today()), interval=0.1)
    pag.sleep(delay)
