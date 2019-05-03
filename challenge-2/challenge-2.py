'''
CHALLENGE 2 INSTRUCTIONS:
Complete the constructor and method definitions within the SparseMatrix class below.  You will be critiqued on how well your code handles corner cases (these include exceptions)!

The stubbed-out unit test below is not required; only try filling it out if you feel like it!
'''
# DO NOT ADD/MODIFY THE IMPORTS
import unittest  # for optional unittests

class SparseMatrix(object):
    ''' SparseMatrix is intended to be a pythonic object that minimally represents (in terms of memory) a sparse matrix.  Please fill in the methods below.'''
    def __init__(self, n_rows, n_cols, nonzero_values):
        '''
        Args:
        - n_rows - number of rows
        - n_cols - number of cols
        - nonzero_vals - data structure with nonzero values defined (HINT: you may find a dictionary useful here)
        '''
        self.nonzero_values = nonzero_values

    def at(self, i, j):
        '''
        Args:
        - i - row index
        - j - col index
        Returns:
        - value of sparse matrix at row i and column j
        '''
        # TODO fill this in
        pass

    def add(self, other_sparse_matrix):
        '''
        Args:
        - other_sparse_matrix - SparseMatrix object whose nonzero_values are to be added to self.nonzero_values
        Returns:
        - 
        BONUS POINTS: Strictly handle the requirement that other_sparse_matrix is actually a SparseMatrix object
        '''
        # TODO fill this in
        # NOTE be careful here; there are a few corner-cases to consider
        pass


''' BELOW HERE IS ALL BONUS '''
class TestSparseMatrix(unittest.TestCase):
    # setup necessary definitions for unit tests here
    def test_sparse_matrix_at(self):
        # TODO fill this in
        pass
    def test_sparse_matrix_add(self):
        # TODO fill this in
        pass


if __name__ == '__main__':
    unittest.main()
