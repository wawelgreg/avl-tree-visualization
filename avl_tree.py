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
		
		return self.rotate(cn)
	
	def rotate(self, cn):
		lh = self.get_height(cn.left)
		rh = self.get_height(cn.right)

		if rh - lh < -1: # Left heavy
			llh = self.get_height(cn.left.left)
			lrh = self.get_height(cn.left.right)
			
			if lrh - llh < -1: # Left left case
				return self.right_rotate(cn)

			if lrh - llh > 1: # Left right case
				cn.left = self.left_rotate(cn.left)
				return self.right_rotate(cn)
			
		if rh - lh > 1: # Right heavy
			rrh = self.get_height(cn.right.right)
			rlh = self.get_height(cn.right.left)

			if rrh - rlh > 1: # Right right case
				return self.left_rotate(cn)
			
			if rrh - rlh < -1: # Right left case
				cn.right = self.right_rotate(cn.right)
				return self.left_rotate(cn)

		return cn
	
	def right_rotate(self, p):
		c = p.left
		t = c.right
		
		c.right = p
		p.left = t

		self.set_height(p)
		self.set_height(c)

		return c

	def left_rotate(self, p):
		c = p.right
		t = c.left

		c.left = p
		p.right = t
	
		self.set_height(p)
		self.set_height(c)

		return c


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
	TIME, TIME_END = 1, 3
	LEVEL_SPACER = 2
	IN_LIST = [-1,0,-10,-5,234,2341234,12341234,242,234,222,12342,2342,2424,23434,22342,111]	

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








		
