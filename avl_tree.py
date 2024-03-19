#!/usr/bin/python
import node
import logging as log
import time
import curses

log.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',level=log.DEBUG, filename='bt.log', datefmt='%Y-%m-%dT%H:%M:%S%z')

log.info("<<<<<<<<<<< STARTING PROCESS >>>>>>>>>>")

stdscr = curses.initscr()
pad = curses.newpad(100,3000)

#TODO: Implement automatic balancing
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
		
		self.set_height(cn)
		
		return cn


	def set_height(self, cn=None):
		cn.height = max(self.get_height(cn.left), self.get_height(cn.right)) + 1

	def get_height(self, cn=None):
		if cn is None:
			return -1
		
		return cn.height
	

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
		res.append(' '*depth + "<({}):".format(cn.height) + str(cn.payload))
		res += self.tree_matrix_r(cn.left, depth+1)
		
		return res		

	def print_tree(self):
		matrix = self.tree_matrix()
		print "---------------"
		for line in matrix:
			print line
		print "---------------"
	
	def draw(self, matrix):
		for ri, r in enumerate(matrix):
			for ci, c in enumerate(r):
				pad.addch(ri, ci, matrix[ri][ci])	



if __name__ == "__main__":
	TIME, TIME_END = 0.3, 3
	LEVEL_SPACER = 2
	IN_LIST = [-1,0,-10,-5,234,2341234,12341234,242,234,222,1]	

	tree = AVLTree()

	def func(scr):
		for i, item in enumerate(IN_LIST):
			tree.insert(item)
			pad.erase()
			tree.draw(tree.tree_matrix())
			pad.refresh(0,0, 0,0, curses.LINES-1, curses.COLS-1)
			time.sleep(TIME)
		time.sleep(TIME_END)

	curses.wrapper(func)
	tree.print_tree()








		
