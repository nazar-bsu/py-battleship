class Point:
	'''
	Point with coordinates in {i,j} notation
	'''

	def __init__(self, i:int, j:int):
		self.i = i
		self.j = j

	def __str__(self):
		orderA = ord('А')
		return f'({self.i};{chr(orderA + self.j)})'
	
	def isHere(self, i:int, j:int) -> bool:
		return i == self.i and j == self.j
