## Coding Challenge 2
### Sparse Matrix Implementation

If you are unfamiliar with what a sparse matrix is, check out the [Wikipedia page](https://en.wikipedia.org/wiki/Sparse_matrix).

The challenge here is to construct a `SparseMatrix` class in python (or, if you prefer, your language of choice) that considers representation of a sparse matriix with as little memory as necessary.  There are many useful methods for operating on/with sparse matrices but, in the interest of time, you only need to implement the following:

* `at` - this method returns the value of the current sparse matrix at a given row and column.  Given that the matrix is sparse, this will _usually_ return 0.
* `add` - this method adds the values of one sparse matrix to the current sparse matrix.

There are many corner-cases to consider, so be cautious here!

You should plan on spending between one and two hours here.

#### Bonus
There are the beginnings of a unit test at the end of the included python file.  If you want to test how robust your code is, fill this section out and try running it.  If all was successful, you should see something like the following:

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
