# src/calculator/calculator.py

class InvalidInputException(Exception):
    """Raised when an input value or computed result is invalid."""
    pass


class Calculator:
    """Simple calculator with strict input and result range validation."""

    # Allowed range for both inputs and results
    MIN_INPUT = -1_000_000
    MAX_INPUT = 1_000_000

    def _validate_input(self, *args):
        for num in args:
            # Reject non-numeric types (exclude bool since it's a subclass of int)
            if not isinstance(num, (int, float)) or isinstance(num, bool):
                raise InvalidInputException(f"Invalid input type: {type(num).__name__}")
            # Reject out-of-range values
            if num > self.MAX_INPUT or num < self.MIN_INPUT:
                raise InvalidInputException(f"Input {num} out of range [{self.MIN_INPUT}, {self.MAX_INPUT}]")

    # def _validate_input(self, *values):
    #     """
    #     Validate that all input values are numeric and inside the allowed range.
    #
    #     Raises InvalidInputException if a value is not an int/float or
    #     falls outside [MIN_INPUT, MAX_INPUT].
    #     """
    #     for value in values:
    #         if not isinstance(value, (int, float)):
    #             raise InvalidInputException(
    #                 f"Input must be int or float. Got: {type(value).__name__}"
    #             )
    #         if value < self.MIN_INPUT or value > self.MAX_INPUT:
    #             raise InvalidInputException(
    #                 f"Input value must be between {self.MIN_INPUT} and "
    #                 f"{self.MAX_INPUT}. Got: {value}"
    #             )

    def _validate_result(self, result, operation: str):
        """
        Validate that the calculated result is inside the allowed range.

        Raises InvalidInputException if result is outside [MIN_INPUT, MAX_INPUT].
        """
        if result < self.MIN_INPUT or result > self.MAX_INPUT:
            raise InvalidInputException(
                f"{operation} result must be between {self.MIN_INPUT} and "
                f"{self.MAX_INPUT}. Got: {result}"
            )

    def add(self, a, b):
        """Return a + b with input and result validation."""
        self._validate_input(a, b)
        result = a + b
        self._validate_result(result, "Addition")
        return result

    def subtract(self, a, b):
        """Return a - b with input and result validation."""
        self._validate_input(a, b)
        result = a - b
        self._validate_result(result, "Subtraction")
        return result

    def multiply(self, a, b):
        """Return a * b with input and result validation."""
        self._validate_input(a, b)
        result = a * b
        self._validate_result(result, "Multiplication")
        return result

    def divide(self, a, b):
        """
        Divide a by b.

        Raises InvalidInputException when:
        - b is zero,
        - inputs are not numeric or out of range, or
        - the result is outside the allowed result range.
        """
        self._validate_input(a, b)
        if b == 0:
            raise InvalidInputException("Division by zero is not allowed.")
        result = a / b
        self._validate_result(result, "Division")
        return result
