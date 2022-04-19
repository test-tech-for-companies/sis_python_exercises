#!/usr/bin/env python3
"""
Unittest
"""

import unittest


from lockcaja import desbloqueo


class UnblockBoxesTest(unittest.TestCase):
    """
    class auto test
    """

    def test_unblock_boxes(self):
        """test_unblock_boxes
        """
    
        input_vars = [
            		[[1], [2], [3], [4], []], 
                    [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]],
                    [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]],
                    [[0]]
                    ]

        results = [True, True, False, True]

        for variant, (boxes, contains) in enumerate(zip(input_vars, results), start = 1):
            error_message = f'box {boxes}. invalid'
            
            with self.subTest(f'variation #{variant}', input=boxes, output=contains):
                  self.assertEqual(contains, desbloqueo(boxes), msg=error_message)


if __name__ == "__main__":
    unittest.main()
                  
                  
