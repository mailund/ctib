# Week 2:  Algorithm analysis

## Objects

* To learn how to *reason about computations* to construct *correct algorithms*.
* To learn how to *reason about complexity* so you can judge the efficiency of different solutions.

## Lectures notes

When we develop algorithms we naturally want them to be both correct and efficient. Constructing them such that they are, or convincing ourselves that a given algorithm is, requires some reasoning tricks.

### Pre- and post-conditions and invariants

If we think of the development of an algorithm as a sequence of refinements from a general goal we want solved until we have specified the steps to take in sufficient details that we can instruct a computer how to perform them, then we can use *predicates* to guide us. A predicate, here, means some logical property we want to be true at specific states in the algorithm. At the most abstract level, where we specify what an algorithm should do, we have a pre-condition that describes what we expect of the input to the algorithm, and a post-condition that describes what the algorithm has computed.

Consider the task of sorting a sequence of numbers. The pre-condition for a sort algorithm could be that the input is a sequence of numerical values, and the post-condition could be that the input numbers are now sorted.

```python
# lst is a list of numbers
<sort algorithm>
# lst is now sorted
```

At this level, of course, we are just describing what the algorithm should do, but once we start refining the steps of the algorithm, we specify what we want the various steps to guarantee. For example, one way to sort a list of numbers is to take one element at a time and put it into a list of already sorted elements. If we run through all the elements, we can specify the algorithm like this:

```python
# lst is a list of numbers
s = []
for x in lst:
	# s contains contains all the element we have
	# seen so far, in sorted order
	<update s with x>
lst = s
# lst is now sorted
```

Here, if `s` contains the elements we have seen so far, in sorted order, and if we iterate through all the elements in `lst`, then at the end of the loop, `s` will contain all the elements we need to sort and contain them in sorted order. The property we have inside the loop is a condition we want to be true whenever we start executing the body of the loop, and such properties we usually call *invariants* of the loop. For the invariant to be true, we need to guarantee that if it is true when we enter the body of the loop, then it is also true once we have executed the body o the loop. Plus, we typically want to specify the invariant in a way that, once the loop is completed, we have achieved a goal that matches pre- and post-conditions of the algorithm. In this example, if the invariant is true before and after each loop body execution, then we have sorted the elements in `lst` once we have finished the loop.

Once we specify an invariant of a loop, we must guarantee that it is always true, so at the very least we must make sure that it is true the first time we enter the loop. In this case, it trivially is, because `s` is empty and the invariant states that it should contain the elements we have seen so far---which are none when we first enter the loop. Next, we need to construct the loop body such that if the invariant is true before we execute it, it is also true once we are done with it.

```python
# lst is a list of numbers
s = []
for x in lst:
	# s contains contains all the element we have
	# seen so far, in sorted order
	smaller = [y for y in s if y <= x]
	larger = [y for y in s if y > x]
	s = smaller + [x] + larger
lst = s
# lst is now sorted
```

The body of this loop splits the `s` list into those that are smaller than the next element we must insert, and those that are larger. If `s` before we enter the loop body, then both `smaller` and `larger` will be sorted, so when we concatenate them with `x` between them, we end up with a sorted list.

As a side note, we wouldn't typically implement an algorithm at the outermost level of a Python program like this, so from here and onwards, we will implement algorithms as functions:

```python
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
```

When we implement algorithms as functions we can use the documentation string to specify the pre- and post-conditions of the function. This tells us what the function expects and what it guarantees, and we can use this when we construct other algorithms where we might use a function as a step along the way.

As another, sorting, example, we can consider so-called *merge sort* that works like this:

```python
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
```

This algorithm exploits that we can merge two sorted lists into one list that contains the element of the two lists in sorted order, so we can sort a list by splitting it into two, recursively sort these, and then merge them. We will get back to this idea shortly.

The merging function can look like this:

```python
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
```

Here as well we have some properties that guide us with implementing it. This function is also recursive. It has basis cases when one of the two lists are empty---in which case the merged list is just the other list---but otherwise the merged list must contain the smallest element, which must be at the front of one of the lists, and then the merging of the remaining  element. The latter, we can compute recursively.

Using recursion to design algorithms is a very powerful tool---one we will return to in later weeks---and the way we exploit it in these two functions is that we consider the pre- and post-conditions guaranteed by the function we are actively writing. If we assume that it is going to do what we promise it will do in the documentation string, then we can also use it to solve sub-problems. Which is exactly what we do here.

### Big-O notation and reasoning about complexity

When we develop algorithms, we want to be able to reason about their complexity at a relatively abstract level. The actual performance of any algorithm, once it is implemented and running on a computer, will depend on how it is implemented, what hardware it is executed on, and which input it works on, and a lot of details that would make it impossible to predict with accuracy how its performance will be. Thus, we abstract away most details of an algorithm and try to figure out a rough estimate of how it will perform, typically up to some unknown factor we can estimate later.

The first, and most important, abstraction we make is to consider all "primitive" operations as being equally expensive in performance. This is not true in any real execution of an algorithm---multiplying numbers takes longer than adding them, unless you multiply with factors of two, and moving values from RAM to the CPU takes longer than manipulating data in the cache, and so forth---but it is a convenient abstraction to get us started. Of course, what a "primitive" operation is, is another issue. Primitive operations would be doing arithmetic on numbers or moving single words of memory around, but usually also includes looking up indices in lists or dictionaries (in Python, these operations take constant time so we consider them primitive). Splitting a list in two, on the other hand, involves copying data from the list into two new lists and is not a primitive operation. In general, what we can consider primitive (constant time) operations and what are not will depend on the programming language you use, and there is not really any easy way to know which are which except from experience. As a rule of thumb, though, whenever an operation involves more than a single primitive data value---like a number or a character---then it is unlikely to be a primitive operation.

Anyway, we consider all primitive operations as equally expensive, and we consider the runtime complexity of an algorithm the number of operations that it will need to perform on a given input. Now, the performance some times depends on the actual input, and at other times just on the size of the input. Usually, we will abstract away the actual input and think only in terms of the size of the input. When we do this, we need to decide on whether we should consider the complexity for a given size the *worst-case performance* for that size---where we work out what the worst possible input could be and how many operations the algorithm needs to perform for that input---or the *average-case performance* where we figure out, from some assumptions about how input would be distributed, what the average number of operations the algorithm will need to perform.

Since there is some uncertainty in how expensive the primitive operations really are, we are not too careful about counting the *exact* correct number of operations an algorithm will perform. We usually just want to know the *order* of the performance, by which we mean some function of the input size that, up to a constant, will be an upper bound on the actual algorithmic performance.

If the (worst-case or average-case) time an algorithm uses on input of size *n* is *T(n)*, and we have some function *f(n)* and some constant *c* such that for all *n*---perhaps of some minimal size *n>N*---*T(n) < cf(n)*, then we say that the algorithm runs in *order* *f(n)* and we write this as *O(f(n))*.

Notice that this notation is only used to give an upper bound on the performance. The algorithm might actually be more efficient than the function *f(n)* indicates---although we usually want to find a function that gives a tight bound. The constant *c* could be considered part of the function *f(n)*, but we include it in the definition so we don't have to worry about the actual time any operation takes---by including the constant in the definition, the actual algorithm can run a hundred times faster or slower than the function indicates and still be in the same order complexity.

To get a feeling for how we use the O-notation, we can consider the two sorting algorithms from above.


 
## Exercises
* Functions (JVG 4)
* Basic data structures (JVG 5)
