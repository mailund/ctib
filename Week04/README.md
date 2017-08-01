# Week 4: Algorithmic design

## Objectives

* **To learn some tricks for developing your own algorithms.**

## Lectures notes

Many algorithms you see in the literature have been refined over several years, and it seems almost magical that someone could come up with them. Now, while some do require a spark of genius insight, mostly it is just a case of refinement of a few simple ideas over time. Most algorithms didn't start out as simple and elegant as they are not presented; they were improved upon over the years and started out from a few simpler tricks.

When you have a problem that you need to solve, you will need to devise an algorithm for it. Algorithm, here, just mean a recipe for solving your problem, so even the simplest programs are really implementations of algorithms. So you need to have some tricks up your sleeve to approach algorithms. Luckily, you can get very far using just a few standard approaches.

### Pre- and post-conditions and invariants revisited

The first "trick" isn't really a trick as such, but a general approach to developing and implementing algorithms in general. The use of conditions and invariants. We have used predicates as pre- and post-conditions and as loop or recursion invariants in the previous weeks, but I cannot stress enough how useful a tool these predicates are. Invariants are particularly useful. Whenever you need to write a loop, you should think of an invariant that should be satisfied by it. If you can come up with an invariant that, if satisfied when the loop terminates guarantees a property you are interested in, then you have reduced the looping problem to the problem of satisfying the invariant at the end of each loop iteration. Guaranteeing that the invariant is satisfied at the end of a loop body, provided it is satisfied at the beginning, is often much easier than guaranteeing some global property about the loop.

As an example we can consider a function that should find the index of the smallest and largest element in a list (in case of ties, any index of a smallest and a largest element will do).

```python
def smallest_and_largest(x):
  # return an index for the smallest and largest
  # element in x.
  pass
```

This naturally calls for a loop and two indices we should return.

```python
def smallest_and_largest(x):
  smallest_index, largest_index = 0, 0
  for i in range(len(x)):
    pass # stuff goes here
  return smallest_index, largest_index
```

I initialise the smallest and largest index with 0, but what does it take to set them to the right values at the end of the function?

At the end of the loop we want `smallest_index` to point to a smallest element and `largest_index` to point to a largest. At any particular iteration of the loop, we have `i` point to some index into `x`. A natural idea would then be to insist on an invariant that concerns the prefix of `x` up to element `i`, `x[:i]`. We can use this invariant:

```python
def smallest_and_largest(x):
  smallest_index, largest_index = 0, 0
  for i in range(len(x)):
  	# Inv: smallest_index points to a smallest element in x[:i]
  	# Inv: largest_index points to a largest element in x[:i]
    pass # stuff goes here
  return smallest_index, largest_index
```

If the invariant holds when the loop terminates, we have the right values for `smallest_index` and `largest_index`, so we have reduced the task to guaranteeing the invariant in each iteration of the loop.

First, we want to ensure that the invariant is actually satisfied before the first iteration of the loop. If it isn't, then we cannot use the invariant as an assumption when we show that it will be satisfied at the end of the loop body. However, at the beginning of the loop, the list `x[:i]` is empty, so although `smallest_index` and `largest_index` point at index zero, they are not violating the invariant. The invariant is true at the beginning of the loop, but trivially so. We actually want them to be *indices* into `x[:i]`, and that they are not (simply because there aren't *any* indices into `x[:i]`, which is empty).

Empty lists are always a special case, and we haven't even specified what the function should return in case `x` is empty. We initialise the variables to zero, so let us say that this should be the return value if `x` is empty. Keeping in mind, though, that we have a special case for empty lists, we also have a special case when `i` is zero and `x[:i]` is empty. We therefore need to be careful in the first iteration of the loop.

Anyway, now we need to provide a loop body that guarantees the invariant at the end of it. So what we have at the beginning of the body is that `smallest_index` and `largest_index` points to the smallest and largest indices, respectively, of `x[:i]`. At the end of the body, we want them to point to the smallest and largest indices of `x[:i+1]` to satisfy the invariant at the next iteration of the loop.

To implement the loop body, we need to figure out how to update the indices to take the next element in `x` into account. This, however, is relatively straightforward. If `x[i]` is smaller than `x[smallest_index]`, then `smallest_index` must be updated. If `x[i]` is larger than `x[largest_index]`, then `largest_index` must be updated.

```python
def smallest_and_largest(x):
  smallest_index, largest_index = 0, 0
  for i in range(len(x)):
    # Inv: smallest_index points to a smallest element in x[:i]
    # Inv: largest_index points to a largest element in x[:i]
    if x[i] < x[smallest_index]:
      smallest_index = i
    if x[largest_index] < x[i]:
      largest_index = i
  return smallest_index, largest_index
```

