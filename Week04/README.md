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

### Dynamic programming

 
## Exercises

* Dynamic programming examples (JVG 13)
