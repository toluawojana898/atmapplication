import getpass as pas
import login
import welcome

def myATM():
	print('|','Welcome to Teejay\'s Bank'.center(82),'|')
	print('_'*85)
	action = int(input('Select 1 to login or 2 to create a new account'))
	while True:
		if action not in [1,2]:
			print('You should select 1 or 2')
			action = int(input('Select 1 to login or 2 to create a new account'))
			continue
		else:
			break
	if action == 1:
		userinput = input('Enter username:')
		pidkeys = pas.getpass(prompt='password: ')
		if login.enter_pass(userinput,pidkeys):
			welcome.dashboard(userinput,pidkeys)
	else:
		pass

myATM()
