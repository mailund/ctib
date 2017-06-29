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

Most computational tasks we care about pertain to the real world. True, some we might be interested in for fun or simple curiosity, but by far the most problems we address computationally somehow reflect a goal we wish to achieve in the real world. It is just that the real world, and goals in the real world, can be terribly fuzzy and hard to pin down. If you ask your GPS to find you the "best route" to somewhere, what does "best" mean? Fastest? Most scenic? Safest to travel? It requires human-like intelligence and familiarity with your preferences to even consider that request.

To work with computation at the level where we can instruct electronic computers how to perform said computations, we need to get much more specific. We need to specify what our goals are with mathematical precision. To get from a goal in the real world to computations performed by a computer, we need to go through several steps, some moving from the concrete to the abstract, and then some moving from the abstract back to the concrete again.

The real world is much too complex to consider in full when we need to achieve a specific goal. To compute the trajectory of a spacecraft, we might consider General Relativity, although Newtonian mechanics usually suffice, but we would never try to take gravity waves into account. For GPS to work, you *do* need to take Relativity into account, but not Quantum Electrodynamics. We cannot consider all the complexities of the real world when we need to solve a specific goal, so we need to construct abstract models of the world in which we can consider problems and solutions.

Building models of the world is an essential part of computational thinking. Most people, when thinking about programming and software development, focus on the actual design and implementation of algorithms, but implementing programs for solving problems is secondary to specifying what the problems actually *are*, and that depends crucially on which model of the world we are considering. Constructing models of the world that both captures the essential aspects of what we need to consider to address a goal, and at the same time allows us to work with some mathematical convenience with the model, is often the hardest part of getting from goals to solutions. Luckily, it is not something we need to consider all that often; once we have a good model of certain aspects of the world, we can usually get away with reusing that model to consider a wealth of other goals. We reuse models all the time. Physics theories are models of the world, and most people doing physics try to understand how the world pertain to certain models; they do not invent new models all the time. The same goes for computations. For certain goals, we usually have an agreed upon model of the world in which we consider solutions---it would in some sense be considered bad form to change the model every time a solution doesn't pan out or doesn't perform as well as one would hope, although it isn't unheard of. Modelling the world is hard. We do it when we have to, but good models often exist for us to reuse.





![Going from goals in the real world to computational implementations.](figures/From World To Implementation.png)


### Basic building blocks of algorithms


## Exercises

* Introduction to Python programming and Jupyter notebooks. 
* Branching and looping (JVG 2 + 3)

