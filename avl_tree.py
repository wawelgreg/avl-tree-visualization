#!/usr/bin/python
import node
import logging as log

log.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',level=log.DEBUG, filename='bt.log', datefmt='%Y-%m-%dT%H:%M:%S%z')


class AVLTree:
	def __init__(self):
		self.root = None

	
		
if __name__ == "__main__":
	log.debug("Test log 1")
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
	log.debug("Test log 2")
