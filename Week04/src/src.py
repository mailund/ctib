
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
