def isBalanced(expr):
	if len(expr)%2 != 0:
		return False

	opening=set('([{')
	match=set([('(', ')'), ('[', ']'), ('{','}')])
	stack=[]
	for char in expr:
		if char in opening:
			stack.append(char)
		else:
			if len(stack) == 0:
				return False
			lastOpen= stack.pop()
			if (lastOpen, char) not in match:
				return False

	return len(stack)==0


if __name__ == '__main__':
	expr = '({[({})]})'
	if isBalanced(expr):
		print('Balanced')
	else:
		print('Not Balanced')
