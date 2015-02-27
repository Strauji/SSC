#######################################################
def fibonacci(pos):
    if not type(pos) == int: 
        return 'Error - Key must be an integer'
    else:
        n = 1
        nn = 0
        nnn = 0
                
        for x in range(0,pos):
           
          nnn = nn

	  nn = n
	  n = nn+nnn
        return n
#######################################################  
#############################################################            
def execute(key, msg):
       return simple(key,msg) #While it can't parser "n:x:y"-like keys, it just jump to "simple"
       print 'Error - uCrypt cant parser string keys yet...'
#############################################################    
'''
####Disabled for a while
def complex(key,msg,plus):
    if not type(key) == str:
        return 'Error - complex key must be an string'
    else:
        args = key.split(':')
        
	f = msg
        for x in range(0,len(args)):
	  ke = int(args[x])
	 

          f = simple(ke,f,plus)
        return f
'''
###########################################################
def simple(key,msg):
    key = int(key)
    if not type(key) == int: 
	#yep, i know that it is redundant.
        return 'Error - simple key must be an integer'
    else:
	r = '' #initialize r	 
        for i in msg:
            rest = fibonacci(key)
            rest = rest % 256
	    ascii_char = ord(i)
            c =  ascii_char - rest
	    r = r + chr(abs(c))    
        return r
###########################################################
    
#Only God know why it works...
