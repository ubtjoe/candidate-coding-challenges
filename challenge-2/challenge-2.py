import unittest  # used to test the implementation

class SparseMatrix(object):
    ''' SparseMatrix class constructor'''
    # TODO: identify and justify approach
    def __init__(self, n_rows, n_cols, nonzero_values=None):
        '''
        SparseMatrix constructor

        args:
        n_rows - number of rows
        n_cols - number of cols
        
        kwargs:
        nonzero_values - data structure with nonzero values defined (default={})
        '''
        # TODO fill this in
        pass

    def at(self, i, j):
        '''
        Return value of matrix at row `i` and column `j`
        
        args:
        i - row index
        j - column index
        
        Returns:
        value of sparse matrix at row i and column j
        '''
        # TODO fill this in
        pass

    def add(self, other_sparse_matrix):
        '''
        Add input matrix to matrix
        
        args:
        other_sparse_matrix - SparseMatrix object whose nonzero_values are to be added to self.nonzero_values
        
        Returns:
        None
        '''
        # TODO fill this in
        pass


'''You may find the following snippet helpful in setting up your unit tests'''
class TestSparseMatrix(unittest.TestCase):
    def test_sparse_matrix_constructor(self):
        pass

    def test_sparse_matrix_at(self):
        pass
    
    def test_sparse_matrix_add(self):
        pass


if __name__ == '__main__':
    unittest.main()
