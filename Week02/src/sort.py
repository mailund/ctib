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
	if len(x) == 0:
		return y
	if len(y) == 0:
		return x
	# the merge must be the smallest element followed by the merging of the remaining
	if x[0] < y[0]:
		return [x[0]] + merge(x[1:], y)
	else:
		return [y[0]] + merge(x, y[1:])


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
