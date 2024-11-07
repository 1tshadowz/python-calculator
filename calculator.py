class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return b - a

    def multiply(self, a, b):
        result = 0
        is_neg = False

        if b < 0:
            b = -b
            is_neg = True

        if a < 0:
            a = -a
            is_neg = True

        for i in range(b):
            result = self.add(result,a)

        if is_neg:
            result=-result

        return result

    def divide(self, a, b):
        # Handle division by zero
        if b == 0:
            return "Can't divide by zero"

        result = 0
        is_neg = (a < 0) ^ (b < 0)  # True if one is negative

        # Take absolute values for simplicity in looping
        a, b = abs(a), abs(b)

        # Main division loop
        while a >= b:
            a -= b
            result += 1

        # Apply negative sign if result is negative
        if is_neg:
            result = -result

        return result

    
    def modulo(self, a, b):
        # Handle division by zero
        if b == 0:
            return "Can't divide by zero"

        abs_a, abs_b = abs(a), abs(b)

        while abs_a >= abs_b:
            abs_a -= abs_b

        remainder = abs_a if a >= 0 else -abs_a

        return remainder


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(3, 7))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))