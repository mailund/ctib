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

### Big-O notation and reasoning about complexity

 
## Exercises
* Functions (JVG 4)
* Basic data structures (JVG 5)
