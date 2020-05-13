import query_db as qdb
import login

def cashAdd(username,password):
	account_number, balance, __, __ = qdb.query_db(qdb.customer_info_query,username,password)[0]
	amount = int(input("Enter the amount you want to deposit: "))
	final_amount = int(balance) + amount
	qdb.query_db(qdb.transfer_to_query,amount,account_number)
	print('The deposit of {} was successful for account number {} you now have a balance of {}'.format(amount,account_number,final_amount))
	return True

def cashRemove(username,password):
	account_number, balance, __, __ = qdb.query_db(qdb.customer_info_query,username,password)[0]
	amount = int(input("Enter the amount you would like to withdraw: "))
	if amount <= int(balance):
		final_amount = int(balance) - amount
		qdb.query_db(qdb.transfer_from_query,amount,account_number)
		print('Withdrawal successful!, your current balance is {}'.format(final_amount))
		return True
	else:
		print('Insufficient Funds!')
	return False

def transfercash(username,password):
	receiver_name = input('Recipients full name: ')
	receiver_acc_num = int(input('Recipient\'s Account Number: '))
	amount_send = int(input('Amount you want to transfer: '))
	account_number = qdb.query_db(qdb.account_query)
	your_acc_num, balance, __, __ = qdb.query_db(qdb.customer_info_query,username,password)[0]
	if receiver_acc_num in account_number:
		print('This account belongs to {}'.format(receiver_name))
		print(account_number)
		if amount_send <= int(balance):
			final_amount = int(balance) - amount_send
			qdb.query_db(qdb.transfer_from_query,amount_send,your_acc_num)
			qdb.query_db(qdb.transfer_to_query,amount_send,receiver_acc_num)
			print('You have transferred {} to {}'.format(amount_send,receiver_name))
		else:
			print('There is no sufficient funds to complete this operation')
	else:
		print('Recipient does not exist')
	
	#Update the database with the value transferred to the beneficiary
	#Send a mail notifying the recipient of the successful transfer
