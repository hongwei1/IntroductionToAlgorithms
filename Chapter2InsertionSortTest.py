import unittest

from Chapter2InsertionSort import chapter2InsertionSort


class Chapter2InsertionSortTest(unittest.TestCase):

    def test_get_min_value_and_index(self):
        abc = chapter2InsertionSort.get_min_value_and_index([1, 2, 3])
        self.assertEqual(abc, (1,0))
        # self.assertEqual(abc._1)

    def test_swap_two_items(self):
        abc = chapter2InsertionSort.swap_two_items([1, 2, 3], 0,2)
        self.assertEqual(abc, [3, 2, 1])

    def test_my_sort_algorithm(self):
        abc = chapter2InsertionSort.my_sort_algorithm([3, 1, 2])
        self.assertEqual(abc, [1, 2, 3])
        abc = chapter2InsertionSort.my_sort_algorithm([3, 1, 2,10,123,23,8,10])
        self.assertEqual(abc, [1, 2, 3, 8, 10, 10, 23, 123])

    def test_insertion_sort(self):
        # abc = chapter2InsertionSort.insertion_sort([3, 1, 2])
        # self.assertEqual(abc, [1, 2, 3])
        abc = chapter2InsertionSort.insertion_sort([3, 1, 2,10,123,23,8,10])
        self.assertEqual(abc, [1, 2, 3, 8, 10, 10, 23, 123])

if __name__ == '__main__':
    unittest.main()