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


def ctrl_w(times, delay):
    for i in range(times):
        pag.hotkey('ctrl', 'w')
        print("\033[92m" + "CTRL + W" + "\033[0m")
        pag.sleep(delay)


def save_file(delay, name):
    pag.typewrite(name)
    pag.sleep(delay)
