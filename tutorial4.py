# tutorial4 , users input and textboxes
import curses 
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time 

def main(stdscr):
	curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
	curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

	rectangle(stdscr, 2, 2, 10, 20)
	stdscr.getch()
	stdscr.refresh()
wrapper(main)