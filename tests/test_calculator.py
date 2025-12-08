"""
Test suite for the Calculator class.
"""

import pytest
from ..src.calculator.calculator import Calculator, InvalidInputException


# ======================================================================
# Fixtures
# ======================================================================

@pytest.fixture
def calc():
    """Provide a fresh Calculator instance for each test."""
    return Calculator()


# ======================================================================
# Basic arithmetic tests
# ======================================================================

class TestAddition:
    """Tests for the add method."""

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (5, 3, 8),
            (-5, -3, -8),
            (5, -3, 2),
            (-5, 3, -2),
            (5, 0, 5),
            (0, 5, 5),
        ],
    )
    def test_add_basic_cases(self, calc, a, b, expected):
        assert calc.add(a, b) == expected

    def test_add_result_above_max_raises(self, calc):
        """Inputs valid but result > MAX_INPUT must raise."""
        with pytest.raises(InvalidInputException):
            calc.add(600_000, 600_000)  # 1_200_000

    def test_add_result_below_min_raises(self, calc):
        """Inputs valid but result < MIN_INPUT must raise."""
        with pytest.raises(InvalidInputException):
            calc.add(-600_000, -600_000)  # -1_200_000


class TestSubtraction:
    """Tests for the subtract method."""

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (10, 4, 6),        # a > b
            (4, 10, -6),       # a < b
            (-5, -3, -2),      # two negatives
            (5, -3, 8),        # positive - negative
            (-5, 3, -8),       # negative - positive
            (7, 0, 7),         # subtracting zero
            (0, 7, -7),        # zero minus number
        ],
    )
    def test_subtract_basic_cases(self, calc, a, b, expected):
        assert calc.subtract(a, b) == expected

    def test_subtract_floats(self, calc):
        """Subtracting floating-point numbers."""
        assert calc.subtract(5.5, 2.1) == pytest.approx(3.4)

    def test_subtract_result_above_max_raises(self, calc):
        """Inputs valid but result > MAX_INPUT must raise."""
        with pytest.raises(InvalidInputException):
            # 600_000 - (-600_000) = 1_200_000
            calc.subtract(600_000, -600_000)

    def test_subtract_result_below_min_raises(self, calc):
        """Inputs valid but result < MIN_INPUT must raise."""
        with pytest.raises(InvalidInputException):
            # -600_000 - 600_000 = -1_200_000
            calc.subtract(-600_000, 600_000)


class TestMultiplication:
    """Tests for the multiply method."""

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (6, 7, 42),                # two positives
            (-4, -5, 20),              # two negatives → positive
            (3, -8, -24),              # positive * negative → negative
            (9, 0, 0),                 # number * 0
            (0, 9, 0),                 # 0 * number
            (5, 1, 5),                 # identity element
            (-500_000, 2, -1_000_000), # exact lower bound
            (333_333, 3, 999_999),     # near upper bound but valid
        ],
    )
    def test_multiply_basic_cases(self, calc, a, b, expected):
        assert calc.multiply(a, b) == expected

    def test_multiply_floats(self, calc):
        """Multiplying floating-point numbers."""
        assert calc.multiply(2.5, 4.0) == pytest.approx(10.0)

    def test_multiply_result_above_max_raises(self, calc):
        """Result > MAX_INPUT must raise."""
        with pytest.raises(InvalidInputException):
            calc.multiply(400_000, 3)  # 1_200_000

    def test_multiply_result_below_min_raises(self, calc):
        """Result < MIN_INPUT must raise."""
        with pytest.raises(InvalidInputException):
            calc.multiply(400_000, -4)  # -1_600_000


class TestDivision:
    """Tests for the divide method."""

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (20, 5, 4),        # two positives
            (-18, -3, 6),      # two negatives → positive
            (21, -7, -3),      # positive / negative → negative
            (8, 1, 8),         # identity
            (0, 5, 0),         # zero divided by non-zero
            (-10, 2, -5),      # / vs * mutation killer
            (10, -5, -2),
            (10, 5, 2),
        ],
    )
    def test_divide_basic_cases(self, calc, a, b, expected):
        assert calc.divide(a, b) == expected

    def test_divide_with_float_result(self, calc):
        """Division that results in a non-integer float."""
        assert calc.divide(10, 3) == pytest.approx(3.3333333)

    def test_divide_float_numbers(self, calc):
        """Dividing floating-point numbers."""
        assert calc.divide(7.5, 2.5) == pytest.approx(3.0)

    def test_divide_by_zero_raises_exception(self, calc):
        """Dividing by zero should raise InvalidInputException."""
        with pytest.raises(InvalidInputException):
            calc.divide(10, 0)

    def test_divide_by_zero_float_raises_exception(self, calc):
        """Dividing by 0.0 (float) should also be treated as zero."""
        with pytest.raises(InvalidInputException):
            calc.divide(5, 0.0)

    def test_divide_result_above_max_raises(self, calc):
        """Inputs valid but result > MAX_INPUT must raise."""
        with pytest.raises(InvalidInputException):
            calc.divide(10, 0.000001)  # 10_000_000.0

    def test_divide_result_below_min_raises(self, calc):
        """Inputs valid but result < MIN_INPUT must raise."""
        with pytest.raises(InvalidInputException):
            calc.divide(-10, 0.000001)  # -10_000_000.0


# ======================================================================
# Range validation tests (inputs & results)
# ======================================================================

