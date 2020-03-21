class Node():
	def __init__(self,item):
		self.elem = item
		self.left = None
		self.right = None

class Solution():
	def LDR(self,root):
		stacks = []
		results = []
		while stacks or root:
			if root:
				stacks.append(root)
				root = root.left
			else:
				tmp = stacks.pop()
				results.append(tmp.elem)
				root = tmp.right
		return results


if __name__ == '__main__':
	node = Node(1)
	node.left = Node(2)
	node.right = Node(3)
	node.left.left = Node(4)
	node.right.left = Node(5)
	results = Solution().LDR(node)
	print(results)
