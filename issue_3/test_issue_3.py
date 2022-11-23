import unittest
from one_hot_encoder import fit_transform


class TestOneHotEncoder(unittest.TestCase):

    def test_list_strings(self):
        test_list = ['slim', 'shady', 'party', 'norimyxxxo']
        actual = fit_transform(test_list)
        expected = [('slim', [0, 0, 0, 1]),
                    ('shady', [0, 0, 1, 0]),
                    ('party', [0, 1, 0, 0]),
                    ('norimyxxxo', [1, 0, 0, 0])]
        self.assertEqual(actual, expected)

    def test_empty(self):
        with self.assertRaises(TypeError) as cm:
            fit_transform()
        error = cm.exception
        self.assertIsInstance(error, TypeError)

    def test_string(self):
        test_list = ['another', 'one']
        container = fit_transform(test_list)
        member = ('one', [1, 0])
        self.assertIn(member, container)

    def test_empty_list(self):
        empty_list = []
        actual = fit_transform(empty_list)
        self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
