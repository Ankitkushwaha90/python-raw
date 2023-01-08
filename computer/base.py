n=50
i=0
s=0
w=0
while i<n:
	i+=s
	s+=w
	w+=s
	s+=10
print("s",s)
