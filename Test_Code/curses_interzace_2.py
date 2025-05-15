import curses
from curses.textpad import Textbox, rectangle
from curses import wrapper

def main(stdscr):
    stdscr.addstr(0, 0, "Enter IM message: (hit Ctrl-G to send)")

    editwin = curses.newwin(1,30, 2,1)
    rectangle(stdscr, 1,0,1, 1+30+1)
    stdscr.refresh()

    box = Textbox(editwin)

    # Let the user edit until Ctrl-G is struck.
    box.edit()

    # Get resulting contents
    message = box.gather()

    editwin2 = curses.newwin(1,30, 2,1)
    rectangle(stdscr, 1,6, 1, 1+30+1)
    stdscr.refresh()

    box2 = Textbox(editwin2)

    # Let the user edit until Ctrl-G is struck.
    box2.edit()

    # Get resulting contents
    message = box2.gather()
    

wrapper(main)
