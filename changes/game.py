
""" The main GUI """
from classes import *
from functions import *
from maps import *
from items import *
from time import sleep

player = Actor()
input_cut = []
def void():
	pass

user_input = ''
current_stage = void
first_run = True

def rtn_pressed(event):
	global user_input
	global current_stage
	user_input = get_input()

	if user_input == '':
		pass
	elif user_input == 'back':
		main_menu()
		current_stage = main_menu
		clear_input_console()

	#TESTING HP BAR
	elif user_input == 'attack':
		player.stats['health']['curh'] -= 1
		clear_input_console()
		update_hp_bar()
	else:
		current_stage()
		clear_input_console()

def update_text(location, input):
	location.config(state = NORMAL)
	location.delete(1.0, END)
	location.insert(END, input)
	location.config(state = DISABLED)

def add_txt(location, input):
	location.config(state = NORMAL)
	location.insert(END, input)
	location.config(state = DISABLED)

def get_txt(location):
	location.config(state = NORMAL)
	return location.get(1.0, END)
	location.config(state = DISABLED)

def get_input():

	return console.get()

def clear_input_console():

	console.delete(0, END)


def update_inv_display():
	update_txt = ""
	update_txt += '      [INVENTORY]\n\n'
	for item in player.inv:
		update_txt += '  ---  ' + item.id + '\n'
	update_text(inv_txt, update_txt)

def update_stat_display():
	update_txt = ""

	update_txt += '      [STATISTICS]\n\n'
	for desc, amount in player.stats['special'].items():
		num_spaces = 13 - (len(desc) + 2)
		spaces = ''
		for a in range(0,num_spaces):
			spaces += ' '

		update_txt += ' ' + desc.upper() + ': '+ spaces + str(amount) + '\n'



	update_text(stats_txt, update_txt)

def update_hp_bar():
	update_txt = ""
	player_vitals = player.stats['health']
	player_health_perc = player_vitals['curh']/player_vitals['maxh']

	count_hash = player_vitals['curh']


	hashes = ''
	for i in range(0,int(count_hash)):
		hashes += '♥'

	update_txt += hashes

	update_text(hp_entry, update_txt)


#displays the main menu of the game
def main_menu():
	global user_input
	global current_stage

	#Display
	out_console_txt = ""
	choice_console_txt = ""
	out_console_txt += draw_ascii('welcome.txt') + '\n'
	out_console_txt += '\n\n\n\n'
	out_console_txt += ' Welcome ' + player.name + '\t\t\t\t\t\t\t'
	choice_console_txt += ' Select:\n\n\t\t\ta.New Game\n\t\t\tb.Load Game\n\t\t\tc.Exit'
	update_text(out_console, out_console_txt)
	update_text(choice_console, choice_console_txt)


	normalised_input = user_input
	user_input = ""

	if normalised_input == 'a':
		new_game()
		current_stage = new_game
		#Start game
	elif normalised_input== 'b':
		load_game()
		current_stage = load_game

	elif normalised_input == 'c':
		quit()



def load_game():

	update_text(out_console, 'Load game menu')
	update_text(choice_console, 'Updated')




def new_game():
	update_text(out_console, draw_ascii('newgame.txt'))
	update_text(choice_console,'Time to select those stats!')



def refresh():
	update_stat_display()
	update_inv_display()
	update_hp_bar()
	update_text(out_console, "")
	update_text(choice_console, "")


#TK gui window
main = Tk ()
main.resizable(width = False, height = False)
main.title('Taffi Warz')

bg_image = PhotoImage(file = "bg3.png")
map_sprite = PhotoImage(file = "map.png")

#window background
frame = Label(main, image = bg_image)
frame.place(x=0, y=0, relwidth=1, relheight=1)


#creating each widget
console = Entry(main, bg = '#6a8c87', fg = 'black', width = 88)
map_label = Label(main,  image = map_sprite)
inv_txt = Text(main, bg = '#262820',fg = 'white', width = 25, height = 15)
stats_txt = Text(main, bg = '#262820', fg = 'green', width = 25, height = 15)
hp_entry = Text(stats_txt, bg = 'black', fg = 'red', font=("Helvetica", 15))
out_console = Text(main, bg = 'black', fg = 'yellow', width = 100)
choice_console = Text(main, bg = 'black', fg = 'yellow', width = 100, height = 10)

#Display and layout of all widgets
console.grid(row = 4, column = 1, columnspan = 3)
map_label.grid(row = 1, column = 1)
inv_txt.grid(row = 1, column = 3, rowspan = 2)
stats_txt.grid(row = 2, column = 1)
hp_entry.place(x=0, y=0, relwidth =1, relheight = 0.1)
out_console.grid(row = 1, column = 2, rowspan = 2)
choice_console.grid(row = 3, column = 1, columnspan = 3)

console.bind('<Return>', rtn_pressed)
inv_txt.config(state = DISABLED)
choice_console.config(state = DISABLED)
out_console.config(state = DISABLED)
stats_txt.config(state = DISABLED)
hp_entry.config(state = DISABLED)

#Set focus on the console
console.focus_set()

#Start
if first_run:
	current_stage = main_menu
	first_run = False

refresh()
current_stage()



main.mainloop()
