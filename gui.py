from tkinter import *
from tkinter import ttk
import character_creater


races = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-elf', 'Halfling', 'Half-Orc', 'Human', 'Tiefling']
classes = ['Artificer', 'Barbarian', 'Bard', 'Blood Hunter','Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger',
           'Rogue', 'Sorcerer', 'Warlock', 'Wizard']


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
        self.window = window
        self.window.geometry('500x150')

        # Character creator frame
        self.master = Frame(window)
        self.top_character_frame = Frame(self.master)
        self.stat_display = Label(self.top_character_frame, text=f'{character_creater.roll_stats()}', font=14)
        self.name_label = Label(self.top_character_frame, text='Name:')
        self.name = Entry(self.top_character_frame)
        self.class_label = Label(self.top_character_frame, text='Class:')
        self.char_class = ttk.Combobox(self.top_character_frame)
        self.char_class['values'] = classes
        self.char_class.state(['readonly'])
        self.race_label = Label(self.top_character_frame, text='Race:')
        self.race_selection = ttk.Combobox(self.top_character_frame)
        self.race_selection['values'] = races
        self.race_selection.state(['readonly'])
        self.level_label = Label(self.top_character_frame, text='Level:')
        self.level = Entry(self.top_character_frame)

        self.bottom_character_frame = Frame(self.master)
        self.strength_label = Label(self.bottom_character_frame, text='Str')
        self.dexterity_label = Label(self.bottom_character_frame, text='Dex')
        self.constitution_label = Label(self.bottom_character_frame, text='Con')
        self.wisdom_label = Label(self.bottom_character_frame, text='Wis')
        self.intelligence_label = Label(self.bottom_character_frame, text='Int')
        self.charisma_label = Label(self.bottom_character_frame, text='Cha')

        self.strength_entry = Entry(self.bottom_character_frame, width=7)
        self.dexterity_entry = Entry(self.bottom_character_frame, width=7)
        self.constitution_entry = Entry(self.bottom_character_frame, width=7)
        self.wisdom_entry = Entry(self.bottom_character_frame, width=7)
        self.intelligence_entry = Entry(self.bottom_character_frame, width=7)
        self.charisma_entry = Entry(self.bottom_character_frame, width=7)

        self.bonus_label = Label(self.bottom_character_frame, text='Bonus')
        self.bonus_strength_label = Label(self.bottom_character_frame, text=f'+0')
        self.bonus_dexterity_label = Label(self.bottom_character_frame, text=f'+0')
        self.bonus_constitution_label = Label(self.bottom_character_frame, text=f'+0')
        self.bonus_wisdom_label = Label(self.bottom_character_frame, text=f'+0')
        self.bonus_intelligence_label = Label(self.bottom_character_frame, text=f'+0')
        self.bonus_charisma_label = Label(self.bottom_character_frame, text=f'+0')

        self.total_label = Label(self.bottom_character_frame, text='Total')
        self.strength_total_label = Label(self.bottom_character_frame, text=f'')
        self.dexterity_total_label = Label(self.bottom_character_frame, text=f'')
        self.constitution_total_label = Label(self.bottom_character_frame, text=f'')
        self.wisdom_total_label = Label(self.bottom_character_frame, text=f'')
        self.intelligence_total_label = Label(self.bottom_character_frame, text=f'')
        self.charisma_total_label = Label(self.bottom_character_frame, text=f'')

        self.modifier_label = Label(self.bottom_character_frame, text='Modifier')
        self.strength_modifier_label = Label(self.bottom_character_frame, text='')
        self.dexterity_modifier_label = Label(self.bottom_character_frame, text='')
        self.constitution_modifier_label = Label(self.bottom_character_frame, text='')
        self.wisdom_modifier_label = Label(self.bottom_character_frame, text='')
        self.intelligence_modifier_label = Label(self.bottom_character_frame, text='')
        self.charisma_modifier_label = Label(self.bottom_character_frame, text='')

        self.character_button_frame = Frame(self.master)
        self.menu_button = Button(self.character_button_frame, text="Go Back to Menu")
        self.save_character_button = Button(self.character_button_frame, text='Save Character')
        self.reset_button = Button(self.character_button_frame, text='Reset', command=self.reset)

        self.top_character_frame.grid(pady=10)
        self.bottom_character_frame.grid(pady=10)
        self.character_button_frame.grid(pady=10)
        self.stat_display.grid(column=0, row=0, rowspan=2, columnspan=2, pady=5, padx=10)
        self.name_label.grid(column=2, row=0, pady=5)
        self.name.grid(column=3, row=0, pady=5)
        self.class_label.grid(column=4, row=0, pady=5)
        self.char_class.grid(column=5, row=0, pady=5)
        self.race_label.grid(column=2, row=1, pady=5)
        self.race_selection.grid(column=3, row=1, pady=5)
        self.level_label.grid(column=4, row=1, pady=5)
        self.level.grid(column=5, row=1, pady=5)

        # Start of bottom grid
        self.strength_label.grid(column=1, row=3, padx=15)
        self.dexterity_label.grid(column=2, row=3, padx=15)
        self.constitution_label.grid(column=3, row=3, padx=15)
        self.wisdom_label.grid(column=4, row=3, padx=15)
        self.intelligence_label.grid(column=5, row=3, padx=15)
        self.charisma_label.grid(column=6, row=3, padx=15)

        self.strength_entry.grid(column=1, row=4, padx=15)
        self.dexterity_entry.grid(column=2, row=4, padx=15)
        self.constitution_entry.grid(column=3, row=4, padx=15)
        self.wisdom_entry.grid(column=4, row=4, padx=15)
        self.intelligence_entry.grid(column=5, row=4, padx=15)
        self.charisma_entry.grid(column=6, row=4, padx=15)

        self.bonus_label.grid(column=0, row=5, padx=5)
        self.bonus_strength_label.grid(column=1, row=5, padx=15)
        self.bonus_dexterity_label.grid(column=2, row=5, padx=15)
        self.bonus_constitution_label.grid(column=3, row=5, padx=15)
        self.bonus_wisdom_label.grid(column=4, row=5, padx=15)
        self.bonus_intelligence_label.grid(column=5, row=5, padx=15)
        self.bonus_charisma_label.grid(column=6, row=5, padx=15)

        self.total_label.grid(column=0, row=6, padx=5)
        self.strength_total_label.grid(column=1, row=6, padx=15)
        self.dexterity_total_label.grid(column=2, row=6, padx=15)
        self.constitution_total_label.grid(column=3, row=6, padx=15)
        self.wisdom_total_label.grid(column=4, row=6, padx=15)
        self.intelligence_total_label.grid(column=6, row=5, padx=15)
        self.charisma_total_label.grid(column=6, row=6, padx=15)

        self.modifier_label.grid(column=0, row=7, padx=5)
        self.strength_modifier_label.grid(column=1, row=7, padx=15)
        self.dexterity_modifier_label.grid(column=2, row=7, padx=15)
        self.constitution_modifier_label.grid(column=3, row=7, padx=15)
        self.wisdom_modifier_label.grid(column=4, row=7, padx=15)
        self.intelligence_modifier_label.grid(column=5, row=7, padx=15)
        self.charisma_modifier_label.grid(column=6, row=7, padx=15)

    def add_character(self):
        self.main_frame.forget()
        self.window.geometry('600x200')
        center(self.window)
        self.master.grid()

    def update_values(self):
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
