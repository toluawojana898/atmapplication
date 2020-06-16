import getpass as pas
import login
import welcome
import deposit_cash as dep
import query_db as qdb 
from datetime import date
import logging
import mysql.connector
from mysql.connector import errorcode

def myATM():
	print('_'*85)
	print('|','Welcome to Teejay\'s Bank'.center(82),'|')
	print('|','_'*82,'|')
	try:
		action = int(input('Select 1 to login or 2 to create a new account: '))
	except:
		action = 0
	while True:
		if action not in [1,2]:
			print('You should select 1 or 2')
			try:
				action = int(input('Select 1 to login or 2 to create a new account: '))
			except:
				action = 0
			continue
		else:
			break

	if action == 1:
		print('This is the Login Page!')
		userinput = input('Enter username: ')
		pidkeys = pas.getpass(prompt='password: ')
		if login.enter_pass(userinput,pidkeys):
			account_number, balance = welcome.dashboard(userinput,pidkeys)
			while True:
				try:
					print('Select options 1 to 4.')
					options = int(input('Enter your choice:1,2,3,4: '))
				except:
					options = 0
				if options in [1,2,3,4]:
					if options == 1:
						dep.cashAdd(userinput,pidkeys)
					if options == 2:
						dep.cashRemove(userinput,pidkeys)
					if options == 3:
						dep.transfercash(account_number)
					if options ==4:
						print('Thanks for banking with us, we are here to serve you better.')
						break
				else:
					try:
						print('Select options 1 to 4.')
						options = int(input('Enter your choice:1,2,3,4: '))
					except:
						options = 0
	else:
		dep.createNewAccount()
		try:
			action = int(input('Select 1 to login or 2 to create a new account: '))
		except:
			action = 0
		while True:
			if action not in [1,2]:
				print('You should select 1 or 2')
				try:
					action = int(input('Select 1 to login or 2 to create a new account: '))
				except:
					action = 0
				continue
			else:
				break
		
myATM()
