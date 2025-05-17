from enum import Enum

class MathOperation(Enum):
    ADDITION = ("+", "add", "Adds two numbers")
    SUBTRACTION = ("-", "subtract", "Subtracts second number from first")
    MULTIPLICATION = ("*", "multiply", "Multiplies two numbers")
    DIVISION = ("/", "divide", "Divides first number by second")
    EXPONENTIATION = ("**", "power", "Raises first number to the power of second")
    MODULUS = ("%", "modulus", "Remainder of division of first number by second")
    FLOOR_DIVISION = ("//", "floor_divide", "Divides and floors the result to nearest lower integer")
    SQUARE_ROOT = ("√", "sqrt", "Calculates the square root")
    LOGARITHM = ("log", "log", "Calculates the logarithm")
    SINE = ("sin", "sine", "Calculates the sine of an angle")
    COSINE = ("cos", "cosine", "Calculates the cosine of an angle")
    TANGENT = ("tan", "tangent", "Calculates the tangent of an angle")
    FACTORIAL = ("!", "factorial", "Calculates the factorial")
    ABSOLUTE = ("abs", "absolute", "Calculates the absolute value")
    CEILING = ("ceil", "ceiling", "Rounds number up to nearest integer")

    def __init__(self, symbol: str, function_name: str, description: str = "Normal Description"):
        """
        Here i only use description argument name so that if not given
        wheen making  obj it will be used
        """
        self.symbol = symbol
        self.function_name = function_name
        self.description = description


all_obj = MathOperation

for obj in all_obj:
    print(obj, obj.symbol, obj.function_name)