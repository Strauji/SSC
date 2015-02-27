from ucrypt import execute

try_again = 'y'

################################################################
print 'uCrypt 2.0'
print 'Please keep in mind that some keys may not work as well'
print 'So, we have a "debug" system.'
print '[-] = Encrypted string'
print '[+] = Output with same key'
print ''
################################################################
#############################################################################
while (try_again == 'y'):
	msg = raw_input('Enter what you want to be encrypted:')
	key = raw_input('Enter a key:')
	print 'It may take several seconds until get finished, please wait'

	
	a = execute(key,msg)
	
	print  "[-] => " + a

	print  ' ------------- '
	b = execute(key,a)
	
	print  "[+] => " + b
	try_again = raw_input('Want to try again?[y/n]:')
############################################################################
print 'Done'
