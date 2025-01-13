import os
import curses

def list_directory(path="./"):
    files = []
    for file in os.listdir(path):
        if file.startswith("."):
            continue
        elif file.endswith(".csv"):
            files.append(file)
    return files

def curses_menu(stdscr, files):
    curses.curs_set(0)
    current_row = 0

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        for idx, file in enumerate(files):
            x = w//2 - len(file)//2
            y = h//2 - len(files)//2 + idx
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, file)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, file)

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(files) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.addstr(0, 0, f"Sie haben '{files[current_row]}' ausgewählt")
            stdscr.refresh()
            stdscr.getch()
            break

def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    files = list_directory()
    curses_menu(stdscr, files)

if __name__ == "__main__":
    curses.wrapper(main)