def modulo(n,d):
	x = n//d
	y = n-(d*x)
	return y

def count(s1 , s2 , b):
	if(len(s2)==0):
		return len(s1)+1
	if(len(s1)==0):
		return -1
	if(b==True):
		i = 0
		c=0
		x = s1.find(s2,i)
		if(x<0):
			return 0
		else:
			c = c+1
			i=x+1
		#j=4
		while(x>0):
			x = s1.find(s2,i)
			if(x>0):
				c = c+1
				i=1+x
		return c
	if(b==False):
		i = 0
		c=0
		x = s1.find(s2,i)
		if(x<0):
			return -1
		else:
			c = c+1
			i=x+len(s2)
		j=4
		while(x>0):
			x = s1.find(s2,i)
			if(x>0):
				c = c+1
				i=x+len(s2)
		return c
			
	
print(modulo(5,-3))
#print(count("","njnj",False))
