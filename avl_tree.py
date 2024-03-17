#!/usr/bin/python
import node
import logging as log

log.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',level=log.DEBUG, filename='bt.log', datefmt='%Y-%m-%dT%H:%M:%S%z')

log.info("<<<<<<<<<<< STARTING PROCESS >>>>>>>>>>")

class AVLTree:
	def __init__(self):
		self.root = None

	def get_root(self):
		log.debug("Getting root")
		return self.root


	def insert(self, payload):
		if payload is None:
			log.error("Payload is empty!")
			return

		log.debug("(++) PL:%r Calling recursive insert method", payload)
		self.root = self.insert_r(payload, self.root)

	def insert_r(self, payload, cn):
		if cn is None:
			log.debug("(--) PL:%r Empty node found: inserting", payload)
			cn = node.Node(payload)

		if payload < cn.payload:
			log.debug("(<-) PL:%r < CN:%r", payload, cn.payload)
			cn.left = self.insert_r(payload, cn.left)
		if payload > cn.payload:
			log.debug("(->) PL:%r > CN:%r", payload, cn.payload)
			cn.right = self.insert_r(payload, cn.right)
		
		return cn

	
	def in_order(self):
		cn = self.get_root()
		if cn is None:
			log.error("Tree is empty!")
			return []
			
		return self.in_order_r(cn)

	def in_order_r(self, cn):
		if cn is None:
			return []

		res = []
		res += self.in_order_r(cn.left)
		res.append(cn.payload)
		res += self.in_order_r(cn.right)
		
		return res

	
	def tree_matrix(self):
		cn = self.get_root()
		if cn is None:
			log.error("Tree is empty!")
			return []

		return self.tree_matrix_r(cn)

	def tree_matrix_r(self, cn=None, depth=0):
		if cn is None:
			return []

		res = []
		res += self.tree_matrix_r(cn.right, depth+1)
		res.append(' '*depth + "<():" + str(cn.payload))
		res += self.tree_matrix_r(cn.left, depth+1)
		
		return res		

	def print_tree(self):
		matrix = self.tree_matrix()
		print "---------------"
		for line in matrix:
			print line
		print "---------------"




if __name__ == "__main__":
	tree = AVLTree()

	l = [2, 1, 3, 3, 4, 5, -1, -2, -5, -6, 100, 34, -101, -99]

	for item in l:
		tree.insert(item)

	print "In order:", tree.in_order(), "\n"
	tree.print_tree()
