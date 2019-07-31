from singlylinkedlist import *

class Stack:
	def __init__(self):
		self.LinkedList = LinkedList()


	def push(self,key):
		self.LinkedList.pushfront(key)

	def pop(self):
		self.LinkedList.popback()

	def top(self):
		self.LinkedList.topback()

	def isempty(self):
		return self.LinkedList.isempty()

	def printData(self):
		self.LinkedList.printData()

