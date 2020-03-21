class Solution():
	def sulo(self,num,value):
		res_length = 0
		for i in range(len(num)):
			if num[i] != value:
				num[res_length] = num[i]
				res_length +=1
		return res_length

if __name__ == '__main__':
	lis = [3,2,2,9,3,2,3]
	value = 2
	res = Solution().sulo(lis,value)
	print(res)