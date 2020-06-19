#!/usr/bin/env python
#-*- coding: utf-8 -*-

#This porogram creater for open your link in web browser
############################################
# L!nK~L!Fe  |______*|*______| @by Xenoret #
############################################

import webbrowser as web
import os

os.system('cls | clear') #Clrar terminal
os.system('chmod a+x ll.py')#start to terminal - ./ll.py

Python = {
	"Pythonorg": 'https://www.python.org/',
	"PyPi": 'https://pypi.org/',
	"Pep8RU": 'https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html',
	"Pep8EN": 'https://www.python.org/dev/peps/pep-0008/',
	"Pythontutor": 'http://www.pythontutor.com/visualize.html#mode=edit'
	}	

Work_searches = {
	"WorkUA": 'https://www.work.ua/jobs/',
	"RabotaUA": 'https://rabota.ua/ua/zapros',
	"JobsUA": 'https://jobs.ua/vacancy/search',
	"JoobleUA": 'https://ua.jooble.org/',
	"TrudUA": 'https://trud.ua/'
	}

Purchases = {
	"Aliexpress": 'https://aliexpress.ru/',
	"Olx": 'https://www.olx.ua/uk/',
	"PromUA": 'https://prom.ua/ua/',
	"RSTUA": 'https://rst.ua/',
	"AutorioUA": 'https://auto.ria.com/'
	}

Entertainment = {
	"Github": 'https://github.com',
	"YouTube": 'https://www.youtube.com',
	"Habr": 'https://habr.com/ru/',
	"Reddit": 'https://www.reddit.com/',
	"Translate": 'https://translate.google.com/?hl=uk#view=home&op=translate&sl=auto&tl=ru'
	}

Developer = {
	"GithubDEV": 'https://github.com/Xenoret',
	"CoubeDEV": 'https://coub.com/nikto780',
	}
#Exit
def bye():
	os.system('cls | clear')
	exit()

def Programing():
	temp = input('[1] - Pythonorg\n[2] - PyPi\n[3] - Pep8RU\n[4] - Pep8EN\n[5] - Pythontutor\n[0] - Display menu\n\nEnter your choice: ')
	if temp == '1':
		web.open_new_tab(Python['Pythonorg'])
	elif temp == '2':
		web.open_new_tab(Python['PyPi'])
	elif temp == '3':
		web.open_new_tab(Python['Pep8RU'])
	elif temp == '4':
		web.open_new_tab(Python['Pep8EN'])
	elif temp == '5':
		web.open_new_tab(Python['Pythontutor'])
	elif temp == '0':
		menu()
	elif temp == '00':
		bye()
	else:
		print("I don't understand you!")

def Work_searchess():
	temp = input('[1] - WorkUA\n[2] - RabotaUA\n[3] - JobsUA\n[4] - JoobleUA\n[5] - TrudUA\n[0] - Display menu\n\nEnter your choice: ')
	if temp == '1':
		web.open_new_tab(Work_searches['WorkUA'])
	elif temp == '2':
		web.open_new_tab(Work_searches['RabotaUA'])
	elif temp == '3':
		web.open_new_tab(Work_searches['JobsUA'])
	elif temp == '4':
		web.open_new_tab(Work_searches['JoobleUA'])
	elif temp == '5':
		web.open_new_tab(Work_searches['TrudUA'])
	elif temp == '0':
		menu()
	elif temp == '00':
		bye()
	else:
		print("I don't understand you!")

def Purchasess():
	temp = input('[1] - Aliexpress\n[2] - Olx\n[3] - PromUA\n[4] - RSTUA\n[5] - AutorioUA\n[0] - Display menu\n\nEnter your choice: ')
	if temp == '1':
		web.open_new_tab(Purchases['Aliexpress'])
	elif temp == '2':
		web.open_new_tab(Purchases['Olx'])
	elif temp == '3':
		web.open_new_tab(Purchases['PromUAt'])
	elif temp == '4':
		web.open_new_tab(Purchases['RSTUA'])
	elif temp == '5':
		web.open_new_tab(Purchases['AutorioUA'])
	elif temp == '0':
		menu()
	elif temp == '00':
		bye()
	else:
		print("I don't understand you!")

def Entertainments():
	temp = input('[1] - Github\n[2] - YouTube\n[3] - Habr\n[4] - Reddit\n[5] - Translate\n[0] - Display menu\n\nEnter your choice: ')
	if temp == '1':
		web.open_new_tab(Entertainment['Github'])
	elif temp == '2':
		web.open_new_tab(Entertainment['YouTube'])
	elif temp == '3':
		web.open_new_tab(Entertainment['Habr'])
	elif temp == '4':
		web.open_new_tab(Entertainment['Reddit'])
	elif temp == '5':
		web.open_new_tab(Entertainment['Translate'])
	elif temp == '0':
		menu()
	elif temp == '00':
		bye()
	else:
		print("I don't understand you!")

def Developers():
	temp = input('[1] - Github\n[2] - Coube\n[0] - Display menu\n\nEnter your choice: ')
	if temp == '1':
		web.open_new_tab(Developer['GithubDEV'])
	elif temp == '2':
		web.open_new_tab(Developer['CoubeDEV'])
	elif temp == '0':
		menu()
	elif temp == '00':
		bye()
	else:
		print("I don't understand you!")

def menu():
	os.system('cls | clear')
	print('L!nK~L!Fe - Discover your dream.\n')
	start = input('''\tMenu
[1] - Python programming
[2] - Work searches
[3] - Purchases
[4] - Entertainment
[5] - Developer
[0] - Display menu
[00] - Exit
\nEnter your choice: ''')
	if start == '1':
		os.system('cls | clear')
		Programing()
		menu()
	elif start == '2':
		os.system('cls | clear')
		Work_searchess()
		menu()
	elif start == '3':
		os.system('cls | clear')
		Purchasess()
		menu()
	elif start == '4':
		os.system('cls | clear')
		Entertainments()
		menu()
	elif start == 'pashal':
		print('Hey-Hey ~ You best coder <3')
	elif start == '5':
		os.system('cls | clear')
		Developers()
		menu()
	elif start == '00':
		bye()
	else:
		print("I don't understand you!")
menu()
