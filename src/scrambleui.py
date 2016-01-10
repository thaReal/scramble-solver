#!/usr/bin/python

from Tkinter import *
import subprocess
import os
import time

GAME_MODE = 0

#---
class MainWindow(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.initialize()
		self.pack()
	
	def initialize(self):
		self.configure(background="#555753")
		
		Label(self, text="Word Streak Solver [v0.1]", font='arial 16 bold', 
		foreground='navy', background="#3465a4", relief=RAISED).grid(column=0,
		row=0, columnspan=4, ipadx=10, ipady=10)
		
		self.mselect = ModeSelect(self)
		self.mselect.grid(column=0, row=1, columnspan=4, sticky="EW", 
		padx=10, pady=10)
		self.status = StatusBar(self)
		self.status.grid(column=0, row=2, columnspan=4, sticky="SEW")
		
		
	def startSingleGame(self):
		self.mselect.destroy()
		self.status.setmsg("Single Game Mode Started!")
		self.gameframe = GameFrame(self)
		self.gameframe.grid(column=0, row=1, columnspan=4, padx=10, pady=10)
		
	def startTournament(self):
		self.mselect.destroy()
		self.status.setmsg("Tournament Mode Started!")
		
	def playSingleGame(self):
		pass	
		
	def loadDevice(self):
		pass
		
		
#---		
class ModeSelect(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.gamemode = 0
		self.modes = { 
				1: "Single Game",
				2: "Tournament"
		}
		self.initialize()
		
	def initialize(self):
		Label(self, text="Select mode:").grid(column=0, row=0, padx=5, pady=5)
		
		Button(self, text=self.modes[1], command=self.selectMode1).grid(row=1, 
		column=0, padx=10, pady=10)
		
		Button(self, text=self.modes[2], command=self.selectMode2).grid(row=2, 
		column=0, padx=10, pady=10)
		
		self.startButton = Button(self, text="Start", state='disabled', 
		command=self.start)
		self.startButton.grid(row=3, column=0, padx=10, pady=10)


	def selectMode1(self):
		self.gamemode = 1
		print "1"
		self.activateStart()

		
	def selectMode2(self):
		self.gamemode = 2
		print "2"
		self.activateStart()

		
	def activateStart(self):
		self.startButton['state'] = 'normal'
		self.startButton['foreground'] = 'green'
		
	def start(self):
		print "Start pressed"
		print str(self.gamemode)
		if self.gamemode == 1:
			self.parent.startSingleGame()
		elif self.gamemode == 2:
			self.parent.startTournament()
		
		

#---
class StatusBar(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.configure(relief=SUNKEN)
		self.msg = StringVar()
		self.msglbl = Label(self, textvar=self.msg)
		self.msglbl.pack(anchor='w')
		self.setmsg("Select Mode")
		
	def setmsg(self, message):
		self.msg.set(message)
		self.update()
	

#---
class GameFrame(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.initialize()
		self.printMessage('Console Loaded!')
		
	def initialize(self):
		self.console = Text(self, height=4, width=20, background='black',
		foreground='white')
		self.console.grid(column=0, row=0, columnspan=2, padx=10, pady=10)
		self.cline = 0
		
		self.display = Canvas(self, height=100, width=100)
		self.display.grid(column=2, row=0)
		
		self.startbutton = Button(self, text="Start", state='disabled')
		self.startbutton.grid(column=0, row=1, pady=10)
		
		
	def printMessage(self, message):
		self.console.insert((str(self.cline) + ".0"), message)
		self.cline += 1
		

if __name__=='__main__':
	root = Tk()
	app = MainWindow(root)
	app.mainloop()
