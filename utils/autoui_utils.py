import time

import pyautogui as pag
import datetime

import pyperclip


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


def win_tab(times, delay):
    pag.sleep(delay+1)
    for i in range(times):
        pag.hotkey('win', 'tab')
        print("\033[92m" + "ALT + TAB" + "\033[0m")
        pag.sleep(delay)


def save_file(delay, name):
    time.sleep(delay)
    def _workaround_write(text):
        """
        This is a work-around for the bug in pyautogui.write() with non-QWERTY keyboards
        It copies the text to clipboard and pastes it, instead of typing it.
        """
        pyperclip.copy(text)
        pag.hotkey('ctrl', 'v')
        pyperclip.copy('')

    # Test
    text_with_special_chars = name + " " + str(datetime.date.today())
    # pag.write(text_with_special_chars)

    _workaround_write(text_with_special_chars)
    # print(name)
    # pag.sleep(delay)
    # print("\033[92m" + "SAVE PDF FILE | PAGE : " + name.upper() + "\033[0m")
    # pag.write(name + " " + str(datetime.date.today()), interval=0.1)
    # pag.sleep(delay + 0.5)
