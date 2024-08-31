Alphabets=["a","b"]
def dfa_ends_with_b(text):
	final=["q1"]
	final_state=q0(text)
	if final_state in final:
		return "Accepted"
	else:
		return "Rejected"
def q0(text):
	if(len(text)>0):
		if text[0] in Alphabets :
			if(text[0]=="a"):
				return q0(text[1:])
			else:
				return q1(text[1:])
		else:
			return "rejected"
	else:
		return "q0"
def q1(text):
	if(len(text)>0):
		if text[0] in Alphabets :
			if(text[0]=="a"):
				return q0(text[1:])
			else:
				return q1(text[1:])
		else:
			return "rejected"
	else:
		return "q1"
print(dfa_ends_with_b("abba"))
		
		
	
