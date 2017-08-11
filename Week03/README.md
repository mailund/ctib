# Week 3: Implementing algorithms

## Objectives

* **To understand the steps involved in implementing an algorithm.**
* **To learn how to experimentally evaluate an algorithm.**

## Lectures notes

### Implementing an algorithm

The goal of this week is learning how to implement an algorithm. This is potentially more complicated than it sounds, depending on the algorithm, because we usually have the description of an algorithm at a reasonable high level, but we need to get to a relatively low level before we can write the code that tells the computer how to run the algorithm.

#### Binary search

As an example we take *binary search*. This is the search strategy you use when you look up a word in a dictionary---at least it used to be when dictionaries were printed on paper. You don't search from the beginning of a sequence of words, rather you exploit that the words are sorted, so you can look in the middle of your set of words and check if this is the word you are looking for. If it is not, you can check if the middle word is lexicographically smaller or larger than the word you are searching for. If it is smaller, you know that if the word you are looking for is in the dictionary, then it must be in the last half of the set. If it is larger, you know that the word must be in the first half of the set.

This approach is faster than a linear search through the elements in the dictionary. At each step, we can discard half of the elements in the dictionary, so the time to find the element we are looking for is O(log n) instead of O(n).

That is the prose description of the algorithm. We can try to break it into a more step-like description:

* Check the middle element of a list to see if it is what you are looking for. If it is, return `True`.
* If the middle element is not what you are searching for, check if it is larger or smaller than the element you are looking for.
* If smaller: search in the list following the middle element.
* If larger: search in the list up until the middle element.

This has a form that looks like we can immediately translate it into code, but code requires just a little more. First, we need to decide what interface the search function should have. We are going to just use it to check if an element is found in the list, not where it is, so we want it to return `True` or `False`, and we want it to be called with the element we search for and the (sorted) list to search in.

We can start with implementing a simple linear search. This can work as a substitute for our algorithm until we get it up and running, and we can use it for testing later on as well. This function could look like this:

```python
def linear_search(x, lst):
  for y in lst:
    if x == y:
      return True
  return False
```

To be able to replace this function with the binary search, we need that function to have the same interface.

```python
def binary_search(x, lst):
  # do binary search
  pass
```

The `pass` keyword here is just a way to make the function syntactically valid without us actually doing anything in the function. That is what we need to do now.

The algorithm wants us to check the middle element and then potentially search the first or the last half of `lst`. Now, we *could* implement a recursive function that splits `lst` but we learned last week that this would involve copying all the elements into the new list. If we took that approach, each call to the algorithm would take time O(n) so we would end up with an O(n log n) algorithm instead of an O(log n) algorithm. We want to avoid this, so we keep track of pointers into the list instead, and write the function on this form:

```python
def binary_search(x, lst):
  def recurse(start, end):
    # search between start and end
    pass
  return recurse(0, len(lst))
```

Now we have set everything up to implement the algorithm, so this is a perfect time for you to try it out yourself. Can you implement the algorithm, as it is described above, by filling out the body of `recurse`?

I will give you a chance to try.

Back again, now? Okay. You might have gotten it working, but let me still walk you through how I would continue from here.

Now, `recurse` should search in `lst` between `start` and `end`, but we have to be more precise about what that means. So first we make the invariant that `x`, if it exists in `lst`, then it is in `x[start:end]`. This means, among other things, that we index from *and including* `start` and to *but not including* `end`. This, in turn, means that if `start == end` then the list we should search in is empty, so we can return `False`.

```python
def binary_search(x, lst):
  def recurse(start, end):
    if start == end:
      return False
    # other cases here
    pass
  return recurse(0, len(lst))
```

We should also explicitly state the invariant that `start <= end`. We don't really need it right now, but if we want the invariant to be that if `x` is in `lst` then it is in `lst[start:end]`, then we want that additional invariant. It also makes sure that testing `start == end` as the termination condition for the recursion is sufficient.

It is always a good idea to be explicit about invariants, so let us annotation the function with them:

```python
def binary_search(x, lst):
  def recurse(start, end):
    # Inv: start <= end and x might be in lst[start:end].
    if start == end:
      return False
    # other cases here
    pass
  return recurse(0, len(lst))
```

The invariant, incidentally, also guarantees the post-condition that if we make it past the first `if` statement, then `start < end`.

```python
def binary_search(x, lst):
  def recurse(start, end):
    # Inv: start <= end and x might be in lst[start:end].
    if start == end:
      return False
    # Inv: start < end
    # other cases here
    pass
  return recurse(0, len(lst))
```

That might come in handy later.

But first, let us consider the next step in the algorithm. Here we need to check the middle element of the list. In `recurse`, the list we are interested in is, of course, `lst[start:end]` so the middle element must be computed from `start` and `end`. We get the index for it like this:

```python
def binary_search(x, lst):
  def recurse(start, end):
    # Inv: start <= end and x might be in lst[start:end].
    if start == end:
      return False
    i = start + (end - start) // 2
    if lst[i] == x:
      return True
    # Inv: start < end
    # other cases here
    pass
  return recurse(0, len(lst))
```

Here, I've both calculated the middle index and checked if the middle element is the one we are searching for. If it is, we should just return `True`.

All that remains is implementing the two recursive calls when the middle element is not the one we are searching for. This, we could do as follows:

```python
def binary_search(x, lst):
  def recurse(start, end):
    # Inv: start <= end and x might be in lst[start:end].
    if start == end:
      return False
    i = start + (end - start) // 2
    if lst[i] == x:
      return True
    # Inv: start < end	
    elif lst[i] < x:
      return recurse(i, end)
    else:
      return recurse(start, i)
  return recurse(0, len(lst))
```

