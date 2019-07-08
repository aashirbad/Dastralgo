class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

	
class LinkedList:
	def __init__(self):
		self.head = None

	def append(self,data):
		new_node = Node(data)
		current = self.head
		if current:
			while current.next:
				current = current.next
			current.next = new_node
			new_node.next = None
		else:
			self.head = new_node

	def printData(self):
		current = self.head
		if not current:
			print("Linked list is empty")
			return
		while current:
			print(current.data)
			current = current.next

	



l = LinkedList()
l.append(4)
l.append(5)
l.append(7)
l.printData()
