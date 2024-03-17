#!/usr/bin/python

class Node:
	def __init__(self, payload=None):
		self.payload = payload
		self.left = None
		self.right = None
		self.bf = None # Balance factor	
		self.height = None
