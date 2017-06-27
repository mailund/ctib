# Week 1: Introduction to computational thinking

## Objectives

* **To understand how we go from problem domains to models, specify problems and goals, derive algorithmic solutions, and finally implement our solutions.**
* **To get familiarity with programming in the Python programming language and using Jupyter notebooks.**

## Lecture notes

### What is computational thinking?

The focus of this class is to learn how to *formalise objectives * we are interested in, for whatever reason, in such a way that we can specify *mathematically and objectively* what solutions to our objectives are. Once we have such objective goals---so we know exactly what solutions will look like---we can derive ways of achieving such solutions as a *series of computations:* recipes that, if followed mindlessly step by step, will provide a solution.

There might be many such recipes for solutions, but we can compare them based on their (theoretical) *efficiency*---some recipes intrinsically reach a solution faster than others. When thinking about efficiency, we will need to abstract away some aspects of concrete solutions. Not all steps in a recipe are equal; some operations are harder than others. It is harder to take the square root of a number than it is to add two to the number. How hard each operation is depends on the computer (human or machine) doing the operations. An exact estimate of how long a computation will take is hard to derive---it is much easier to simply measure the time it takes to follow the recipe---but for obvious reasons we don't choose the best recipe to solve a problem by solving it multiple times with different approaches and then preferring the fastest one.

We can abstract away some details of operations in recipes and get general ideas about how efficient different approaches to solving a problem are. This won't be perfectly accurate, but it will in general let us choose recipes that are good candidates for the best way of achieving solutions. After that, it might makes sense to do some experiments with measuring the performance of selected approaches on selected problems---typically smaller problems than the one we really want to solve, since it is obviously daft to solve the real problem many times to find out the best way to solve it.

Before we can do any measurements, though---and before we can use a recipe to solve the initial objects---we need to implement the recipe in a way that can be followed by a computer. If the computer is a human, a rough description of the approach will often be enough. Humans are good at working out ambiguities and figuring out the intended meaning behind an instruction if it is somewhat vague. If the computer is an actual electronic computer, things are more difficult---at least until we achieve AI.

There are many different ways to implement a recipe for a computer to follow, but the steps it takes are usually the same regardless of how we end up implementing the recipe at the end: we need to *break down the steps to follow into more and more primitive steps* until the steps are so primitive they can easily be followed by the computer.

If you are new to instructing computers on what to do, this can be very frustrating. Electronic computers rarely take high-level instructions; you need to tell them how to do *everything*. And you need to tell them exactly *how*. If there is any ambiguity, they cannot follow instructions; if there is any way of misunderstanding you and doing the wrong thing, you bet they will do so.

The good news is that what it takes to break down steps in a recipe into more primitive steps is just following the same approach as working out our original recipe: we have an objective---the step, or computation, we need done---so we formalise what the solution is and then we derive a recipe for getting the solution.

What all of this boils down to is thinking about achieving solutions as doing a computation---and breaking down computations into steps that are themselves computations---and all of this is *computational thinking*.

### Programs, models, and the real world

### Basic building blocks of algorithms


## Exercises

* Introduction to Python programming and Jupyter notebooks. 
* Branching and looping (JVG 2 + 3)

