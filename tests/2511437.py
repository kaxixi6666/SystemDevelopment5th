"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException


class TestAddition:
    """Tests for the add method."""
    # （已有的加法测试保持不变）
    def test_add_positive_numbers(self):
        calc = Calculator()
        assert calc.add(5, 3) == 8

    def test_add_negative_numbers(self):
        calc = Calculator()
        assert calc.add(-5, -3) == -8

    def test_add_positive_and_negative(self):
        calc = Calculator()
        assert calc.add(5, -3) == 2

    def test_add_negative_and_positive(self):
        calc = Calculator()
        assert calc.add(-5, 3) == -2

    def test_add_positive_with_zero(self):
        calc = Calculator()
        assert calc.add(5, 0) == 5

    def test_add_zero_with_positive(self):
        calc = Calculator()
        assert calc.add(0, 5) == 5

    def test_add_floats(self):
        calc = Calculator()
        assert calc.add(2.5, 3.7) == pytest.approx(6.2)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers (a > b)."""
        calc = Calculator()
        assert calc.subtract(10, 4) == 6

    def test_subtract_positive_numbers_reversed(self):
        """Test subtracting positive numbers (a < b)."""
        calc = Calculator()
        assert calc.subtract(4, 10) == -6

    def test_subtract_negative_numbers(self):
        """Test subtracting two negative numbers."""
        calc = Calculator()
        assert calc.subtract(-5, -3) == -2  # -5 - (-3) = -2

    def test_subtract_positive_and_negative(self):
        """Test subtracting negative from positive."""
        calc = Calculator()
        assert calc.subtract(5, -3) == 8  # 5 - (-3) = 8

    def test_subtract_negative_and_positive(self):
        """Test subtracting positive from negative."""
        calc = Calculator()
        assert calc.subtract(-5, 3) == -8  # -5 - 3 = -8

    def test_subtract_with_zero(self):
        """Test subtracting zero from a number."""
        calc = Calculator()
        assert calc.subtract(7, 0) == 7

    def test_subtract_number_from_zero(self):
        """Test subtracting a number from zero."""
        calc = Calculator()
        assert calc.subtract(0, 7) == -7

    def test_subtract_floats(self):
        """Test subtracting floating point numbers."""
        calc = Calculator()
        assert calc.subtract(5.5, 2.1) == pytest.approx(3.4)


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        calc = Calculator()
        assert calc.multiply(6, 7) == 42

    def test_multiply_negative_numbers(self):
        """Test multiplying two negative numbers (result positive)."""
        calc = Calculator()
        assert calc.multiply(-4, -5) == 20

    def test_multiply_positive_and_negative(self):
        """Test multiplying positive and negative (result negative)."""
        calc = Calculator()
        assert calc.multiply(3, -8) == -24

    def test_multiply_with_zero(self):
        """Test multiplying a number by zero."""
        calc = Calculator()
        assert calc.multiply(9, 0) == 0

    def test_multiply_zero_with_number(self):
        """Test multiplying zero by a number."""
        calc = Calculator()
        assert calc.multiply(0, 9) == 0

    def test_multiply_floats(self):
        """Test multiplying floating point numbers."""
        calc = Calculator()
        assert calc.multiply(2.5, 4.0) == pytest.approx(10.0)

    def test_multiply_by_one(self):
        """Test multiplying by 1 (identity)."""
        calc = Calculator()
        assert calc.multiply(5, 1) == 5


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers."""
        calc = Calculator()
        assert calc.divide(20, 5) == 4

    def test_divide_negative_numbers(self):
        """Test dividing two negative numbers (result positive)."""
        calc = Calculator()
        assert calc.divide(-18, -3) == 6

    def test_divide_positive_and_negative(self):
        """Test dividing positive by negative (result negative)."""
        calc = Calculator()
        assert calc.divide(21, -7) == -3

    def test_divide_with_float_result(self):
        """Test division that results in a float."""
        calc = Calculator()
        assert calc.divide(10, 3) == pytest.approx(3.3333333)

    def test_divide_float_numbers(self):
        """Test dividing floating point numbers."""
        calc = Calculator()
        assert calc.divide(7.5, 2.5) == pytest.approx(3.0)

    def test_divide_by_one(self):
        """Test dividing by 1 (identity)."""
        calc = Calculator()
        assert calc.divide(8, 1) == 8

    def test_divide_zero_by_number(self):
        """Test dividing zero by a non-zero number."""
        calc = Calculator()
        assert calc.divide(0, 5) == 0

    def test_divide_by_zero_raises_exception(self):
        """Test dividing by zero raises InvalidInputException."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(10, 0)  # 除数为0应抛出异常

    def test_divide_by_zero_negative(self):
        """Test dividing by negative zero (still invalid)."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(5, -0)  # 负零也视为0，应抛出异常
