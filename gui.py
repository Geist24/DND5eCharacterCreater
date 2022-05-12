from tkinter import *
from tkinter import ttk
import rolling
import csv

characters = []
races = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-elf', 'Halfling', 'Half-Orc', 'Human', 'Tiefling']
classes = ['Artificer', 'Barbarian', 'Bard', 'Blood Hunter', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger',
           'Rogue', 'Sorcerer', 'Warlock', 'Wizard']


class Window:
    def __init__(self, window):
        # Main screen
        self.main_frame = Frame(window)
        self.main_phrase = Label(self.main_frame, text='Welcome to the DM\'s tavern what can we do for you today?')
        self.add_character_button = Button(self.main_frame, text='Add Character', command=self.add_character)
        self.see_characters_button = Button(self.main_frame, text='See Character', command=self.question)
        self.main_phrase.pack(side=TOP, pady=20)
        self.add_character_button.pack(side=LEFT, padx=50)
        self.see_characters_button.pack(side=BOTTOM)
        self.main_frame.pack()
        self.window = window
        self.window.geometry('500x150')

        # Character creator frame
        self.master = Frame(window)
        self.top_character_frame = Frame(self.master)
        self.stats = rolling.roll_stats()
        self.stats.sort(reverse=True)
        self.hidden_stats = self.stats[:]
        self.hidden_stats.insert(0, '--')
        self.rolls = StringVar()
        self.stat_display = Label(self.top_character_frame, textvariable=self.rolls, font=14)
        self.rolls.set(f'{self.stats}')
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

        self.strength_entry = ttk.Combobox(self.bottom_character_frame, width=7)
        self.dexterity_entry = ttk.Combobox(self.bottom_character_frame, width=7)
        self.constitution_entry = ttk.Combobox(self.bottom_character_frame, width=7)
        self.wisdom_entry = ttk.Combobox(self.bottom_character_frame, width=7)
        self.intelligence_entry = ttk.Combobox(self.bottom_character_frame, width=7)
        self.charisma_entry = ttk.Combobox(self.bottom_character_frame, width=7)

        self.strength_entry['values'] = self.hidden_stats
        self.strength_entry.state(['readonly'])
        self.dexterity_entry['values'] = self.hidden_stats
        self.dexterity_entry.state(['readonly'])
        self.constitution_entry['values'] = self.hidden_stats
        self.constitution_entry.state(['readonly'])
        self.wisdom_entry['values'] = self.hidden_stats
        self.wisdom_entry.state(['readonly'])
        self.intelligence_entry['values'] = self.hidden_stats
        self.intelligence_entry.state(['readonly'])
        self.charisma_entry['values'] = self.hidden_stats
        self.charisma_entry.state(['readonly'])

        self.str_mod = StringVar()
        self.dex_mod = StringVar()
        self.con_mod = StringVar()
        self.wis_mod = StringVar()
        self.int_mod = StringVar()
        self.cha_mod = StringVar()

        self.str_bonus = StringVar()
        self.dex_bonus = StringVar()
        self.con_bonus = StringVar()
        self.wis_bonus = StringVar()
        self.int_bonus = StringVar()
        self.cha_bonus = StringVar()

        self.str_total = StringVar()
        self.dex_total = StringVar()
        self.con_total = StringVar()
        self.wis_total = StringVar()
        self.int_total = StringVar()
        self.cha_total = StringVar()

        self.bonus_label = Label(self.bottom_character_frame, text='Bonus')
        self.bonus_strength_label = Label(self.bottom_character_frame, textvariable=self.str_bonus)
        self.bonus_dexterity_label = Label(self.bottom_character_frame, textvariable=self.dex_bonus)
        self.bonus_constitution_label = Label(self.bottom_character_frame, textvariable=self.con_bonus)
        self.bonus_wisdom_label = Label(self.bottom_character_frame, textvariable=self.wis_bonus)
        self.bonus_intelligence_label = Label(self.bottom_character_frame, textvariable=self.int_bonus)
        self.bonus_charisma_label = Label(self.bottom_character_frame, textvariable=self.cha_bonus)

        self.str_mod.set('+0')
        self.dex_mod.set("+0")
        self.con_mod.set('+0')
        self.wis_mod.set('+0')
        self.int_mod.set("+0")
        self.cha_mod.set('+0')

        self.str_prev = '--'
        self.dex_prev = '--'
        self.con_prev = '--'
        self.wis_prev = '--'
        self.int_prev = '--'
        self.cha_prev = '--'

        self.total_label = Label(self.bottom_character_frame, text='Total')
        self.strength_total_label = Label(self.bottom_character_frame, textvariable=self.str_total)
        self.dexterity_total_label = Label(self.bottom_character_frame, textvariable=self.dex_total)
        self.constitution_total_label = Label(self.bottom_character_frame, textvariable=self.con_total)
        self.wisdom_total_label = Label(self.bottom_character_frame, textvariable=self.wis_total)
        self.intelligence_total_label = Label(self.bottom_character_frame, textvariable=self.int_total)
        self.charisma_total_label = Label(self.bottom_character_frame, textvariable=self.cha_total)

        self.modifier_label = Label(self.bottom_character_frame, text='Modifier')
        self.strength_modifier_label = Label(self.bottom_character_frame, textvariable=self.str_mod)
        self.dexterity_modifier_label = Label(self.bottom_character_frame, textvariable=self.dex_mod)
        self.constitution_modifier_label = Label(self.bottom_character_frame, textvariable=self.con_mod)
        self.wisdom_modifier_label = Label(self.bottom_character_frame, textvariable=self.wis_mod)
        self.intelligence_modifier_label = Label(self.bottom_character_frame, textvariable=self.int_mod)
        self.charisma_modifier_label = Label(self.bottom_character_frame, textvariable=self.cha_mod)

        self.strength_entry.set('--')
        self.dexterity_entry.set('--')
        self.constitution_entry.set('--')
        self.wisdom_entry.set('--')
        self.intelligence_entry.set('--')
        self.charisma_entry.set('--')

        self.str_bonus.set('+0')
        self.dex_bonus.set('+0')
        self.con_bonus.set('+0')
        self.wis_bonus.set('+0')
        self.int_bonus.set('+0')
        self.cha_bonus.set('+0')

        self.race_selection.bind('<<ComboboxSelected>>', self.racial_bonus)
        self.strength_entry.bind('<<ComboboxSelected>>', self.strength_update_values)
        self.dexterity_entry.bind('<<ComboboxSelected>>', self.dexterity_update_values)
        self.constitution_entry.bind('<<ComboboxSelected>>', self.constitution_update_values)
        self.wisdom_entry.bind('<<ComboboxSelected>>', self.wisdom_update_values)
        self.intelligence_entry.bind('<<ComboboxSelected>>', self.intelligence_update_values)
        self.charisma_entry.bind('<<ComboboxSelected>>', self.charisma_update_values)

        self.character_button_frame = Frame(self.master)
        self.menu_button = Button(self.character_button_frame, text="Go Back to Menu", command=self.menu)
        self.save_character_button = Button(self.character_button_frame, text='Save Character',
                                            command=self.save_character)
        self.restart_button = Button(self.character_button_frame, text='Restart', command=self.restart)

        # Putting the items on the frame to display later
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
        self.intelligence_total_label.grid(column=5, row=6, padx=15)
        self.charisma_total_label.grid(column=6, row=6, padx=15)

        self.modifier_label.grid(column=0, row=7, padx=5)
        self.strength_modifier_label.grid(column=1, row=7, padx=15)
        self.dexterity_modifier_label.grid(column=2, row=7, padx=15)
        self.constitution_modifier_label.grid(column=3, row=7, padx=15)
        self.wisdom_modifier_label.grid(column=4, row=7, padx=15)
        self.intelligence_modifier_label.grid(column=5, row=7, padx=15)
        self.charisma_modifier_label.grid(column=6, row=7, padx=15)

        self.menu_button.grid(column=0, row=0, padx=50)
        self.save_character_button.grid(column=1, row=0, padx=50)
        self.restart_button.grid(column=2, row=0, padx=50)

        self.char_question = Frame(window)
        self.which = Label(self.char_question, text='Which Character Would You Like to See')
        self.question_selection = ttk.Combobox(self.char_question)
        self.question_selection['values'] = characters
        self.question_selection.state(['readonly'])
        self.select_button = Button(self.char_question, text='Select', command=self.see_character)
        self.which_menu_button = Button(self.char_question, text='Menu', command=self.menu)

        self.which.pack(side=TOP, pady=10)
        self.question_selection.pack(side=TOP, pady=15)
        self.select_button.pack(side=LEFT, pady=20, padx=15)
        self.which_menu_button.pack(side=RIGHT, pady=20, padx=15)

        # Start of See character Screen
        self.char_window = Frame(window)
        self.char_frame_top = Frame(self.char_window)
        self.char_frame_bottom = Frame(self.char_window)
        self.char_menu = Button(self.char_window, text='Menu', command=self.menu)

        self.nombre = StringVar()
        self.char = StringVar()
        self.race = StringVar()
        self.str = StringVar()
        self.dex = StringVar()
        self.con = StringVar()
        self.int = StringVar()
        self.wis = StringVar()
        self.cha = StringVar()
        self.chara_level = StringVar()

        self.char_name = Label(self.char_frame_top, textvariable=self.nombre)
        self.char_name_label = Label(self.char_frame_top, text='Name')
        self.chara_class_label = Label(self.char_frame_top, text='Class')
        self.char_race_label = Label(self.char_frame_top, text='Race')
        self.chara_class = Label(self.char_frame_top, textvariable=self.char)
        self.char_race = Label(self.char_frame_top, textvariable=self.race)
        self.char_level_label = Label(self.char_frame_top, text='Level')
        self.char_level = Label(self.char_frame_top, textvariable=self.chara_level)

        self.str_label = Label(self.char_frame_bottom, text='Str')
        self.dex_label = Label(self.char_frame_bottom, text='Dex')
        self.con_label = Label(self.char_frame_bottom, text='Con')
        self.wis_label = Label(self.char_frame_bottom, text='Wis')
        self.int_label = Label(self.char_frame_bottom, text='Int')
        self.cha_label = Label(self.char_frame_bottom, text='Cha')

        self.char_str = Label(self.char_frame_bottom, textvariable=self.str)
        self.char_dex = Label(self.char_frame_bottom, textvariable=self.dex)
        self.char_con = Label(self.char_frame_bottom, textvariable=self.con)
        self.char_int = Label(self.char_frame_bottom, textvariable=self.int)
        self.char_wis = Label(self.char_frame_bottom, textvariable=self.wis)
        self.char_cha = Label(self.char_frame_bottom, textvariable=self.cha)

        self.str_modi = StringVar()
        self.dex_modi = StringVar()
        self.con_modi = StringVar()
        self.int_modi = StringVar()
        self.wis_modi = StringVar()
        self.cha_modi = StringVar()

        self.char_str_mod = Label(self.char_frame_bottom, textvariable=self.str_modi)
        self.char_dex_mod = Label(self.char_frame_bottom, textvariable=self.dex_modi)
        self.char_con_mod = Label(self.char_frame_bottom, textvariable=self.con_modi)
        self.char_int_mod = Label(self.char_frame_bottom, textvariable=self.int_modi)
        self.char_wis_mod = Label(self.char_frame_bottom, textvariable=self.wis_modi)
        self.char_cha_mod = Label(self.char_frame_bottom, textvariable=self.cha_modi)

        self.char_name.grid(column=0, row=1, padx=5)
        self.char_name_label.grid(column=0, row=0, padx=5)
        self.chara_class_label.grid(column=1, row=0, padx=5)
        self.char_race_label.grid(column=2, row=0, padx=5)
        self.chara_class.grid(column=1, row=1, padx=5)
        self.char_race.grid(column=2, row=1, padx=5)

        self.str_label.grid(column=0, row=0, padx=5)
        self.dex_label.grid(column=1, row=0, padx=5)
        self.con_label.grid(column=2, row=0, padx=5)
        self.wis_label.grid(column=3, row=0, padx=5)
        self.int_label.grid(column=4, row=0, padx=5)
        self.cha_label.grid(column=5, row=0, padx=5)

        self.char_str.grid(column=0, row=1, padx=5)
        self.char_dex.grid(column=1, row=1, padx=5)
        self.char_con.grid(column=2, row=1, padx=5)
        self.char_int.grid(column=3, row=1, padx=5)
        self.char_wis.grid(column=4, row=1, padx=5)
        self.char_cha.grid(column=5, row=1, padx=5)

        self.char_str_mod.grid(column=0, row=2, padx=5)
        self.char_dex_mod.grid(column=1, row=2, padx=5)
        self.char_con_mod.grid(column=2, row=2, padx=5)
        self.char_int_mod.grid(column=3, row=2, padx=5)
        self.char_wis_mod.grid(column=4, row=2, padx=5)
        self.char_cha_mod.grid(column=5, row=2, padx=5)

        self.blank_frame = Frame(self.char_window)

        self.blank_frame.grid(column=0, row=0, columnspan=3, rowspan=3)
        self.char_frame_top.grid(column=3, row=3, padx=5)
        self.char_frame_bottom.grid(column=4, row=4, padx=5)
        self.char_menu.grid(column=5, row=5, padx=5)

    def add_character(self):
        self.main_frame.forget()
        self.window.geometry('650x250')
        center(self.window)
        self.master.grid()

    def racial_bonus(self, event):
        race = self.race_selection.get()
        if race == 'Dragonborn':
            self.str_bonus.set("+2")
            self.dex_bonus.set("+0")
            self.con_bonus.set("+0")
            self.wis_bonus.set("+0")
            self.int_bonus.set("+0")
            self.cha_bonus.set("+1")
        elif race == 'Dwarf':
            self.str_bonus.set("+2")
            self.dex_bonus.set("+0")
            self.con_bonus.set("+2")
            self.wis_bonus.set("+0")
            self.int_bonus.set("+0")
            self.cha_bonus.set("+0")
        elif race == 'Elf':
            self.str_bonus.set("+0")
            self.dex_bonus.set("+2")
            self.con_bonus.set("+0")
            self.wis_bonus.set("+0")
            self.int_bonus.set("+1")
            self.cha_bonus.set("+0")
        elif race == 'Gnome':
            self.str_bonus.set("+0")
            self.dex_bonus.set("+1")
            self.con_bonus.set("+0")
            self.wis_bonus.set("+0")
            self.int_bonus.set("+2")
            self.cha_bonus.set("+0")
        elif race == 'Half-elf':
            self.str_bonus.set("+0")
            self.dex_bonus.set("+1")
            self.con_bonus.set("+1")
            self.wis_bonus.set("+0")
            self.int_bonus.set("+0")
            self.cha_bonus.set("+2")
        elif race == 'Halfling':
            self.str_bonus.set("+0")
            self.dex_bonus.set("+2")
            self.con_bonus.set("+0")
            self.wis_bonus.set("+0")
            self.int_bonus.set("+0")
            self.cha_bonus.set("+1")
        elif race == 'Half-Orc':
            self.str_bonus.set("+2")
            self.dex_bonus.set("+0")
            self.con_bonus.set("+1")
            self.wis_bonus.set("+0")
            self.int_bonus.set("+0")
            self.cha_bonus.set("+0")
        elif race == 'Human':
            self.str_bonus.set("+1")
            self.dex_bonus.set("+1")
            self.con_bonus.set("+1")
            self.wis_bonus.set("+1")
            self.int_bonus.set("+1")
            self.cha_bonus.set("+1")
        elif race == 'Tiefling':
            self.str_bonus.set("+0")
            self.dex_bonus.set("+0")
            self.con_bonus.set("+0")
            self.wis_bonus.set("+0")
            self.int_bonus.set("+1")
            self.cha_bonus.set("+2")
        self.strength_update_values('')
        self.dexterity_update_values('')
        self.constitution_update_values('')
        self.wisdom_update_values('')
        self.intelligence_update_values('')
        self.charisma_update_values('')

    def strength_update_values(self, event):
        try:
            strength = int(self.strength_entry.get())
            if self.str_prev != '--' and self.str_prev not in self.hidden_stats:
                self.hidden_stats.append(self.str_prev)
                self.charisma_entry['values'] = self.hidden_stats
                self.hidden_stats.remove('--')
                self.hidden_stats.sort(reverse=True)
                self.hidden_stats.insert(0, '--')
                self.strength_entry['values'] = self.hidden_stats
                self.dexterity_entry['values'] = self.hidden_stats
                self.constitution_entry['values'] = self.hidden_stats
                self.wisdom_entry['values'] = self.hidden_stats
                self.intelligence_entry['values'] = self.hidden_stats
                self.charisma_entry['values'] = self.hidden_stats
        except ValueError:
            if self.str_prev == '--':
                pass
            else:
                self.hidden_stats.append(int(self.str_prev))
                self.hidden_stats.remove('--')
                self.hidden_stats.sort(reverse=True)
                self.hidden_stats.insert(0, '--')
                self.strength_entry['values'] = self.hidden_stats
                self.dexterity_entry['values'] = self.hidden_stats
                self.constitution_entry['values'] = self.hidden_stats
                self.wisdom_entry['values'] = self.hidden_stats
                self.intelligence_entry['values'] = self.hidden_stats
                self.charisma_entry['values'] = self.hidden_stats
                self.str_prev = '--'
            self.str_mod.set('+0')
        else:
            self.str_prev = strength
            try:
                self.hidden_stats.remove(strength)
                self.strength_entry['values'] = self.hidden_stats
                self.dexterity_entry['values'] = self.hidden_stats
                self.constitution_entry['values'] = self.hidden_stats
                self.wisdom_entry['values'] = self.hidden_stats
                self.intelligence_entry['values'] = self.hidden_stats
                self.charisma_entry['values'] = self.hidden_stats
            except ValueError:
                pass
            bonus = 0
            holder = self.str_bonus.get()
            if holder == '+0':
                bonus = 0
            elif holder == '+1':
                bonus = 1
            elif holder == "+2":
                bonus = 2
            self.str_total.set(f'{strength + bonus}')
            modi = strength + bonus
            strength_mod = rolling.modifier(modi)
            if strength_mod < 0:
                self.str_mod.set(f'{strength_mod}')
            else:
                self.str_mod.set(f'+{strength_mod}')

    def dexterity_update_values(self, event):
        try:
            dexterity = int(self.dexterity_entry.get())
            if self.dex_prev != '--' and self.dex_prev not in self.hidden_stats:
                self.hidden_stats.append(self.dex_prev)
                self.charisma_entry['values'] = self.hidden_stats
                self.hidden_stats.remove('--')
                self.hidden_stats.sort(reverse=True)
                self.hidden_stats.insert(0, '--')
                self.strength_entry['values'] = self.hidden_stats
                self.dexterity_entry['values'] = self.hidden_stats
                self.constitution_entry['values'] = self.hidden_stats
                self.wisdom_entry['values'] = self.hidden_stats
                self.intelligence_entry['values'] = self.hidden_stats
                self.charisma_entry['values'] = self.hidden_stats
        except ValueError:
            if self.dex_prev == '--':
                pass
            else:
                self.hidden_stats.append(int(self.dex_prev))
                self.hidden_stats.remove('--')
                self.hidden_stats.sort(reverse=True)
                self.hidden_stats.insert(0, '--')
                self.strength_entry['values'] = self.hidden_stats
                self.dexterity_entry['values'] = self.hidden_stats
                self.constitution_entry['values'] = self.hidden_stats
                self.wisdom_entry['values'] = self.hidden_stats
                self.intelligence_entry['values'] = self.hidden_stats
                self.charisma_entry['values'] = self.hidden_stats
                self.dex_prev = '--'
            self.dex_mod.set('+0')
        else:
            self.dex_prev = dexterity

            try:
                self.hidden_stats.remove(dexterity)
                self.strength_entry['values'] = self.hidden_stats
                self.dexterity_entry['values'] = self.hidden_stats
                self.constitution_entry['values'] = self.hidden_stats
                self.wisdom_entry['values'] = self.hidden_stats
                self.intelligence_entry['values'] = self.hidden_stats
                self.charisma_entry['values'] = self.hidden_stats
            except ValueError:
                pass
            bonus = 0
            holder = self.dex_bonus.get()
            if holder == '+0':
                bonus = 0
            elif holder == '+1':
                bonus = 1
            elif holder == "+2":
                bonus = 2
            self.dex_total.set(f'{dexterity + bonus}')
            modi = dexterity + bonus
            dexterity_mod = rolling.modifier(modi)
            if dexterity_mod < 0:
                self.dex_mod.set(f'{dexterity_mod}')
            else:
                self.dex_mod.set(f'+{dexterity_mod}')

    def constitution_update_values(self, event):
        try:
            constitution = int(self.constitution_entry.get())
            if self.con_prev != '--' and self.con_prev not in self.hidden_stats:
                self.hidden_stats.append(self.con_prev)
                self.charisma_entry['values'] = self.hidden_stats
                self.hidden_stats.remove('--')
                self.hidden_stats.sort(reverse=True)
                self.hidden_stats.insert(0, '--')
                self.strength_entry['values'] = self.hidden_stats
                self.dexterity_entry['values'] = self.hidden_stats
                self.constitution_entry['values'] = self.hidden_stats
                self.wisdom_entry['values'] = self.hidden_stats
                self.intelligence_entry['values'] = self.hidden_stats
                self.charisma_entry['values'] = self.hidden_stats
        except ValueError:
            if self.con_prev == '--':
                pass
            else:
                self.hidden_stats.append(int(self.con_prev))
                self.hidden_stats.remove('--')
                self.hidden_stats.sort(reverse=True)
                self.hidden_stats.insert(0, '--')
                self.strength_entry['values'] = self.hidden_stats
                self.dexterity_entry['values'] = self.hidden_stats
                self.constitution_entry['values'] = self.hidden_stats
                self.wisdom_entry['values'] = self.hidden_stats
                self.intelligence_entry['values'] = self.hidden_stats
                self.charisma_entry['values'] = self.hidden_stats
                self.con_prev = '--'
            self.con_mod.set('+0')
        else:
            self.con_prev = constitution
            try:
                self.hidden_stats.remove(constitution)
                self.strength_entry['values'] = self.hidden_stats
                self.dexterity_entry['values'] = self.hidden_stats
                self.constitution_entry['values'] = self.hidden_stats
                self.wisdom_entry['values'] = self.hidden_stats
                self.intelligence_entry['values'] = self.hidden_stats
                self.charisma_entry['values'] = self.hidden_stats
            except ValueError:
                pass
            bonus = 0
            holder = self.con_bonus.get()
            if holder == '+0':
                bonus = 0
            elif holder == '+1':
                bonus = 1
            elif holder == "+2":
                bonus = 2
            self.con_total.set(f'{constitution + bonus}')
            modi = constitution + bonus
            constitution_mod = rolling.modifier(modi)
            if constitution_mod < 0:
                self.con_mod.set(f'{constitution_mod}')
            else:
                self.con_mod.set(f'+{constitution_mod}')

    def wisdom_update_values(self, event):
        try:
            wisdom = int(self.wisdom_entry.get())
            if self.wis_prev != '--' and self.wis_prev not in self.hidden_stats:
                self.hidden_stats.append(self.wis_prev)
                self.charisma_entry['values'] = self.hidden_stats
                self.hidden_stats.remove('--')
                self.hidden_stats.sort(reverse=True)
                self.hidden_stats.insert(0, '--')
                self.strength_entry['values'] = self.hidden_stats
                self.dexterity_entry['values'] = self.hidden_stats
                self.constitution_entry['values'] = self.hidden_stats
                self.wisdom_entry['values'] = self.hidden_stats
                self.intelligence_entry['values'] = self.hidden_stats
                self.charisma_entry['values'] = self.hidden_stats
        except ValueError:
            if self.wis_prev == '--':
                pass
            else:
                self.hidden_stats.append(int(self.wis_prev))
                self.hidden_stats.remove('--')
                self.hidden_stats.sort(reverse=True)
                self.hidden_stats.insert(0, '--')
                self.strength_entry['values'] = self.hidden_stats
                self.dexterity_entry['values'] = self.hidden_stats
                self.constitution_entry['values'] = self.hidden_stats
                self.wisdom_entry['values'] = self.hidden_stats
                self.intelligence_entry['values'] = self.hidden_stats
                self.charisma_entry['values'] = self.hidden_stats
                self.wis_prev = '--'
            self.wis_mod.set('+0')
        else:
            self.wis_prev = wisdom
            try:
                self.hidden_stats.remove(wisdom)
                self.strength_entry['values'] = self.hidden_stats
                self.dexterity_entry['values'] = self.hidden_stats
                self.constitution_entry['values'] = self.hidden_stats
                self.wisdom_entry['values'] = self.hidden_stats
                self.intelligence_entry['values'] = self.hidden_stats
                self.charisma_entry['values'] = self.hidden_stats
            except ValueError:
                pass
            bonus = 0
            holder = self.wis_bonus.get()
            if holder == '+0':
                bonus = 0
            elif holder == '+1':
                bonus = 1
            elif holder == "+2":
                bonus = 2
            self.wis_total.set(f'{wisdom + bonus}')
            modi = wisdom + bonus
            wisdom_mod = rolling.modifier(modi)
            if wisdom_mod < 0:
                self.wis_mod.set(f'{wisdom_mod}')
            else:
                self.wis_mod.set(f'+{wisdom_mod}')

    def intelligence_update_values(self, event):
        try:
            if self.int_prev != '--' and self.int_prev not in self.stats:
                self.hidden_stats.append(self.int_prev)
            intelligence = int(self.intelligence_entry.get())
        except ValueError:
            if self.int_prev == '--':
                pass
            else:
                self.hidden_stats.append(int(self.int_prev))
                self.hidden_stats.remove('--')
                self.hidden_stats.sort(reverse=True)
                self.hidden_stats.insert(0, '--')
                self.strength_entry['values'] = self.hidden_stats
                self.dexterity_entry['values'] = self.hidden_stats
                self.constitution_entry['values'] = self.hidden_stats
                self.wisdom_entry['values'] = self.hidden_stats
                self.intelligence_entry['values'] = self.hidden_stats
                self.charisma_entry['values'] = self.hidden_stats
                self.int_prev = '--'
            self.int_mod.set('+0')
        else:
            self.int_prev = intelligence
            try:
                self.hidden_stats.remove(intelligence)
                self.strength_entry['values'] = self.hidden_stats
                self.dexterity_entry['values'] = self.hidden_stats
                self.constitution_entry['values'] = self.hidden_stats
                self.wisdom_entry['values'] = self.hidden_stats
                self.intelligence_entry['values'] = self.hidden_stats
                self.charisma_entry['values'] = self.hidden_stats

            except ValueError:
                pass
            bonus = 0
            holder = self.int_bonus.get()
            if holder == '+0':
                bonus = 0
            elif holder == '+1':
                bonus = 1
            elif holder == "+2":
                bonus = 2
            self.int_total.set(f'{intelligence + bonus}')
            modi = intelligence + bonus
            intelligence_mod = rolling.modifier(modi)
            if intelligence_mod < 0:
                self.int_mod.set(f'{intelligence_mod}')
            else:
                self.int_mod.set(f'+{intelligence_mod}')

    def charisma_update_values(self, event):
        try:
            charisma = int(self.charisma_entry.get())
            if self.cha_prev != '--' and self.cha_prev not in self.hidden_stats:
                self.hidden_stats.append(self.cha_prev)
                self.charisma_entry['values'] = self.hidden_stats
                self.hidden_stats.remove('--')
                self.hidden_stats.sort(reverse=True)
                self.hidden_stats.insert(0, '--')
                self.strength_entry['values'] = self.hidden_stats
                self.dexterity_entry['values'] = self.hidden_stats
                self.constitution_entry['values'] = self.hidden_stats
                self.wisdom_entry['values'] = self.hidden_stats
                self.intelligence_entry['values'] = self.hidden_stats
                self.charisma_entry['values'] = self.hidden_stats
        except ValueError:
            if self.cha_prev == '--':
                pass
            else:
                self.hidden_stats.append(int(self.cha_prev))
                self.hidden_stats.remove('--')
                self.hidden_stats.sort(reverse=True)
                self.hidden_stats.insert(0, '--')
                self.strength_entry['values'] = self.hidden_stats
                self.dexterity_entry['values'] = self.hidden_stats
                self.constitution_entry['values'] = self.hidden_stats
                self.wisdom_entry['values'] = self.hidden_stats
                self.intelligence_entry['values'] = self.hidden_stats
                self.charisma_entry['values'] = self.hidden_stats
                self.cha_prev = '--'
            self.cha_mod.set('+0')
        else:
            self.cha_prev = charisma
            try:
                self.hidden_stats.remove(charisma)
                self.strength_entry['values'] = self.hidden_stats
                self.dexterity_entry['values'] = self.hidden_stats
                self.constitution_entry['values'] = self.hidden_stats
                self.wisdom_entry['values'] = self.hidden_stats
                self.intelligence_entry['values'] = self.hidden_stats
                self.charisma_entry['values'] = self.hidden_stats

            except ValueError:
                pass
            bonus = 0
            holder = self.cha_bonus.get()
            if holder == '+0':
                bonus = 0
            elif holder == '+1':
                bonus = 1
            elif holder == "+2":
                bonus = 2
            self.cha_total.set(f'{charisma + bonus}')
            modi = charisma + bonus
            charisma_mod = rolling.modifier(modi)
            if charisma_mod < 0:
                self.cha_mod.set(f'{charisma_mod}')
            else:
                self.cha_mod.set(f'+{charisma_mod}')

    def see_character(self):
        name = self.question_selection.get()
        file = open(name + '.csv', 'r')
        read = csv.reader(file)
        stats = []
        for i in read:
            stats = {'Name': name, 'Strength': int(i[1]), 'Dexterity': int(i[2]), 'Constitution': int(i[3]),
                     'Intelligence': int(i[4]), 'Wisdom': int(i[5]), 'Charisma': int(i[6]), 'Level': i[7],
                     'class': i[8], 'race': i[9]}
        print(stats)
        self.nombre.set(stats['Name'])
        self.str.set(stats['Strength'])
        self.dex.set(stats['Dexterity'])
        self.con.set(stats['Constitution'])
        self.wis.set(stats['Wisdom'])
        self.int.set(stats['Intelligence'])
        self.cha.set(stats['Charisma'])
        self.chara_level.set(stats['Level'])
        self.char.set(stats['class'])
        self.race.set(stats['race'])

        self.char_question.forget()
        self.char_window.grid()

    def restart(self):
        new_rolls = rolling.roll_stats()
        new_rolls.sort(reverse=True)
        hidden_list = new_rolls[:]
        self.hidden_stats = hidden_list
        hidden_list.insert(0, '--')
        self.rolls.set(f'{new_rolls}')
        self.name.delete(0, END)
        self.level.delete(0,END)
        self.strength_entry.set('--')
        self.dexterity_entry.set('--')
        self.constitution_entry.set('--')
        self.wisdom_entry.set('--')
        self.intelligence_entry.set('--')
        self.charisma_entry.set('--')
        self.str_mod.set('+0')
        self.dex_mod.set('+0')
        self.con_mod.set('+0')
        self.wis_mod.set('+0')
        self.int_mod.set('+0')
        self.cha_mod.set('+0')
        self.str_bonus.set('+0')
        self.dex_bonus.set('+0')
        self.con_bonus.set('+0')
        self.wis_bonus.set('+0')
        self.int_bonus.set('+0')
        self.cha_bonus.set('+0')
        self.str_total.set('')
        self.dex_total.set('')
        self.con_total.set('')
        self.wis_total.set('')
        self.int_total.set('')
        self.cha_total.set('')
        self.str_prev = '--'
        self.dex_prev = '--'
        self.con_prev = '--'
        self.wis_prev = '--'
        self.int_prev = '--'
        self.cha_prev = '--'
        self.race_selection.set('')
        self.char_class.set('')
        self.strength_entry['values'] = hidden_list
        self.dexterity_entry['values'] = hidden_list
        self.constitution_entry['values'] = hidden_list
        self.wisdom_entry['values'] = hidden_list
        self.intelligence_entry['values'] = hidden_list
        self.charisma_entry['values'] = hidden_list

    def save_character(self):
        # Files should be written as Name, Str, Dex, Con, Int, Wis, Cha, lvl, class, race
        file = open(self.name.get() + '.csv', 'w', newline='')
        weird = open('files.txt', 'a')
        stats = {'Name': self.name.get().strip(), "Strength": self.str_total.get().strip(),
                 'Dexterity': self.dex_total.get().strip(),
                 'Constitution': self.con_total.get().strip(), 'Intelligence': self.int_total.get().strip(),
                 'Wisdom': self.wis_total.get().strip(), 'Charisma': self.cha_total.get().strip(),
                 "Level": self.level.get().strip(),
                 'Class': self.char_class.get().strip(), "Race": self.race_selection.get().strip()}
        fields = ['Name', 'Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma', 'Level',
                  'Class', 'Race']
        write = csv.DictWriter(file, fieldnames=fields)
        write.writerow(stats)
        weird.write(str(self.name.get()) + '\n')
        file.close()
        weird.close()
        self.restart()
        self.menu()
        update()
        self.question_selection['values'] = characters

    def menu(self):
        self.master.grid_remove()
        self.char_window.grid_remove()
        self.char_question.forget()
        self.main_frame.pack()
        self.window.geometry('500x150')
        center(self.window)

    def question(self):
        update()
        self.main_frame.forget()
        self.char_question.pack()


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


def update():
    characters.clear()
    f = open('files.txt', 'r')
    c = 0
    for i in f.readlines():
        line = i.strip()
        line.replace(' ', '.csv')
        line = line.strip()
        characters.insert(c, line)
        c += 1
