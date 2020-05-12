import login
import query_db as query

def dashboard(username,password):
	account_number, balance, fullname, email = query.query_db(query.customer_info_query,username,password)[0]
	print('_'*85)
	print('|','Welcome to Teejay\'s Bank'.center(82),'|')
	print('|','_'*82,'|')
	print('|','You\'re in!!!' .center(82),'|')	
	print('|', ' '*82, '|')
	print('|', ' '*82, '|')
	print('|', '\tNAME:  {}'.format(fullname),' '*52,'|')
	print('|',' '*82, '|')
	print('|',' '*82, '|')
	print('|','\tAccount Number\t{}'.format(account_number),'\t' 'Account Balance:\t{}'.format(balance),' '*22,'|')
	print('|','-'*82,'|')
	print('|',' '*82, '|')
	print('|','\tHow can we help you today?',' '*49, '|')
	print('|','-'*82,'|')
	print('|',' '*82,'|')
	print('|','\tCheck Balance:     1', '\t\t\t', '\tTransfer Money:    2',' '*7,'|')
	print('|',' '*82,'|')
	print('|','\tCash Withdrawal:   3', '\t\t\t', '\tOpen New Account:  4',' '*7,'|')
	print('|',' '*82,'|')
	print('-'*85)
