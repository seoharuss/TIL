class Point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	
	def __str__(self):
		return f"({self.x}, {self.y})"
	
	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)
	
	def __sub__(self, other):
		return Point(self.x - other.x, self.y - other.y)
	
	def __mul__(self, other):
		return Point(self.x * other.x, self.y * other.y)
	
p = Point(1, 2)
q = Point(3, 4)
r = p - q
print(r)
r = q * p
print(r)
r = p * q		# 이 문장은 에러를 발생시킨다!
print(r)