This will obviously satisfy the invariant, provided `smallest_index` and `largest_index` are actually indices into `x[:i]`, which the invariant guarantees when `x[:i]` is not empty. When `x[:i]` is empty, though, we are dealing with `i==0` and there these two variables automatically point to the smallest and largest (and only) element in `x[:i+1]`, so we are fine.

There is a lot of invariant going on in this simple example, and normally we wouldn't be so formal for trivial cases like this, but whenever you need to do something only slightly more complicated, thinking in terms of invariants will greatly help you.


### Recursion and "divide and conquer"

A general trick for developing an algorithm involves recursion and so-called "divide and conquer". The basic idea by recursion is to reduce a problem to a smaller problem of the same type that we can solve, well, recursively. With recursive solutions to a problem, we have some base cases we can handle directly and more complicated cases that we reduce to problems closer to the base cases. What the base cases are, and what it means to be closer to a base case, varies from problem to problem.

Divide and conquer is just the same idea. You have a problem that you split into sub-problems that you manage recursively, and then you combine the results of the recursive calls into a solution to the problem at the original level.

The merge sort algorithm we saw the second week is an example of divide and conquer. Another one is the so-called *quick sort* algorithm. For the latter, the idea is this: A list of length zero or 1 is already sorted, so that is a base case where we just return the input; for longer lists, we pick a random element, called the *pivot*, and split the list into those smaller, equal to, and larger than this element. A sorted list must have the smaller elements at the front, then the elements equal to the pivot, and then the larger elements at the end, but to be sorted, the smaller and larger elements must first be sorted. These are smaller sets, so we can sort them recursively. The entire algorithm looks like this:

```python
from random import randint
def quick_sort(x):
  # base case
  if len(x) <= 1:
    return x
  # recursive case
  pivot = x[randint(0, len(x)-1)]
  equal = [e for e in x if e == pivot]
  smaller = [e for e in x if e < pivot]
  larger = [e for e in x if e > pivot]
  return quick_sort(smaller) + equal + quick_sort(larger)
```

The general form for divide and conquer is this:

1. Split the problem into subproblems
2. Recursively solve subproblems
3. Combine the solutions to the subproblems into a solution to the main problem

Here, the splitting is done based on the pivot, the recursive solutions are to `smaller` and `larger`, and the combination at the end is list concatenation.

The worst-case complexity of quick sort is actually O(n^2) because we might might end up with almost all elements in `smaller` or `larger`, but if we pick a random pivot, then we expect the two subproblems to be of roughly the same size, and then then running time is O(n log n). Because there is very little overhead in the algorithm, it is quick---thus the name.

In the implementation above, I create new lists for `equal`, `smaller`, and `larger`. This does incur some overhead that can be avoided by just rearranging the elements in `x`, but the code for that is less elegant. I leave that as an exercises for you to try out.

### Dynamic programming

A final example of a general trick I will mention is *dynamic programming*. The name is more fancy than the idea; the idea is simply this: instead of computing the same values several times in a recursive call, use a table and remember them.

Any recursive solution to a problem, we can also think of as a solution that builds up from simple parts and combine to a more complex part; we can think of starting with the base cases and then combining solutions rather than splitting complicated cases and recursing. In practise, one approach might be much simpler than another---in the quick sort example, it would not be obvious where to start the computation at the most basic level because it depends on the pivot at a higher level---but in principle, we can reverse the order of computations.

Consider computing the factorial of a number, *n*. This is a classical recursive problem since *n!=n*(n-1)!*. In Python, we can implement this recursively as

```python
def rec_factorial(n):
  if n <= 1:
    return 1
  else:
    return n * rec_factorial(n - 1)
```
 
However, we could also start from the basic case and build up the solution like this:

```python
def dynprog_factorial(n):
  table = [1] * n
  for i in range(1, n):
    table[i] = i * table[i-1]
  return n * table[n-1]
```

Here, I use a table to store intermediate values, but I could just keep an accumulator variable. I keep the table here to show the similarity with the dynamic programming example coming up...

There isn't any difference in running time between the two solutions. The second use more memory because it stores the table, but the running time is the same. Everything we use in the computation is only used once. Consider, however, Fibonnacci numbers instead. Here the *n*'th number depends on the two previous numbers, so a recursive solution will have to compute the same values more than once.

```python
def rec_fibonacci(n):
  if n <= 2:
    return 1
  else:
    return rec_fibonacci(n-1) + rec_fibonacci(n - 2)
```

Here, if we store the intermediate values, we get a much faster solution:

```python
def dynprog_fibonacci(n):
  table = [1] * n
  for i in range(3, n):
    table[i] = table[i-1] + table[i-2]
  return table[n-1] + table[n-2]
```

As an exercise, I suggest you experiment with the two solutions and compare their running time.



## Exercises

* Dynamic programming examples (JVG 13)
