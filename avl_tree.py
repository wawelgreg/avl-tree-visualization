#!/usr/bin/python

import node

class AVLTree:
	def __init__(self):
		self.root = None
	
		
if __name__ == "__main__":
	tree = AVLTree()

	na = node.Node(2)
	nb = node.Node(1)
	nc = node.Node(3)

	tree.root = na
	tree.root.left = nb
	tree.root.right = nc

	print "Tree root", tree.root.payload
	print "Root left child", tree.root.left.payload		
	print "Root right child", tree.root.right.payload		
