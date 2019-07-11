
class Node(object):
	def __init__(self,key=None):
		self.key = key
		self.next = None
		self.prev = None


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
			node.prev = current
		else:
			self.head = node
			node.prev = self.head
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
		current.prev = new_node
		self.head = new_node
		new_node.prev = self.head

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
			current = self.head.next
			self.head = current
			current.prev = self.head


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
			while current.next:
				current = current.next
			node = current.prev
			key = current.key
			node.next = None
			current.prev = None
			return key


	def addafter(self,node,key):
		new_node = Node(key)
		c = 0
		tmp = self.head
		while node != c:
			tmp = tmp.next
			c += 1
		tmp.next.prev = new_node
		new_node.prev = tmp
		new_node.next = tmp.next
		tmp.next = new_node

	def addbefore(self,node,key):
		new_node = Node(key)
		c = 0
		tmp = self.head
		while node != c:
			tmp = tmp.next
			c += 1
		new_node.prev = tmp.prev
		new_node.next = tmp
		tmp.prev.next = new_node
		tmp.prev = new_node
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
		while current.key != key:
			current = current.next
		if current is None:
			print("Key not found")
		elif current.next is None:
			current.prev.next = None
			current.prev = None
		else:
			current.prev.next = current.next
			current.next.prev = current.prev
			current.next = None
			current.prev = None













l = LinkedList()
l.append(5)
l.append(6)
l.append(7)
l.pushfront(1)
l.pushfront(2)
l.pushfront(3)
print(l.popback())
l.printData()