def caesar(s):
	res=''
	for i in range(len(s)):
		res+=chr(ord(s[i])+3) if ord(s[i])+3<=90 else chr(ord(s[i])-23)
	return res
print(caesar(input().upper()))