import unittest
from sudoku import solve

class TestCaseSudoku(unittest.TestCase):
    def test_given_test(self):
        grid0 = [[0, 0, 8, 0, 0, 0, 0, 1, 6],  # Data type for sudoku puzzles:
                 [5, 0, 0, 0, 9, 2, 0, 0, 8],  # a list of 9 lists, each of 9 digits.
                 [0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [9, 0, 0, 3, 0, 0, 8, 2, 0],  # grid0 is a global variable used by readFile()
                 [0, 2, 0, 0, 0, 0, 0, 7, 0],
                 [0, 8, 4, 0, 0, 6, 0, 0, 5],  # This sudoku is solved when there is no
                 [0, 0, 0, 0, 0, 3, 0, 0, 0],  # filename argument on the command line.
                 [4, 0, 0, 9, 6, 0, 0, 0, 2],
                 [1, 6, 0, 0, 0, 0, 7, 0, 0]]

        solution = [[2, 4, 8, 7, 3, 5, 9, 1, 6],  # Data type for sudoku puzzles:
                 [5, 7, 1, 6, 9, 2, 4, 3, 8],  # a list of 9 lists, each of 9 digits.
                 [6, 9, 3, 1, 8, 4, 2, 5, 7],
                 [9, 1, 6, 3, 5, 7, 8, 2, 4],  # grid0 is a global variable used by readFile()
                 [3, 2, 5, 8, 4, 9, 6, 7, 1],
                 [7, 8, 4, 2, 1, 6, 3, 9, 5],  # This sudoku is solved when there is no
                 [8, 5, 2, 4, 7, 3, 1, 6, 9],  # filename argument on the command line.
                 [4, 3, 7, 9, 6, 1, 5, 8, 2],
                 [1, 6, 9, 5, 2, 8, 7, 4, 3]]

        self.assertTrue(solve(grid0))
        self.assertEqual(grid0, solution)

    def test_wikiGrid(self ):
        wiki_grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9]]

        wiki_solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                        [6, 7, 2, 1, 9, 5, 3, 4, 8],
                        [1, 9, 8, 3, 4, 2, 5, 6, 7],
                        [8, 5, 9, 7, 6, 1, 4, 2, 3],
                        [4, 2, 6, 8, 5, 3, 7, 9, 1],
                        [7, 1, 3, 9, 2, 4, 8, 5, 6],
                        [9, 6, 1, 5, 3, 7, 2, 8, 4],
                        [2, 8, 7, 4, 1, 9, 6, 3, 5],
                        [3, 4, 5, 2, 8, 6, 1, 7, 9]]

        self.assertTrue(solve(wiki_grid))
        self.assertEqual(wiki_grid, wiki_solution)

    def test_random(self):
        random_grid = [
    [0, 0, 0, 4, 1, 0, 3, 7, 8],
    [0, 0, 0, 7, 0, 0, 0, 2, 9],
    [3, 0, 4, 0, 0, 0, 5, 0, 0],
    [0, 5, 3, 0, 0, 0, 0, 0, 6],
    [2, 0, 8, 0, 9, 6, 0, 0, 5],
    [0, 0, 0, 0, 0, 7, 0, 0, 0],
    [0, 4, 9, 0, 0, 0, 0, 5, 0],
    [5, 0, 0, 6, 0, 0, 9, 0, 4],
    [0, 0, 0, 0, 4, 0, 6, 0, 3]]

        random_solution = [
    [9, 6, 2, 4, 1, 5, 3, 7, 8],
    [1, 8, 5, 7, 6, 3, 4, 2, 9],
    [3, 7, 4, 9, 2, 8, 5, 6, 1],
    [7, 5, 3, 2, 8, 4, 1, 9, 6],
    [2, 1, 8, 3, 9, 6, 7, 4, 5],
    [4, 9, 6, 1, 5, 7, 8, 3, 2],
    [6, 4, 9, 8, 3, 1, 2, 5, 7],
    [5, 3, 1, 6, 7, 2, 9, 8, 4],
    [8, 2, 7, 5, 4, 9, 6, 1, 3]]

        self.assertTrue(solve(random_grid))
        self.assertEqual(random_grid, random_solution)

    def test_secondrandom(self):
        secondrandom_grid = [
    [9, 1, 0, 0, 0, 6, 2, 0, 7],
    [0, 8, 7, 0, 0, 0, 1, 0, 0],
    [2, 0, 4, 0, 0, 9, 0, 0, 0],
    [0, 0, 9, 5, 0, 8, 0, 1, 2],
    [0, 6, 0, 4, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 7, 0],
    [0, 0, 0, 3, 0, 7, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 4, 3, 0],
    [0, 0, 5, 0, 9, 0, 7, 8, 1]
]

        secondrandom_solution = [
    [9, 1, 3, 8, 5, 6, 2, 4, 7],
    [6, 8, 7, 2, 3, 4, 1, 9, 5],
    [2, 5, 4, 7, 1, 9, 8, 6, 3],
    [4, 7, 9, 5, 6, 8, 3, 1, 2],
    [1, 6, 2, 4, 7, 3, 9, 5, 8],
    [5, 3, 8, 9, 2, 1, 6, 7, 4],
    [8, 9, 1, 3, 4, 7, 5, 2, 6],
    [7, 2, 6, 1, 8, 5, 4, 3, 9],
    [3, 4, 5, 6, 9, 2, 7, 8, 1]
]
        self.assertTrue(solve(secondrandom_grid))
        self.assertEqual(secondrandom_grid, secondrandom_solution)

    def test_failing(self):
        failing_grid = [[0, 0, 3, 0, 0, 2, 0, 4, 0],
                       [0, 0, 0, 0, 0, 6, 8, 0, 0],
                       [0, 2, 6, 8, 4, 0, 0, 3, 1],
                       [1, 7, 0, 3, 2, 0, 0, 0, 0],
                       [0, 0, 0, 4, 5, 0, 2, 0, 8],
                       [0, 0, 0, 0, 0, 2, 0, 0, 0],
                       [0, 5, 0, 7, 0, 0, 9, 6, 0],
                       [0, 0, 0, 7, 0, 4, 0, 0, 5],
                       [9, 8, 3, 0, 0, 5, 0, 0, 0]]

        self.assertFalse(solve(failing_grid))

    def test_failingagain(self):
        failingagain_grid = [[0, 0, 2, 0, 0, 3, 0, 4, 0],
                            [0, 0, 0, 0, 0, 6, 8, 0, 0],
                            [0, 2, 6, 8, 4, 0, 0, 2, 1],
                            [3, 9, 0, 3, 2, 0, 0, 0, 0],
                            [0, 0, 0, 4, 5, 0, 2, 0, 8],
                            [0, 0, 0, 0, 0, 4, 0, 0, 0],
                            [0, 5, 0, 7, 0, 0, 4, 6, 0],
                            [0, 0, 0, 8, 0, 4, 0, 0, 9],
                            [9, 8, 3, 0, 0, 5, 0, 0, 0]]

        self.assertFalse(solve(failingagain_grid))




if __name__ == '__main__':
    unittest.main()