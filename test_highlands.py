import unittest

from pos_logic import (
    calculate_total,
    add_to_order,
    InvalidQuantityError,
    current_order
)


class TestHighlandsPOS(unittest.TestCase):

    def setUp(self):
        current_order.clear()

    def test_calculate_total(self):

        mock_order = [
            {
                "code": "P1",
                "quantity": 2
            },
            {
                "code": "F1",
                "quantity": 1
            }
        ]

        result = calculate_total(
            mock_order
        )

        self.assertEqual(
            result,
            125000
        )

    def test_invalid_quantity(self):

        with self.assertRaises(
            InvalidQuantityError
        ):
            add_to_order(
                "P1",
                -1
            )


if __name__ == "__main__":
    unittest.main()