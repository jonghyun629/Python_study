# Week 1 — Python Basics Practice
# Fill in the functions below. Run this file to see simple tests.
# Tips:
# - Use f-strings for formatting.
# - Prefer clear variable names.
# - Run `python week01_basics_practice.py` to test locally.

def greet(name: str) -> str:
    """Return 'Hello, <name>!'"""
    # TODO: implement
    return f"Hello, {name}!"


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    # TODO: implement
    return a + b


def is_even(n: int) -> bool:
    """Return True if n is even, else False."""
    # TODO: implement
    return n % 2 == 0


def average(nums: list[float]) -> float:
    """Return the arithmetic mean of nums. If empty, return 0.0."""
    # TODO: implement
    if not nums:
        return 0.0
    return sum(nums) / len(nums)


def fizzbuzz(n: int) -> list[str]:
    """Return a list from 1..n with Fizz/Buzz/FizzBuzz rules."""
    # TODO: implement
    out = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))
    return out


def count_vowels(s: str) -> int:
    """Count vowels (a, e, i, o, u) in s, case-insensitive."""
    # TODO: implement
    vowels = set("aeiou")
    return sum(1 for ch in s.lower() if ch in vowels)


def factorial(n: int) -> int:
    """Return n! for n >= 0. Use an iterative solution."""
    # TODO: implement
    if n < 0:
        raise ValueError("n must be >= 0")
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans


def reverse_words(s: str) -> str:
    """Reverse word order in a sentence. 'hello world' -> 'world hello'"""
    # TODO: implement
    return " ".join(reversed(s.split()))


def c_to_f(c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    # TODO: implement
    return c * 9 / 5 + 32


def f_to_c(f: float) -> float:
    """Convert Fahrenheit to Celsius."""
    # TODO: implement
    return (f - 32) * 5 / 9


# --------------------
# Simple Tests
# --------------------
def _approx(a: float, b: float, tol: float = 1e-9) -> bool:
    return abs(a - b) <= tol


if __name__ == "__main__":
    print("Running basic tests...\n")
    assert greet("Roy") == "Hello, Roy!"
    assert add(2, 3) == 5
    assert is_even(4) is True and is_even(5) is False
    assert _approx(average([1, 2, 3, 4]), 2.5)
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert count_vowels("Alphabet") == 3
    assert factorial(5) == 120
    assert reverse_words("I love Python") == "Python love I"
    assert _approx(c_to_f(0), 32)
    assert _approx(f_to_c(212), 100)

    print("All tests passed! ✨")
