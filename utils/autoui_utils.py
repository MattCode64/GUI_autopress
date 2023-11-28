import pyautogui as pag


def tabulate():
    pag.press('tab')


def enter():
    pag.press('enter')


def down_arrow():
    pag.press('down')


def automatise_print():
    print("Hello from autoui_utils.py")
    print("Starting autoui_utils.py")

    # Click on tabulate 5 times
    for i in range(5):
        tabulate()

    # Click on enter one time
    enter()

    # Click on down arrow one time
    down_arrow()

    # CLick on enter one time
    enter()

    # Click on tabulate 4 times
    for i in range(4):
        tabulate()

    # Click on enter one time
    enter()

    print("Ending autoui_utils.py")
