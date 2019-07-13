class Node(object):
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None


class BinaryTree(object):
	def __init__(self,root=None):
		self.root = Node(root)

	def preorder_traverse(self,start):
		if self.root is None:
			print("tree is empty")
			return
		else:
			print(start.value)
			self.preorder_traverse(start.left)
			self.preorder_traverse(start.right)

	def inorder_traverse(self,start):
		if self.root is None:
			print("tree is empty")
			return
		else:
			self.inorder_traverse(start.left)
			print(start.value)
			self.inorder_traverse(start.right)

	def postorder_traverse(self,start):
		if self.root is None:
			print("tree is empty")
			return
		else:
			self.postorder_traverse(start.left)
			self.postorder_traverse(start.right)
			print(start.value)


	def insert(self,value):
		if self.root is None:
			self.root = Node(value)
		else:
			self._insert(value,self.root)

	def _insert(self,value,curr_node):
		if 