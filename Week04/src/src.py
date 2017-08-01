
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


from random import randint
def quick_sort(x):
	# base case
	if len(x) < 2:
		return x

	# recursive case
	pivot = x[randint(0, len(x)-1)]
	equal = [e for e in x if e == pivot]
	smaller = [e for e in x if e < pivot]
	larger = [e for e in x if e > pivot]
	return quick_sort(smaller) + equal + quick_sort(larger)


x = [1, 5, 2, 5, 7, 2, 5, 8, 2, 9, 4]
print(quick_sort(x))

def rec_factorial(n):
	if n <= 1:
		return 1
	else:
		return n * rec_factorial(n - 1)

def dynprog_factorial(n):
	table = [1] * n
	for i in range(1, n):
		table[i] = i * table[i-1]
	return n * table[n-1]

print(rec_factorial(5), dynprog_factorial(5))

def rec_fibonacci(n):
	if n <= 2:
		return 1
	else:
		return rec_fibonacci(n-1) + rec_fibonacci(n - 2)

def dynprog_fibonacci(n):
	table = [1] * n
	for i in range(3, n):
		table[i] = table[i-1] + table[i-2]
	return table[n-1] + table[n-2]


print(rec_fibonacci(5), dynprog_fibonacci(5))