This *looks* reasonable, but it is actually incorrect. It is one of those cases where the prose explanation of the algorithm is imprecise and we need to do better in the code. It is correct that we should look in the first or last half of the list, respectively, but implicit in calling recursively is the expectation that we only call recursively on problems that are *smaller* than the one we are already trying to deal with. If we simply call recursively with the exact same problem as we are trying to handle we will never get anyway.

Can this happen here? I'm glad you asked. Yes it can. The expression we use to compute `i` will set `i` to `start` if `end = start + 1`. We know that `start` is not equal to `end` at this point, but we could be looking at a list of length one, and if that is the case, then `start == i`. If `lst[i] > x`, this will not be a problem. We will recurse with `start == end` and terminate. No worries. If `lst[i] < x`, though, we will recurse with `recurse(i, end)` which is the same as `recurse(start, end)`. We are not reducing the problem, and we will just keep recursing until Python complaints that we have used up all its stack space.

Whenever we recurse, we must make sure that we recurse on a problem smaller than the one we are currently considering, so we must make sure that the interval is smaller for binary search. 

From how we compute `i` we know that `start <= i < end`. This means that we can recurse as `recurse(i + 1, end)` and still satisfy the function invariant `start <= end`, and since we only recurse when we know that `lst[i]` is not the element we are searching for, we can recurse this way and satisfy both invariants of the function. We can thus update the function to look like this:

```python
def binary_search(x, lst):
  def recurse(start, end):
    # Inv: start <= end and x might be in lst[start:end].
    if start == end:
      return False
    i = start + (end - start) // 2
    if lst[i] == x:
      return True
    # Inv: start < end	
    elif lst[i] < x:
      return recurse(i + 1, end)
    else:
      return recurse(start, i - 1)
  return recurse(0, len(lst))
```

We leave out the `i`th element in the recursive calls, so all should be fine now.

But wait! Our reasoning tells us that it is okay to call `recurse(i + 1, end)`, but in this version I also left out the `i`th element in `recurse(start, i - 1)`. Is *this* also correct?

In this recursion we are certainly making the problem we try to solve smaller and we know that `lst[i]` is not what we are searching for, so it should be safe, right?

No.

Remember that the invariant considers the interval `start:end` with `start` included and `end` excluded. If we recurse on `i - 1` we are removing more than element `i` from the list we search in. we are also removing `i - 1`. So we were a little too fast with generalising here. The correct implementation is this:

```python
def binary_search(x, lst):
  def recurse(start, end):
    # Inv: start <= end and x might be in lst[start:end].
    if start == end:
      return False
    i = start + (end - start) // 2
    if lst[i] == x:
      return True
    # Inv: start < end	
    elif lst[i] < x:
      return recurse(i, end)
    else:
      return recurse(start, i)
  return recurse(0, len(lst))
```

Binary search is a very simple algorithm, but as you can see, there is some work to be done to go from a high-level description of an algorithm---even a simple one such as this---to a working implementation.

I chose binary search as the example because there are these special cases around the boundaries of the interval. Binary search is known to be difficult to get right in the first attempt. It is not unusual in its complexity, though. And it *is* a simple algorithm.

The take home message is this: there are always some details missing in a prose description of an algorithm that you will have to flesh out when you implement it. Being careful with stating invariants and pre- and post-conditions can greatly alleviate the problems involved with translating prose into code.


### Testing an algorithm 

When it comes to implementations, you will want to test them. Even if you convince yourself that the algorithm is absolutely correct, all special cases are handled, all invariants are satisfied, all pigs are fed and ready to fly, there is always a chance that you have made a mistake at some point during the implementation. Testing can help reduce the chance of this.

The point of testing is not to guarantee that an implementation is correct. There is not really any way of doing this through testing; if your implementation works as intended on all the input you provide it in your testing, that does not guarantee that the *next* data you could give it will not trigger an error. We use formal reasoning to construct algorithms that we can mathematically prove will solve a given problem, but when it comes to an actual implementation and testing it, the goal is not to test correctness but rather to try to break the implementation. If we can break our implementation, that is great. It means that we have discovered an error, and now we can fix it. Don't be kind to your code. Hit it as hard as you can. The harder you hit it without breaking it, the more confidence you will have in it, but the goal of testing really is to break the code if possible.

How you attack your code when testing depends both on your actual code and your ingenuity. As long as you keep in mind that the goal is to break the code if possible, you are on the right path. There are some rules of thumbs, however, that often helps you trigger errors.

Always give your code some common-case data first. You will feel silly if you do a lot of testing and then find out that the code doesn't handle the most basic cases.

After that, throw special cases at the code. For numbers, make sure you use both negative and positive numbers and zero. For lists, give your code the empty list and lists of length one. What the special cases are depend on your code and your data, but always try to throw all those you can think of at your code.

Finally, if you can generate representative but random data, use that to test your code. Even when we try as hard as we can, it is hard to figure out data that really stresses our functions. Using random data enables us to test our code on large collections of input without having to dream up the data ourselves, and as an added benefit, random data is not likely to be coloured by our biased belief of what input data should look like, so it is often more successful at breaking our code.


### Evaluating running times

Just as we should test our code to see if there are errors in its functionality, even when we have proven that the algorithm is correct, we should also test its running time, even if we have proved its running time analytically. It is quite easy to make a mistake in an implementation that doesn't affect the correctness but changes the running time. Therefore, you should always run some experiments to validate that the running time of your implementation is what you would expect.

You can find a Jupyter Notebook [here](src/Performance.ipynb) that does this for the binary search. Download it and experiment with it.

 
## Exercises:

* Testing and debugging (JVG 6)
* Plotting (JVG 11.1)
* Complexity (JVG 9)
