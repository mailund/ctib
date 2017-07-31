
def linear_search(x, lst):
	for y in lst:
		if x == y:
			return True
	return False


def binary_search(x, lst):
	def recurse(start, end):
		# Inv: start <= end and x might be in lst[start:end].
		if start == end:
			return False
		i = start + (end - start) // 2
		if lst[i] == x:
			return True
		# Inv: start < end	
		elif lst[i] < x:
			return recurse(i, end)
		else:
			return recurse(start, i)
	return recurse(0, len(lst))


lst = [1, 4, 6, 9, 12, 15]
for i in range(20):
	print(i, binary_search(i, lst))
