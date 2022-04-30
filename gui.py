from tkinter import *
from tkinter import ttk
import character_creater


class Window:
    def __init__(self, window):
        # Main screen
        self.main_frame = Frame(window)
        self.main_phrase = Label(self.main_frame, text='Welcome to the DM\'s tavern what can we do for you today?')
        self.add_character_button = Button(self.main_frame, text='Add Character', command=self.add_character)
        self.update_character_button = Button(self.main_frame, text='Update Character', command=self.update_character)
        self.see_characters_button = Button(self.main_frame, text='See All Characters', command=self.see_all_characters)
        self.main_phrase.pack(side=TOP, pady=20)
        self.add_character_button.pack(side=LEFT, padx=50)
        self.update_character_button.pack(side=RIGHT, padx=50)
        self.see_characters_button.pack(side=BOTTOM)
        self.main_frame.pack()
        window.geometry('500x150')

        # Character creator frame
        self.character_frame = Frame(window)
        self.stat_display = Label(self.character_frame, text=f'{character_creater.roll_stats()}')
        self.name_label = Label(self.character_frame, text='Name:')
        self.name = Entry(self.character_frame)
        self.race_selection = ttk.Combobox(self.character_frame, textvariable=character_creater.races)

        self.strength_label = Label(self.character_frame, text='Str')
        self.dexterity_label = Label(self.character_frame, text='Dex')
        self.constitution_label = Label(self.character_frame, text='Con')
        self.wisdom_label = Label(self.character_frame, text='Wis')
        self.intelligence_label = Label(self.character_frame, text='Int')
        self.charisma_label = Label(self.character_frame, text='Cha')

        self.strength_entry = Entry(self.character_frame)
        self.dexterity_entry = Entry(self.character_frame)
        self.constitution_entry = Entry(self.character_frame)
        self.wisdom_entry = Entry(self.character_frame)
        self.intelligence_entry = Entry(self.character_frame)
        self.charisma_entry = Entry(self.character_frame)

        self.bonus_strength_label = Label(self.character_frame, text='')
        self.bonus_dexterity_label = Label(self.character_frame, text='')
        self.bonus_constitution_label = Label(self.character_frame, text='')
        self.bonus_wisdom_label = Label(self.character_frame, text='')
        self.bonus_intelligence_label = Label(self.character_frame, text='')
        self.bonus_charisma_label = Label(self.character_frame, text='')

        self.strength_total_label = Label(self.character_frame, text='')
        self.dexterity_total_label = Label(self.character_frame, text='')
        self.constitution_total_label = Label(self.character_frame, text='')
        self.wisdom_total_label = Label(self.character_frame, text='')
        self.intelligence_total_label = Label(self.character_frame, text='')
        self.charisma_total_label = Label(self.character_frame, text='')

        self.strength_modifier_label = Label(self.character_frame, text='')
        self.dexterity_modifier_label = Label(self.character_frame, text='')
        self.constitution_modifier_label = Label(self.character_frame, text='')
        self.wisdom_modifier_label = Label(self.character_frame, text='')
        self.intelligence_modifier_label = Label(self.character_frame, text='')
        self.charisma_modifier_label = Label(self.character_frame, text='')

        self.menu_button = Button(self.character_frame, text="Go Back to Menu")
        self.save_character_button = Button(self.character_frame, text='Save Character')
        self.reset_button = Button(self.character_frame, text='Reset', command=self.reset)

    def add_character(self):
        pass

    def update_character(self):
        pass

    def see_all_characters(self):
        pass

    def reset(self):
        pass

    def save_character(self):
        pass

    def menu(self):
        pass


# Got this code from https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter
def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()
