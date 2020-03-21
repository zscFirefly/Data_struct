class Node():
	def __init__(self,item):
		self.elem = item
		self.left = None
		self.right = None


class Solution():
	def level_traversal(self,root):
		# 利用队列，每次遍历一层节点，将他们入队，计算队列剩余多少节点。
		if not root:
			return results
		results = []
		queue = [root]
		level = 0
		while queue:
			# 每一层遍历就是树的一层
			length = len(queue)
			results.append([])
			for i in range(length):
				node = queue.pop(0)
				results[level].append(node.elem)

				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)
			level += 1
		return results

if __name__ == '__main__':
	node = Node(1)
	node.left = Node(2)
	node.right = Node(3)
	node.left.left = Node(4)
	node.left.right = Node(5)
	results = Solution().level_traversal(node)
	print(results)

