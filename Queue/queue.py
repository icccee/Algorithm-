# basic queue

class Queue:

	def __init__(self):
		self.queue = []

	def push(self,item):
		self.queue.append(item)

	def pop(self):
		if not self.isEmpty():
			self.queue.pop(0)
		else:
			print("Empty queue")	
	
	def size(self):
		return len(self.queue)
	
	def isEmpty(self):
		if self.size() == 0:
			return True
		else:
			return False
	
	def peek(self):
		if not self.isEmpty():
			return self.queue[0]
		else:
			print("Empty queue")

	def printQueue(self):
		for i in self.queue:
			print(i,end='')
		print('')	

queue = Queue()
for i in range(10):
	queue.push(i)
queue.printQueue()
