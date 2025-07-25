# Tutorial 2 
# Atributtes and Colors
import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    stdscr.clear()
    for i in range(100):        
        color = BLUE_AND_YELLOW
        if i % 2 == 0:
            color = GREEN_AND_BLACK
        stdscr.addstr(f"Count: {i}", color)
        stdscr.refresh()
        time.sleep(0.1)
    stdscr.getkey()

wrapper(main)
