import curses
import random
import time

def run(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    sh, sw = stdscr.getmaxyx()
    letters = [chr(i) for i in range(33, 126)]
    columns = [0] * sw

    while True:
        stdscr.erase()
        for i in range(sw):
            char = random.choice(letters)
            y = columns[i]
            stdscr.addstr(y, i, char, curses.color_pair(1))
            if random.random() < 0.05:
                stdscr.addstr(max(0, y - 1), i, char, curses.color_pair(2))
            columns[i] = (y + 1) % sh

        stdscr.refresh()
        time.sleep(0.05)
        try:
            key = stdscr.getch()
            if key == 27:  # ESC çıkış
                break
        except:
            pass
