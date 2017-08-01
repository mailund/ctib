
def smallest_and_largest(x):
  smallest_index, largest_index = 0, 0
  for i in range(len(x)):
  	# Inv: smallest_index points to a smallest element in x[:i] or is 0
  	# Inv: largest_index points to a largest element in x[:i] or is 0
    if x[i] < x[smallest_index]:
    	smallest_index = i
    if x[largest_index] < x[i]:
    	largest_index = i
  return smallest_index, largest_index

x = [1, 0, 5, 2, 5, 7, 2, 5, 8, 2, 9, 4]
print(smallest_and_largest(x))
print(x[:0])


def quick_sort(x):
	if len(x) < 2:
		return x

	pivot = x[1] # FIXME
	equal = [e for e in x if e == pivot]
	smaller = [e for e in x if e < pivot]
	larger = [e for e in x if e > pivot]
	return quick_sort(smaller) + equal + quick_sort(larger)


x = [1, 5, 2, 5, 7, 2, 5, 8, 2, 9, 4]
print(quick_sort(x))
