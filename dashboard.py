import login
import query_db as query

def dashboard(username,password):
	account_number, balance, fullname, email = query.query_db(query.customer_info_query,username,password)[0]
	print('_'*85)
	print('|','Welcome to Teejay\'s Bank'.center(82),'|')
	print('_'*85)
	print('|','You\'re in!!!' .center(82),'|')	
	print('|', ' '*82, '|')
	print('|', ' '*82, '|')
	print('|', ' '*2, 'NAME:  {}'.format(fullname),' ')
	print(''*15, end = '')
	print('|',' '*82, '|')
	print('|',' '*82, '|')
	print('|','\tAccount Number\t{}'.format(account_number),'\t' 'Account Balance:\t{}'.format(balance),' '*28,'|')
	print(('-')*48)
	print()
	print('How can we help you today?')
	print('-'*20)
	print()
	print('Check Balance     1', '\t\t', 'Transfer Money    2')
	print()
	print('Cash Withdrawal   3', '\t\t', 'Open New Account  4')
	print()
	print('|','-'*80, '|')
