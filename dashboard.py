import login
import query_db as query

def dashboard(username,password):
	account_number, balance, fullname = query.query_db(query.display_customer_data_query,username,password)[0]
	print('_'*85)
	print('|','Welcome to Teejay\'s Bank'.center(82),'|')
	print('|','_'*82,'|')
	print('|','You\'re in!!!' .center(82),'|')	
	print('|', ' '*82, '|')
	print('|', ' '*82, '|')
	print('|', '\tNAME:  {}'.format(fullname),' '*56,'|')
	print('|',' '*82, '|')
	print('|',' '*82, '|')
	print('|','\tAccount Number\t{}'.format(account_number),'\t' 'Account Balance:\t{}'.format(balance),' '*20,'|')
	print('|','-'*82,'|')
	print('|',' '*82, '|')
	print('|','\tHow can we help you today?',' '*49, '|')
	print('|','-'*82,'|')
	print('|',' '*82,'|')
	print('|','\tCash Deposit:     1', '\t\t\t', '\tCash Withdrawal:    2',' '*6,'|')
	print('|',' '*82,'|')
	print('|','\tTransfer:         3', '\t\t\t', '\tExit:               4',' '*6,'|')
	print('|',' '*82,'|')
	print('-'*85)
	return (account_number, balance)