class TestInputRangeValidation:
    """
    Input range validation: each operand must be within [-1_000_000, 1_000_000].
    """

    @pytest.mark.parametrize(
        "method, a, b",
        [
            ("add",       1_000_001,      5),
            ("subtract", -1_000_001,      5),
            ("multiply",  1_000_001,      1),
            ("divide",    1_000_001,      1),
            ("add",              0, 1_000_001),
            ("subtract",         0, -1_000_001),
            ("multiply",         1, 1_000_001),
            ("divide",           1, -1_000_001),
        ],
    )
    def test_operand_out_of_range_raises(self, calc, method, a, b):
        """Any operand outside the allowed range must raise."""
        with pytest.raises(InvalidInputException):
            getattr(calc, method)(a, b)

    @pytest.mark.parametrize(
        "method, a, b, expected",
        [
            ("add",  1_000_000, 0,  1_000_000),
            ("add", -1_000_000, 0, -1_000_000),
        ],
    )
    def test_operand_at_exact_bounds_is_allowed(self, calc, method, a, b, expected):
        """Values exactly at the bounds are valid inputs."""
        assert getattr(calc, method)(a, b) == expected

    def test_add_over_upper_bound_by_one_raises(self, calc):
        """Upper bound + 1 must raise (catches < → <= style mutations)."""
        with pytest.raises(InvalidInputException):
            calc.add(1_000_000, 1)  # 1_000_001


class TestResultRangeValidation:
    """
    Result range validation: operation results must be within [-1_000_000, 1_000_000].
    """

    def test_multiply_exact_result_bound_is_allowed(self, calc):
        """A result exactly equal to +1_000_000 is allowed."""
        assert calc.multiply(500_000, 2) == 1_000_000

    @pytest.mark.parametrize(
        "a, b",
        [
            (200_000, 6),   # 1_200_000
            (600_000, 2),   # 1_200_000
            (400_000, 3),   # 1_200_000
            (400_000, -4),  # -1_600_000
        ],
    )
    def test_multiply_result_out_of_range_raises(self, calc, a, b):
        """Any multiplication result outside the allowed range must raise."""
        with pytest.raises(InvalidInputException):
            calc.multiply(a, b)


# ======================================================================
# Type validation tests
# ======================================================================

class TestTypeValidation:
    """
    Type validation: non-numeric values (string, None, containers, etc.)
    must raise InvalidInputException.
    """

    @pytest.mark.parametrize(
        "method, a, b",
        [
            ("add",      "5",      3),
            ("add",       5,     "x"),
            ("multiply",  None,    4),
            ("divide",    [],      2),
            ("multiply", (1, 2),   3),
            ("divide",   {"a": 1}, 2),
        ],
    )
    def test_non_numeric_inputs_raise(self, calc, method, a, b):
        """Any non-numeric input must raise InvalidInputException."""
        with pytest.raises(InvalidInputException):
            getattr(calc, method)(a, b)


# ======================================================================
# Focused mutation-killer tests (operator / logic variants)
# ======================================================================

class TestMutationKillers:
    """Additional edge-case tests to kill tricky mutants."""

    def setup_method(self):
        self.calc = Calculator()

    # ---- Operator replacements ----
    def test_add_operator_kill(self):
        assert self.calc.add(7, 3) == 10
        assert self.calc.add(-4, -6) == -10

    def test_subtract_operator_kill(self):
        assert self.calc.subtract(9, 3) == 6
        assert self.calc.subtract(-8, -2) == -6

    def test_multiply_operator_kill(self):
        assert self.calc.multiply(5, 5) == 25
        assert self.calc.multiply(-3, 4) == -12

    def test_divide_operator_kill(self):
        assert self.calc.divide(12, 3) == 4
        assert self.calc.divide(-12, -3) == 4

    # ---- Division zero condition variants ----
    def test_divide_zero_condition_kill(self):
        with pytest.raises(InvalidInputException):
            self.calc.divide(5, 0)
        assert self.calc.divide(10, -5) == -2
        assert self.calc.divide(10, 5) == 2

    # ---- Extra type-mutation killers ----
    @pytest.mark.parametrize("method, a, b", [
        ("add", "x", 3),
        ("multiply", None, 3),
        ("divide", [], 2),
        ("subtract", {}, 2),
    ])
    def test_extra_non_numeric_inputs_raise(self, method, a, b):
        with pytest.raises(InvalidInputException):
            getattr(self.calc, method)(a, b)

    # ---- Floating-point precision edge ----
    def test_floating_point_precision_edge(self):
        """Ensure float precision related mutants are caught."""
        result = self.calc.divide(0.3, 0.1)
        assert pytest.approx(result, rel=1e-9) == 3.0


# ======================================================================
# Algebraic property tests (relations between operations)
# ======================================================================

class TestAlgebraicProperties:
    """Tests that relate different operations to each other."""

    def setup_method(self):
        self.calc = Calculator()

    @pytest.mark.parametrize("a, b", [
        (10, 3),
        (-7, 5),
        (0.5, -0.25),
    ])
    def test_add_and_subtract_inverse(self, a, b):
        """a - b should equal a + (-b)."""
        left = self.calc.subtract(a, b)
        right = self.calc.add(a, -b)
        assert pytest.approx(left) == right

    @pytest.mark.parametrize("a, b", [
        (10, 2),
        (-9, 3),
    ])
    def test_multiply_and_divide_inverse(self, a, b):
        """(a / b) * b should give back a."""
        result = self.calc.divide(a, b)
        back = self.calc.multiply(result, b)
        assert pytest.approx(back) == pytest.approx(a)

    def test_double_negation(self):
        """Subtracting a negative should be same as adding a positive."""
        assert self.calc.subtract(5, -3) == self.calc.add(5, 3)
