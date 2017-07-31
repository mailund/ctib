def insertion_sort(lst):
	"""Sort a list of numbers.
	Input: lst -- a list of numbers
	Output: a list of the elements from lst in sorted order.
	"""
	s = []
	for x in lst:
		# s contains contains all the element we have
		# seen so far, in sorted order
		smaller = [y for y in s if y <= x]
		larger = [y for y in s if y > x]
		s = smaller + [x] + larger
	return s

def merge(x, y):
	"""Merge two lists, x and y.
	Input: sorted lists x and y
	Output: the merging of x and y -- a list with the elements of x and y in sorted order.
	"""
	n = len(x)
	m = len(y)
	z = [None] * (n + m)

	def helper(i, j, k):
		if i == n:
			z[k:] = y[j:]
		elif j == m:
			z[k:] = x[i:]
		elif x[i] < y[j]:
			z[k] = x[i]
			helper(i+1, j, k+1)
		else:
			z[k] = y[j]
			helper(i, j+1, k+1)

	helper(0, 0, 0)
	return z

def merge_sort(lst):
	"""Sort a list of numbers.
	Input: lst -- a list of numbers
	Output: a list of the elements from lst in sorted order.
	"""
	if len(lst) <= 1:
		return lst
	n = len(lst)
	first = merge_sort(lst[:n//2])
	second = merge_sort(lst[n//2:])
	# first is the sorted first half of the elements
	# second is the sorted second half of the elements
	return merge(first, second)


lst = [3, 2, 4, 6, 5, 8, 2, 5]
print(insertion_sort(lst))
print(merge_sort(lst))
