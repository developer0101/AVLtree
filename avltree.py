'''
Reza Fathi
AVL Tree in python3
'''
class Node:
	def __init__(self, val):
		self.val = val
		self.left = self.right = None
		self.height = 0

	def updateHeight(self):
		lh = self.left.height if self.left else 0
		rh = self.right.height if self.right else 0
		self.height = 1 + max(lh, rh)

	def balance(self):
		lh = self.left.height if self.left else 0
		rh = self.right.height if self.right else 0
		return lh-rh

	def leftRotate(self):
		root = self.right
		self.right = root.left
		root.left = self
		self.updateHeight()
		root.updateHeight()
		return root

	def rightRotate(self):
		root = self.left
		self.left = root.right
		root.right = self
		self.updateHeight()
		root.updateHeight()
		return root

	def rebalance(self):
		balance = self.balance()
		if balance>1:
			if self.left.balance()<0:
				self.left = self.left.leftRotate()
			return self.rightRotate()
		elif balance<-1:
			if self.right.balance()>0:
				self.right = self.right.rightRotate()
			return self.leftRotate()
		return self

	def insert(self, val):
		# print(val, flush=True)
		if val<self.val:
			self.left = self.left.insert(val) if self.left else Node(val)
		else:
			self.right = self.right.insert(val) if self.right else Node(val)
		self.updateHeight()
		return self.rebalance()

	def getMinValueNode(self):
		return self.left.getMinValueNode() if self.left else self

	def delete(self, val):
		if val<self.val:
			self.left = self.left.delete(val) if self.left else self.left
		elif val>self.val:
			self.right = self.right.delete(val) if self.right else self.right
		else:
			if self.left is None:
				return self.right
			elif self.right is None:
				return self.left
			temp  = self.right.getMinValueNode()
			self.val = temp.val
			self.right = self.right.delete(temp.val)
		self.updateHeight()
		return self.rebalance()

	def search(self, val):
		if val==self.val:
			return val
		if val<self.val:
			return self.left.search(val) if self.left else self.left
		else:
			return self.right.search(val) if self.right else self.right

	def isValid(self, minval, maxval):
		if self.val<minval or self.val>maxval:
			return False
		elif abs(self.balance())>1:
			return False
		res = self.left.isValid(minval, self.val) if self.left else True
		if res:
			res = self.right.isValid(self.val, maxval) if self.right else True
		return res

class AVLTree:
	def __init__(self):
		self.root = None

	def insert(self, val):
		self.root = self.root.insert(val) if self.root else Node(val)

	def delete(self, val):
		self.root = self.root.delete(val) if self.root else self.root

	def search(self, val):
		return self.root.search(val) if self.root else self.root

	def test(self):
		import random
		d = 100
		n = 2014+d
		nums = []
		for i in range(n):
			nums.append(random.randint(0, n**2))
			self.insert(nums[-1])
		numsdel = random.sample(nums, d)
		for num in numsdel:
			self.delete(num)

		import sys
		import numpy as np
		print("Simulation test inserted {0} random numbers and deleted {1} numbers".format(n,d))
		if self.root:
			print ("log(n)={0:0.2f}, avltree height={1}".format(np.log2(n-d),self.root.height))
		if self.root is None or self.root.isValid(-sys.maxsize, sys.maxsize):
			print("Valid avl tree!")
		else:
			print("Opps, Invalid avl tree")

def test():
	avltree = AVLTree()
	avltree.test()

if __name__=="__main__":
	test()
