from datetime import date
import mysql.connector
from mysql.connector import errorcode
import logging

LOG_FORMAT = '%(asctime)-15s %(levelname)s %(message)s'
LOG_FILE = '/Users/tolu/Downloads/Tolu_Python/log1.txt' #Personalize

logger= logging.getLogger()
logger.setLevel(logging.DEBUG) 
handler = logging.FileHandler(LOG_FILE, 'a', 'utf-8')
handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(handler)

query_config = {
  'user': 'root', #Personalize
  'password': 'raincheck$25', #Personalize
  'host': '127.0.0.1',
  'database': 'atm',
  'raise_on_warnings': True
}

insert_account_data_query = ("INSERT INTO atm.account (customer_id, account_number, balance, account_type) VALUES (%s, %s, %s, %s)")
insert_cusomer_data_query = ("INSERT INTO atm.customer (fullname, username, password, gender, email, date_of_birth) VALUES (%s, %s, %s, %s, %s, %s)")

balance_query = ("SELECT balance FROM atm.account WHERE account_number = %s")
login_query = ("SELECT username FROM atm.customer WHERE username = %s and password = %s")

transfer_from_query = query_add = ("UPDATE atm.account SET balance = balance - %s WHERE account_number = %s")
transfer_to_query = query_add = ("UPDATE atm.account SET balance = balance + %s WHERE account_number = %s")

customer_info_query = ("SELECT account_number, balance, fullname, email FROM atm.account join atm.customer on (atm.account.customer_id = atm.customer.id) where username = %s and password = %s")
account_info_query = ("SELECT account_number, balance, fullname, email FROM atm.account join atm.customer on (atm.account.customer_id = atm.customer.id) where account_number = %s")

def query_db(query, *args):
	cnx = mysql.connector.connect(**query_config)
	cursor = cnx.cursor()
	logger.debug('Database auth successful for USER: {}'.format(query_config.get('user')))
	val = []
	for arg in args:
		val.append(arg)
	val = tuple(val)
	cursor.execute(query, val) # Must be a tuple
	logger.debug('Database Query successful for USER: {}'.format(query_config.get('user')))
	result =  []
	for r in cursor:
		result.append(r)
	if not result:
		cnx.commit()
	cursor.close()
	cnx.close()
	return result

#print(query_db(insert_account_data_query,'7', '1989', '6000000', 'Current'))
#print(query_db(insert_cusomer_data_query,'Kemi Awojana', 'yutbabie', 'yyuyu97', 'F', 'kemiawojana@gmail.com', date(1992, 9, 2)))
