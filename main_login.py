import getpass as pas
import login
import welcome
import deposit_cash as dep

def myATM():
	print('_'*85)
	print('|','Welcome to Teejay\'s Bank'.center(82),'|')
	print('|','_'*82,'|')
	action = int(input('Select 1 to login or 2 to create a new account: '))
	while True:
		if action not in [1,2]:
			print('You should select 1 or 2')
			action = int(input('Select 1 to login or 2 to create a new account: '))
			continue
		else:
			break
	if action == 1:
		print('This is the Login Page!')
		userinput = input('Enter username: ')
		pidkeys = pas.getpass(prompt='password: ')
		if login.enter_pass(userinput,pidkeys):
			welcome.dashboard(userinput,pidkeys)
			options = int(input('Enter your choice:1,2,3,4: '))
			while not True:
				if options in [1,2,3,4]:
					print('Select options 1 to 4.')
					options = int(input('Enter your choice:1,2,3,4: '))
					continue
			else:
				if options == 1:
					dep.cashAdd(userinput,pidkeys)
				if options == 2:
					dep.cashRemove(userinput,pidkeys)
				if options == 3:
					dep.transfercash(userinput,pidkeys)
	else:
		pass

myATM()
