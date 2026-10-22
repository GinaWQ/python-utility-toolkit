"""Базовий модуль калькулятора.

Містить чотири арифметичні операції: додавання, віднімання,
множення та ділення.
"""


def add(a: float, b: float) -> float:
    """Повертає суму a + b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Повертає різницю a - b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Повертає добуток a * b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Повертає частку a / b.

    Викликає ValueError, якщо b дорівнює нулю.
    """
    if b == 0:
        raise ValueError("Ділення на нуль неможливе")
    return a / b


if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("5 - 1 =", subtract(5, 1))
    print("4 * 6 =", multiply(4, 6))
    print("10 / 4 =", divide(10, 4))
