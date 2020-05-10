# basic stack 


class Stack:
	
	def __init__(self):
		self.stack = []

	def push(self,item):
		self.stack.insert(0,item)
	
	def pop(self):
		if not self.isEmpty():
			self.stack.pop(0)
		else:
			print("Empty stack")

	def peek(self):
		if not self.isEmpty():
			return self.stack[0]
		else:
			print("Empty stack")

	def size(self):
		return len(self.stack)

	def isEmpty(self):
		if self.size() == 0:
			return True
		else:
			return False

	def printStack(self):
		if not self.isEmpty():
			for i in self.stack:
				print(i)
		else:
			print("Empty Stack")



"""
aStack = Stack()

aStack.printStack()
aStack.push(3)
aStack.push(5)
aStack.push(0)
aStack.push(7)
#aStack.printStack()
aStack.pop()
aStack.push(21)
print("{} {} {}".format("There r",aStack.size(),"items in the stack"))
#aStack.printStack()
while aStack.size() > 0:
	print(aStack.peek())
	aStack.pop()

aStack.printStack()
"""