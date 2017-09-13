# Week 2:  Algorithm analysis

## Objects

* To learn how to *reason about computations* to construct *correct algorithms*.
* To learn how to *reason about complexity* so you can judge the efficiency of different solutions.

## Reading material

Read JVG chapters 4 and 5 and sections 10-10.2.

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

To get a feeling for how we use the O-notation, we can consider the two sorting algorithms from above. We start with insertion sort:

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

This algorithm has one main loop that runs through `lst`. If the length of this list is *n*, then we can reason that the running time of the algorithm is *n* times the average time it takes to execute the body of the loop. Inside the loop, we split the list `s` into `smaller` and `larger` and then concatenate these with `[x]` in the middle. We construct the two lists using list comprehension, and while this doesn't look like a loop, it actually is---also hinted at by the keyword `for` used in the expressions---and constructing the `smaller` and `larger` lists take time proportional to the length of `s`. Concatenating the lists also take time proportional to the length of the lists, so that expression take time proportional to the length of `s` plus one. So the running time of insertion sort is *n* times the average length of `s` during the algorithm. In the first iteration, `s` is empty, so it has length 0. The second time we execute the loop-body it has length 1, and it grows by one for each iteration: 0, 1, 2, ..., *n*-1. The mean of this is *n/2*. Thus, the running time for the algorithm is *O(n \* n/2)=O(n^2)*.

Now for merge sort:

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

Here, the reasoning is slightly more complex because the solution is recursive. If we define *T(n)* to be the running time for sorting a list of length *n*, then we write a recursion for the time complexity as well. Inside the function, we split the initial list into two lists of half the length. This involves copying the values from the old list into the two new ones, and takes linear time: *O(n)*. Then the two smaller lists are sorted, which must take time 2 \* *T(n/2)*. Finally, the lists are merged. We will, for now, assume that this can be done in linear time---*O(n)*---since this is possible, although the solution we have right now doesn't do this. Anyway, the complexity for the algorithm is then *T(n) = O(n) + T(n/2)*. One can solve this recursion and the solution is *T(n) = O(n log n)*. So we see that merge sorting is more efficient than insertion sorting since eventually, for some *n*, any *n log n* function will be dominated by an *n^2* function.

If you measure the running time of the two algorithms, though, you will find that the merge sort we have implemented here is slower than insertion sort. This is because the merge function does not, in fact, run in linear time.

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

We can write a recursion for the running time for this function as well. What the function does is that it takes the smallest element from the two lists, make a list of a single element out of that, and then concatenate it with the result of a recursive call. This concatenation involves copying all the list elements, so the running time is *T(n) = O(n) + T(n-1)* which is *O(n^2)* and not *O(n)* as we want it to be. If we could modify the algorithm so the recursion would be *T(n) = O(1) + T(n-1)*, then we would have a linear time version---we can do that by not concatenating lists. Here is a way to do that that uses indices into the lists and constructs a new lists of the right length before the merging.

```python
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
```

As an exercise, try to annotate this function with pre- and post-conditions for the `helper` function that will help you prove that it works correctly.

It might be easier to implement `merge` using a loop instead of a recursive `helper` function. Try to rewrite the function to do this.
 
## Exercises

Clone the notebook library for [week 2](https://notebooks.azure.com/mailund/libraries/ctib-week02) into your library. Then do the exercises in the notebooks

1. Working with lists
2. Working with functions
3. Designing algorithms

