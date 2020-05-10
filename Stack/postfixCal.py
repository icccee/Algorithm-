import stack
# Translate infix calculation into postfix cal
# idea :
# 1, scan the string from left to right
# 2, if it is an number, put into the a empty list
# 3, if it is an oprator, 
# 	3.1 check stack
#	3.2 if the stack is empty, push the operator into the stack
#	3.3 if the stack is not empty, compare the priority of oprators
#		3.3.1 pop the one in the stack if it is higher than the one outside	
#				and put the poped one in the list
#		3.3.2 push the new operator into the stack
#		3.3.3 push the new operator into the stack if the priority is higher than the one in stack
# 4,once all items scaned, pop the rest of stack in the list


class postfix:

	def __init__(self):
		self.infix = []
		self.postfix=[]
		self.stack = stack.Stack()
	
	def scan(self,infix):
		if infix:
			self.infix = list(infix)
		else:
			print("empty")

	def toPostfixcal(self):
		operator ="*/+-"
		for item in self.infix:
			if item not in operator:
				self.postfix.append(item)
			elif item in operator:
				if self.stack.isEmpty():
					self.stack.push(item)
				else:
					stackOperator = self.stack.peek()
					if operator.index(item) < operator.index(stackOperator):
						self.stack.push(item)
					else:
						self.postfix.append(stackOperator)
						self.stack.pop()
						self.stack.push(item)
	
		while not self.stack.isEmpty():
			stackOperator = self.stack.peek()
			self.postfix.append(stackOperator)
			self.stack.pop()

	def result(self):
		#print(self.postfix)
		result = ' '
		for i in self.postfix:
			result+=i
		print(result)




			


a = "1*2+3*4"
b = postfix()
b.scan(a)
b.toPostfixcal()
b.result()
