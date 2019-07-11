from singlylinkedlist import *

class Stack:
	def __init__(self):
		self.LinkedList = LinkedList()


	def push(self,key):
		self.LinkedList.pushfront(key)

	def pop(self):
		self.LinkedList.popfront()

	def top(self):
		self.LinkedList.topback()

	def isempty(self):
		return self.LinkedList.isempty()

	def printData(self):
		self.LinkedList.printData()



s = Stack()
s.push(1)
s.push(2)
s.push(3)
print("*****")
s.printData()
print("******")
print(s.pop())
print("*******")
s.printData()
print("*********8")
print(s.top())
