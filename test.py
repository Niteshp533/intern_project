import unittest
from dict2 import Dict2, KeyNotFoundError

class TestDict2(unittest.TestCase):
    def test_store_and_retrieve_values(self):
        obj = Dict2()
        obj['a'] = 1
        obj['b'] = 2
        obj['c'] = 3

        self.assertEqual(obj['a'], 1)
        self.assertEqual(obj['b'], 2)
        self.assertEqual(obj['c'], 3)

    def test_key_not_found_exception(self):
        obj = Dict2()
        with self.assertRaises(KeyNotFoundError):
            val = obj['a']

    def test_iterate_over_keys(self):
        obj = Dict2()
        obj['a'] = 1
        obj['b'] = 2
        obj['c'] = 3

        keys = []
        for k in obj:
            keys.append(k)

        self.assertEqual(keys, ['a', 'b', 'c'])

    def test_update_existing_key(self):
        obj = Dict2()
        obj['a'] = 1
        obj['a'] = 5

        self.assertEqual(obj['a'], 5)

if __name__ == '__main__':
    unittest.main()
