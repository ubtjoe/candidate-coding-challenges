## Coding Challenge 2 - Sparse Matrix
### Summary
If you are unfamiliar with what a sparse matrix is, check out the [Wikipedia page](https://en.wikipedia.org/wiki/Sparse_matrix).  Common computational representations of sparse matrices are discussed [here](https://cmdlinetips.com/2018/03/sparse-matrices-in-python-with-scipy/)

The challenge here is to construct a `SparseMatrix` class in your language of choice that can be used to create sparse matrices from scratch with limited memory.  Two popular methods to consider are the _row-based linked list_- and the _dictionary of keys_-based approaches.  See the second link above for more details.  Whichever method you choose, provide a quick justification in your source file.

Within your `SparseMatrix` class, you will need to implement the following public methods:

* `at` - this method returns the value of the current sparse matrix at a given row and column.  Given that the matrix is sparse, this will _usually_ return 0.
* `add` - this method adds the values of one sparse matrix to the _current_ sparse matrix - _This method should not return a copy!_

_Note: Your indexing should match the convention of the language you choose (python/c are zero-based, matlab/fortran are 1-based)_

_If you do not use the python stubs provided, you must provide a separate,  _complete_, set of instructions for building and running your solution.  Failure to do so will result in an automatic fail._

### Challenge Requirements

* Create `SparseMatrix` class - make sure that your choice of representation (e.g. row-based linked list or other) is stated clearly with justification.  The data type for your matrix should be `float` or `double`.
* Whichever language you choose, _make sure that your interface matches the one defined in challenge-2.py_.
* Correctly implement `at` method and verify with unit tests
* Correctly implement `add` method - verify with unit tests

#### Design Considerations

* You may assume that the matrix you are trying to represent is _actually_ sparse; no checks for density should be implemented
* Have you implemented the required features in a straightforward way?  If your intent is unclear, did you provide clarifying comments?
* What corner cases could be encountered here?  Does your solution handle all of them?

You should plan on spending between one to two hours here.

