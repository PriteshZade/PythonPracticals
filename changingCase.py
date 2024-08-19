def capitalise(text):
	i=0
	ans=""
	while(i<len(text)):
		if(ord(text[i])>=97 and ord(text[i])<=122):
			ans=ans+chr(ord(text[i])-32)
		else:
			ans = ans+text[i]
		i=i+1
	return ans
def smaller(text):
	i = 0
	ans=""
	while(i<len(text)):
		if(ord(text[i])>=65 and ord(text[i])<=90):
			ans=ans+chr(ord(text[i])+32)
		else:
			ans = ans+text[i]
		i=i+1
	return ans
def reverse(text):
	i = 0
	ans=""
	while(i<len(text)):
		if(ord(text[i])>=65 and ord(text[i])<=90):
			ans=ans+chr(ord(text[i])+32)
		elif(ord(text[i])>=97 and ord(text[i])<=122):
			ans=ans+chr(ord(text[i])-32)
		else:
			ans = ans+text[i]
		i=i+1
	return ans
def zigZag(text):
	ans=""
	if(ord(text[0])>=65 and ord(text[0])<=90):
			i = 0
			while(i<len(text)):
				if(i%2==0):
					if(ord(text[i])>=97 and ord(text[i])<=122):
						ans=ans+chr(ord(text[i])-32)
					else:
						ans = ans+text[i]
				else:
					if(ord(text[i])>=65 and ord(text[i])<=90):
						ans=ans+chr(ord(text[i])+32)
					else:
						ans = ans+text[i]

				i=i+1
			return ans

	else:
			i = 0
			while(i<len(text)):
				if(i%2==0):
					if(ord(text[i])>=65 and ord(text[i])<=90):
						ans=ans+chr(ord(text[i])+32)
					else:
						ans = ans+text[i]

				else:
					if(ord(text[i])>=97 and ord(text[i])<=122):
						ans=ans+chr(ord(text[i])-32)
					else:
						ans = ans+text[i]
						
				i=i+1
			return ans
def change_case(text , style):
	
	if(style in ["c","C"]):
		return capitalise(text)
		
	if(style in ["s","S"]):
		return smaller(text)
	if(style in ["r","R"]):
		return reverse(text)
	if(style in ["z","Z"]):
		return zigZag(text)
	else:
		return text
print(change_case("Pri$esh","z"))

						

	
				
				