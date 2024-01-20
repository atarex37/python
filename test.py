class Vector:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)

	def __repr__(self):
		return f"X is {self.x} and Y is {self.y}"

	def __str__(self):
		return f"X: {self.x}, Y: {self.y}"

	def __len__(self):
		return 11

	def __call__(self):
		return ("hep !")


v1 = Vector(2,3)
v2 = Vector(4,5)
v3 = v1 + v2
print(v3)
print(len(v3))
print(v3.__repr__())
print("dict: ", v1.__dict__)
print("dict: ", Vector.__dict__)
print(v3.__call__())
for key in v3.__dict__:
	print(key, v3.__dict__[key])