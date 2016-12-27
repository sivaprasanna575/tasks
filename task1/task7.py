
def password(input):
	a=pswd.split()
	b=input.split()
	if(a==b):
		print "password is correct"
		
	
	else:
		print "wrong password please enter correct password"
		

input=raw_input("enter password")
pswd="git123"
password(input)


