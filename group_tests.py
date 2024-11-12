import group
import unittest
class TestCases(unittest.TestCase):
    def test_groups_of_3(self):
        list = [1,2,3,4,5,6,7,8,9]
        result = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual(group.groups_of_3(list), result)
    def test_groups_of_3_2(self):
        list = [1,2,3,4,5,6,7]
        list2 = [1, 2, 3, 4, 5, 6, 7,8]
        result = [[1,2,3],[4,5,6],[7]]
        result2 = [[1, 2, 3], [4, 5, 6], [7,8]]
        self.assertEqual(group.groups_of_3(list), result)
        self.assertEqual(group.groups_of_3(list2), result2)
if __name__ == '__main__':
    unittest.main()
