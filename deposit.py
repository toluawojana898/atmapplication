import query_db as qdb
import login
import getpass as pas 
from datetime import date
import logging
import mysql.connector
from mysql.connector import errorcode
import re
import smtplib
from email.mime.text import MIMEText
import os

def cashAdd(username,password):
	account_number, balance, ___ = qdb.query_db(qdb.display_customer_data_query,username,password)[0]
	amount = int(input("Enter the amount you want to deposit: "))
	final_amount = int(balance) + amount
	qdb.query_db(qdb.transfer_to_query,amount,account_number)
	print('The deposit of {} was successful for account number {} you now have a balance of {}'.format(amount,account_number,final_amount))
	qdb.logger.debug('Deposit of {} successful for {}'.format(amount,account_number))

def cashRemove(username,password):
	account_number, balance, ___ = qdb.query_db(qdb.display_customer_data_query,username,password)[0]
	amount = int(input("Enter the amount you would like to withdraw: "))
	if amount <= int(balance):
		final_amount = int(balance) - amount
		qdb.query_db(qdb.transfer_from_query,amount,account_number)
		print('Withdrawal successful please take your cash!, your current balance is {}'.format(final_amount))
		qdb.logger.debug('Withdrawal of {} successful for {}'.format(amount,account_number))
		return True
	else:
		print('Insufficient Funds!')
		qdb.logger.debug('Insufficient funds for Account number: {}'.format(account_number))
		return False

def transfercash(account_number):
	try:
		receiver_name = input('Recipients full name: ')
		receiver_acc_num = int(input('Recipient\'s Account Number: '))
		amount_send = int(input('Amount you want to transfer: '))
		rcv_acc_num = qdb.query_db(qdb.check_account_query,receiver_acc_num)[0]
		if receiver_acc_num not in rcv_acc_num:
			print('Recipient does not exist')
	except:
		print('Something went wrong :)')
		return False	

	try:
		account_number, balance = qdb.query_db(qdb.customer_transfer_query,account_number, amount_send)[0]
		print('You have transferred {} to {}'.format(amount_send,receiver_name))
		qdb.logger.debug('Successfully debited account number {} with {}'.format(account_number,amount_send))
		qdb.logger.debug('Successfully credited account number {} with {}'.format(receiver_acc_num,amount_send))
	except:
		print('Insufficient Funds to complete this operation')
		qdb.logger.debug('Insufficient funds for Account Number {}'.format(account_number))
		#print('This account belongs to {}'.format(receiver_name))
		#print(account_number)
	qdb.query_db(qdb.transfer_from_query,amount_send,account_number)
	qdb.query_db(qdb.transfer_to_query,amount_send,receiver_acc_num)

def createNewAccount():
	fullname, newuser, email = getUserInfo()
	account_number = getAndCreateUserAccountInfo()
	sendEmail()

def getUserInfo():
	fullname = input('Enter your fullname: ').lower()
	newuser = input('Enter a unique login username: ')
	isUserNameExist(newuser)
	#newuser = input('Enter a unique login username: ')
	'''
	if not isUserNameExist():
		print('Hello {}, please start all over')
		os.exit(1)
	'''
	pd = pas.getpass(prompt='Enter a login password:')
	gender = input('Gender! Enter either "M" or "F" only: ').upper()
	email = input('Enter a valid email address: ')
	isEmailValid(email)
	dob = input('Enter date of birth in this format YYYY MM DD: ')
	dob = dob.split(' ')
	dob[0] = int(dob[0])
	dob[1] = int(dob[1])
	dob[2] = int(dob[2])
	qdb.query_db(qdb.insert_cusomer_data_query,fullname, newuser, pd, gender, email, date(dob[0],dob[1],dob[2]))
	return(fullname,newuser,email)

def isUserNameExist(newuser):
	attempt = 5
	#newuser = input('Enter a unique login username: ')
	userNameExist = qdb.query_db(qdb.check_customer_username)[0]
	while newuser in userNameExist:
		attempt -= 1
		print('Not available! use another name')
		qdb.logger.debug('Username: {} already exists'.format(newuser))
		newuser = input('Enter a unique login username again: ')
		if attempt <= 1:
 			break
	return True

def getAndCreateUserAccountInfo():
	balance = int(input('Enter your opening balance: '))
	account_type = input('Enter account type,"Savings" or "Current": ').title()
	account_number = qdb.query_db(qdb.get_account_query,newuser, pd)[0][0]
	qdb.query_db(qdb.insert_account_data_query, account_number, balance, account_type)
	return (account_number)
 

def isEmailValid(email):
	#email = input('Enter a valid email address: ')
	while not re.search(r'^(\w.+)@(\w+)\.(\w+)$', email):
		email = input('Re-enter a valid email address: ')
	return True

def sendEmail():
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.ehlo()
	server.login('bankerspython@gmail.com', 'atmapplication2020')
	msg = MIMEText('Hello {}, Welcome to Teejay\'s Bank! Your new account number is {}'.format(fullname, account_number))
    #print('Hello {}, Your new account number is {}'.format(fname, acc))
	fromx = 'bankerspython@gmail.com'
	msg['Subject'] = 'Welcome to Teejay\'s Bank'
	msg['From'] = fromx
	server.sendmail(fromx, email, msg.as_string()) 
	server.quit()
