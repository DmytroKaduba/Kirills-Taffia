import time
from functions import *
from tkinter import *


""" These are the classes which are the structures for different objects in the game """

class Actor():
	def __init__(self):
		self.name = 'Blank_name'
		self.inv = []
		self.stats = {
			'special': {'str':0, 'per':0, 'end':0, 'cha':0, 'int':0, 'agi':0, 'luc':0},
			'health': {'curh':0, 'maxh':0},
			'level': {'exp':0,'lvl':0,'nxt_lvl':0, 'nxt_exp':0}
		}

		self.stats['special'] = {'str':1, 'per':1, 'end':1, 'cha':1, 'int':1, 'agi':1, 'luc':1}
		self.calc_stats()

	def calc_stats(self):
		cur_maxh = self.stats['health']['maxh']
		cur_curh = self.stats['health']['curh']
		new_maxh = self.stats['special']['str'] * 8
		new_curh = cur_curh + (new_maxh - cur_maxh)
		self.stats['health'] = {'maxh': new_maxh, 'curh': new_curh}

	def take(self, item):
		self.inv.append(item)

	def drop(self):
		self.inv.remove(item)


"""The room class. Rooms will for maps which will be assigned to levels. The rooms will determine the story. """

class Room():
	def __init__(self, name, des, exits, items):
		self.name = name
		self.description = des
		self.exits = exits
		self.items = items

class gui():
	#constructor called on creation
	def __init__(self, player):
		pass

class GradientFrame(Canvas):
	'''A gradient frame which uses a canvas to draw the background'''
	def __init__(self, parent, borderwidth=1, relief="sunken"):
		Canvas.__init__(self, parent, borderwidth=borderwidth, relief=relief)
		self._color1 = '#152018'
		self._color2 = '#344e3a'
		self.bind("<Configure>", self._draw_gradient)

	def _draw_gradient(self, event=None):
		'''Draw the gradient'''
		self.delete("gradient")
		width = self.winfo_width()
		height = self.winfo_height()
		limit = width
		(r1,g1,b1) = self.winfo_rgb(self._color1)
		(r2,g2,b2) = self.winfo_rgb(self._color2)
		r_ratio = float(r2-r1) / limit
		g_ratio = float(g2-g1) / limit
		b_ratio = float(b2-b1) / limit

		for i in range(limit):
			nr = int(r1 + (r_ratio * i))
			ng = int(g1 + (g_ratio * i))
			nb = int(b1 + (b_ratio * i))
			color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
			self.create_line(i,0,i,height, tags=("gradient",), fill=color)
		self.lower("gradient")

class Item():
	def __init__(self, id, name, description):
		self.id = id
		self.name = name
		self.description = description

	def inspect():
		#Print out name, description and hints in narration section
		pass
