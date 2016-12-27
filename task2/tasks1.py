b=[];c=[];d=[]
a=['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
for i in a:
	if(i.startswith('x')):
				
		b.append(i)
	else:
		c.append(i)
b.sort()
c.sort()
d=b+c
print d

	
		
		
