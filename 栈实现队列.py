class MyQueue():
	def __init__(self):
		self.s1=[]
		self.s2=[]

	def push(self,x:int) -> None:
		self.s1.append(x)

	def pop(self) -> int:
		if not self.s2:
			while self.s1:
				a = self.s1.pop()
				self.s2.append(a)
		return self.s2.pop()

	def peek(self) -> int:
		if not self.s2:
			while self.s1:
				a = self.s1.pop()
				self.s2.append()
		return self.s2[-1]

	def empty(self) -> bool:
		if not self.s1 and not self.s2:
			return True
		else:
			return False

if __name__ == '__main__':
	so = MyQueue()
	so.push(1)
	so.push(2)
	print(so.peek())
	print(so.peek())
	print(so.peek())

