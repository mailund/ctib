# Week 5: Data structures and trees

## Objectives

* **Get familiar with the tree data structure and how to traverse and modify trees.**

## Lectures notes

There are different ways that we can represent data structures, but all based on classes and objects. We won't work much with those in this class, though, so I hope you can generalise from examples. This week we look at tree data structures, and you can see ways of representing these in the [Trees notebook](src/Trees.ipynb).

### Search trees

Search trees are binary trees with the following property: For all inner nodes, all values in the left subtree are smaller than the value in the node and all values in the right tree are larger than the value in the node. This property makes it efficient to search for values in a search tree: you compare the value you are searching for with the value in the node, if you have found the value you are done, otherwise you search either left or right depending on whether your search key is smaller or larger than the value in the root. You can read more about search trees in the [SearchTrees notebook](src/SearchTrees.ipynb).

### Heaps

The heap property of a tree is this: the value at the root of a tree is always smaller than all values in its subtrees. This means that we can always access the smallest element in a set that we have stored in a heap tree by accessing the value in the root. You can read more about heaps in the [Heaps notebook](src/Heaps.ipynb).

## Exercises

* [Tree traversal](exercises/TreeTraversal.ipynb)
* [Red-black search trees](exercises/RedBlackTrees.ipynb)

