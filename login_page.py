import getpass as pas
import query_db as qdb

def enter_pass(username,password):
  attempts = 3
  name = 'TeeJay'
  user_name, passwd = qdb.query_db(qdb.login_query,username,password)[0]
  #print(usernpasswd)
  #print(type(usernpasswd))
  while True:
    if username.lower() == user_name and password == passwd:
      print('You are welcome to {}\'s Bank!!!'.format(name))
      qdb.logger.debug('Successfully logged in for username: {}'.format(user_name))
      return True
    else:
      attempts -= 1
      print('Login is wrong, You have {} attempts left'.format(attempts))
      qdb.logger.error('Failed login attempts for username: {}'.format(username))
      userinput = input('Enter username again: ')
      pidkeys = pas.getpass(prompt='password again: ')
      if attempts <= 1:
        print('This account is locked, try again in 24 hours sorry!')
        return False
