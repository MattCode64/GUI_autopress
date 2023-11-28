import pyautogui as pag


# Create a function tabulate that may takes a parameter which is the number of times we want to tabulate
def tabulate(times, delay):
    for i in range(times):
        pag.press('tab')
        pag.sleep(delay)


def enter(times, delay):
    for i in range(times):
        pag.press('enter')
        pag.sleep(delay)


def down_arrow(times, delay):
    for i in range(times):
        pag.press('down')
        pag.sleep(delay)


def ctrl_w(times, delay):
    for i in range(times):
        pag.hotkey('ctrl', 'w')
        pag.sleep(delay)


def automatise_print():
    print("Hello from autoui_utils.py")
    print("Starting autoui_utils.py")

    # Tabulate 5 times
    tabulate(6, 2)

    # Enter 1 time
    enter(1, 1)

    # Down arrow 1 time
    down_arrow(1, 1)

    # Enter 1 time
    enter(1, 1)

    # Tabulate 4 times
    tabulate(4, 1)

    # Enter 1 time
    enter(1, 10)

    print("Ending autoui_utils.py")
