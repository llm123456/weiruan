#双头栈
class TwoStack():
	def __init__(self,arr=None):
		if not arr:
			self.arr = []
		else:
			self.arr = arr

	def l_push(self,value):
		self.arr.insert(0,value)

	def l_pop(self):
		if len(self.arr) > 0:
			del self.arr[0]

	def r_push(self,value):
		self.arr.append(value)

	def r_pop(self):
		if len(self.arr) > 0:
			del self.arr[len(self.arr)-1]

	def __str__(self):
		return '['+','.join([str(x) for x in self.arr])+']'


if __name__ == '__main__':
	a = TwoStack()
	a.l_push(1)
	# a.l_pop()
	# a.l_push(2)
	# a.r_push(3)
	# a.r_pop()
	print(a)

