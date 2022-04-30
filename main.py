from gui import *


def main():
    master = Tk()
    # master.resizable(False, False)
    master.geometry('500x250')
    center(master)
    widgets = Window(master)
    mainloop()


if __name__ == '__main__':
    main()