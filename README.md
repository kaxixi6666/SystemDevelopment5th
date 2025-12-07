# Calculator

A Python calculator implementation with comprehensive test coverage and input validation.
This Calculator can handle the values up to 1000000 (Not implemented yet on purpose)

## Features

- **Basic Operations**: Addition, subtraction, multiplication, division

## Installation

1. Fork and Clone the repository:
```bash
git clone https://github.com/Yutaro-Kashiwa/SystemDevelopment5th.git
cd SystemDevelopment5th
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install pytest pytest-cov
```

## Usage

### Basic Usage

```python
from src.calculator.calculator import Calculator

# Create calculator instance
calc = Calculator()

# Basic operations
result = calc.add(5, 3)         # 8
result = calc.subtract(10, 3)   # 7
result = calc.multiply(4, 5)    # 20
result = calc.divide(10, 2)     # 5.0

# Advanced operations
result = calc.power(2, 3)       # 8
result = calc.square_root(16)   # 4.0
result = calc.modulo(10, 3)     # 1
```


## Testing

### Run All Tests

```bash
pytest tests/
```

### Run Tests with Verbose Output

```bash
pytest tests/test_calculator.py -v
```

### Generate Coverage Report

```bash
pytest --cov=src --cov-report=html tests/
```

View the HTML report:
```bash
open htmlcov/index.html
```

## Project Structure

```
SystemDevelopment5th/
├── src/
│   └── calculator/
│       ├── __init__.py
│       └── calculator.py          # Calculator implementation
├── tests/
│   ├── __init__.py
│   └── test_calculator.py         # Test suite (67 tests)
├── .gitignore
├── .coveragerc                    # Coverage configuration
├── setup.cfg                      # Project configuration
└── README.md
```

## API Documentation

### Calculator Class

#### Methods

**`add(a, b)`**
- Adds two numbers
- Raises `InvalidInputException` if inputs are outside valid range
- Returns: Sum of a and b

**`subtract(a, b)`**
- Subtracts b from a
- Raises `InvalidInputException` if inputs are outside valid range
- Returns: Difference of a and b

**`multiply(a, b)`**
- Multiplies two numbers
- Raises `InvalidInputException` if inputs are outside valid range
- Returns: Product of a and b

**`divide(a, b)`**
- Divides a by b
- Raises `InvalidInputException` if inputs are outside valid range
- Raises `ValueError` if b is zero
- Returns: Quotient of a and b

### Constants

- `MAX_VALUE = 1000000`: Maximum allowed input value
- `MIN_VALUE = -1000000`: Minimum allowed input value

### Exceptions

**`InvalidInputException`**
- Raised when input values are outside the valid range [-1000000, 1000000]
- Inherits from `Exception`


### Code Quality

The project follows Python best practices:
- Comprehensive docstrings for all methods
- Type hints where applicable
- Error handling for edge cases
- Input validation
- AAA test pattern

## Requirements

- Python 3.12+
- pytest 9.0+
- pytest-cov 7.0+

## License

This project is for educational purposes.

## Contributing

Contributions are welcome! Please ensure:
1. All tests pass
2. New features include tests
3. Tests follow AAA pattern
4. Code includes proper documentation

## Author

Yutaro Kashiwa


