def reverseWords1(text):
	print(" ".join(reversed(text.split())))

def reverseWords2(text):
	print(" ".join(text.split()[::-1]))

import string
def reverseWords3(text):
	words=[]
	length=len(text)
	space=set(string.whitespace)
	#breakpoint()
	index=0
	while index < length:
		if text[index] not in space:
			wordStart=index
			while index<length and text[index] not in space:
				index+=1
			words.append(text[wordStart:index])
		index+=1
	print(" ".join(reversed(words)))


#Like in place modification, But since python strings are immutable we can’t modify them in-place. 
def reverseWords4(text):
	words =  text[::-1].split()
	print(" ".join(word[::-1] for word in words))

if __name__ == '__main__':
	text="This is reversed"
	reverseWords2(text)