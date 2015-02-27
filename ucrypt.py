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
                
def execute(key, msg,is_plus):
   
    if type(key) == int:
        return simple(key,msg,is_plus)
	
		
    elif type(key) == str:
       # return complex(key,msg,is_plus) - Disabled for a while
       print 'Error - uCrypt cant parser string keys yet...'
    
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
def simple(key,msg,plus):
    key = int(key)
    if not type(key) == int: 
	#just to avoid (IM)POSSIBLES errors
        return 'Error - simple key must be an integer'
    else:
	r = ''
	 
        for i in msg:
             


            rest = fibonacci(key)
            rest = rest % 256
	    ascii_char = ord(i)
            c =  ascii_char - rest
	  
	  
	   
	   
	    r = r + chr(abs(c))    
        return r

    

