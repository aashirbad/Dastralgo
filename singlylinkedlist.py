
class Node(object):
	def __init__(self,key=None):
		self.key = key
		self.next = None


class LinkedList(object):
	def __init__(self,head=None):
		self.head = None

	def append(self,key):
		node = Node(key)
		current = self.head
		if self.head:
			while current.next:
				current = current.next
			current.next = node
			node.next = None
		else:
			self.head = node
			node.next = None


	def printData(self):
		current = self.head
		if self.head is None:
			print("list is empty")
			return
		else:
			while current:
				print(current.key)
				current = current.next

	def isempty(self):
		if not self.head:
			return True
		else:
			return False

	def pushfront(self,key):
		new_node = Node(key)
		current = self.head
		new_node.next = current
		self.head = new_node

	def topfront(self):
		if not self.head:
			print("list is empty")
		else:
			return self.head.key

	def popfront(self):
		if not self.head:
			print("empty list")
			return
		else:
			self.head = self.head.next

	def topback(self):
		current = self.head
		if not self.head:
			print("list is empty")
			return
		while current.next:
			current = current.next
		return current.key

	def popback(self):
		current = self.head
		if not self.head:
			print("list is empty")
			return
		else:
			while current.next.next:
				current = current.next
			current.next = None


	def addafter(self,node,key):
		new_node = Node(key)
		c = 0
		tmp = self.head
		while node != c:
			tmp = tmp.next
			c += 1
		new_node.next = tmp.next
		tmp.next = new_node

	def addbefore(self,node,key):
		new_node = Node(key)
		c = 0
		tmp = self.head
		while node-1 != c:
			tmp = tmp.next
			c += 1
		new_node.next = tmp.next
		tmp.next = new_node

	def find(self,key):
		tmp = self.head
		index = []
		c = 0
		while tmp:
			if tmp.key == key:
				index.append(c)
			tmp = tmp.next
			c += 1
		if not self.head:
			print("List is empty")
		elif not index:
			print("element not found")
		else:
			print("key found at indices")
			for item in index:
				print(item,end=" ")
		return tuple(index)

	def delete(self,key):
		current = self.head
		while current.next.key != key:
			current = current.next
		tmp = current.next
		if tmp.next is None:
			print("key not found")
		current.next = tmp.next














l = LinkedList()
l.append(4)
l.append(5)
l.append(7)


print("***")
l.printData()
l.addafter(1,44)
print()
l.printData()
print("*****")
l.addbefore(2,55)
l.append(5)
l.append(64)
l.append(5)

print("*****")
l.printData()
print("*****")
print(l.find(5))
l.delete(65)
print("*****")
l.printData()