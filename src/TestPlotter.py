import unittest
import plotter

class TestPlotter(unittest.TestCase):
    # plot function as well as eval function are already tested, 
    # so we only need to test the validate_expression function

    def test_validate_expression(self):
        self.assertEqual(plotter.validate_expression('x ^ 2 + 5 * x + 37'), 'x ** 2 + 5 * x + 37')
        self.assertEqual(plotter.validate_expression('(x + 5) ^ 3 + 5 * (x - 4) - 222 '), '(x + 5) ** 3 + 5 * (x - 4) - 222 ')

        with self.assertRaises(ValueError) as exception1:
            plotter.validate_expression('x + 5 +')
        self.assertEqual(exception1.exception.args[0], 'ERROR: last operator without a second operand!')

        with self.assertRaises(ValueError) as exception2:
            plotter.validate_expression('y + 3')
        self.assertEqual(exception2.exception.args[0], 'ERROR: Invalid symbol exists! \'y\'')

        with self.assertRaises(ValueError) as exception3:
            plotter.validate_expression('x^2 + 3 * xx')
        self.assertEqual(exception3.exception.args[0], 'ERROR: consecutive operands without a seperating operator!')

        with self.assertRaises(ValueError) as exception4:
            plotter.validate_expression('x^2 + 3x')
        self.assertEqual(exception4.exception.args[0], 'ERROR: consecutive operands without a seperating operator!')

        with self.assertRaises(ValueError) as exception5:
            plotter.validate_expression('x + 2 3')
        self.assertEqual(exception5.exception.args[0], 'ERROR: there is a space inside a number!')

        with self.assertRaises(ValueError) as exception6:
            plotter.validate_expression(' + x')
        self.assertEqual(exception6.exception.args[0], 'ERROR: there exists an operator without a first operand!')

        with self.assertRaises(ValueError) as exception7:
            plotter.validate_expression('x ++ 5')
        self.assertEqual(exception7.exception.args[0], 'ERROR: there exists an operator without a first operand!')

        with self.assertRaises(ValueError) as exception8:
            plotter.validate_expression('3 (* x)')
        self.assertEqual(exception8.exception.args[0], 'ERROR: brackets misplacing!')

        with self.assertRaises(ValueError) as exception9:
            plotter.validate_expression('(3 *) x')
        self.assertEqual(exception9.exception.args[0], 'ERROR: brackets misplacing!')

        with self.assertRaises(ValueError) as exception10:
            plotter.validate_expression('(3 * x) + 5)')
        self.assertEqual(exception10.exception.args[0], 'ERROR: There is a closing bracket without an opening one!')

        with self.assertRaises(ValueError) as exception11:
            plotter.validate_expression('x % 2')
        self.assertEqual(exception11.exception.args[0], 'ERROR: Invalid symbol exists! \'%\'')

        with self.assertRaises(ValueError) as exception12:
            plotter.validate_expression('X + 2')
        self.assertEqual(exception12.exception.args[0], 'ERROR: Invalid symbol exists! \'X\'')

        with self.assertRaises(ValueError) as exception13:
            plotter.validate_expression('(x ^ 2) + (3 * x')
        self.assertEqual(exception13.exception.args[0], 'ERROR: There is an opening bracket without a closing one!')


if __name__ == '__main__':
    unittest.main()