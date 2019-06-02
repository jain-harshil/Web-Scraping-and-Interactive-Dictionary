interactive_dictionary = open("data.json","r")
import json
from difflib import get_close_matches
a = interactive_dictionary.read() 
n = ["abandoned industrial site"] 
m = []
for i in range (len(a)-3):
	if a[i:i+4] == '], "':
			j = i+4
			b = ""
			while a[j]!='"':
			  	b = b+a[j]
			  	j = j+1
			n.append(b)
	elif a[i:i+4] ==': ["':
			j = i+4
			q = ""
			while a[j]!='"':
			  	q = q+a[j]
			  	j = j+1
			m.append(q)
d = {}
for i in range (len(n)):
	if n[i] not in d:
		d[n[i]] = m[i]
def translate(k):
	if k in d:
		return(d[k])
	else:
		a = get_close_matches(k,n)
		if a!=[]:
		  	print("Did you mean?")
		  	for i in range (len(a)):
		  		print(i+1,a[i])
		  	print("Do you want to find the meaning of any of the above words? Yes/No")
		  	x = str(input())
		  	if(x == "Yes"):
		  		print("Enter the number of the word which you want")
		  		y = int(input())
		  		return(d[a[y-1]])
		  	elif(x == "No"):
		  		return("Ok as you want")
		else:
		  	print("No such word found in dictionary")
l = str(input("Enter the word"+"\n"))
l = l.lower()
output = translate(l)
print(output)
interactive_dictionary.close()