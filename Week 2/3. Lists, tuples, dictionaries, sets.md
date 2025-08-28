# 🔹 1. **Lists**

- Ordered, changeable (mutable), allow duplicates.
- Use `[]`.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])        # apple (indexing starts at 0)
fruits[1] = "grape"     # change item
print(fruits)           # ['apple', 'grape', 'cherry']
fruits.append("mango")  # add item
print(fruits)           # ['apple', 'grape', 'cherry', 'mango']

```

👉 Think of a list like a shopping list: order matters, you can add/change items.

---

# 🔹 2. **Tuples**

- Ordered, **unchangeable** (immutable), allow duplicates.
- Use `()`.

```python
colors = ("red", "green", "blue")
print(colors[0])    # red
# colors[1] = "yellow"  ❌ Error (cannot change)

```

👉 Use tuples when you want data to stay fixed (like coordinates `(x, y)`).

---

# 🔹 3. **Dictionaries**

- Store data as **key → value** pairs.
- Unordered (in Python 3.7+, they keep insertion order).
- Use `{}`.

```python
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

print(student["name"])   # Alice
student["age"] = 21      # update value
student["school"] = "DYB"  # add new key
print(student)
# {'name': 'Alice', 'age': 21, 'grade': 'A', 'school': 'DYB'}

```

👉 Think of a dictionary like a real dictionary: **word = definition**.

---

# 🔹 4. **Sets**

- Unordered, **no duplicates**, mutable.
- Use `{}` but not for empty set (`set()` instead).

```python
numbers = {1, 2, 3, 3, 2}
print(numbers)   # {1, 2, 3} (duplicates removed)

numbers.add(4)
print(numbers)   # {1, 2, 3, 4}

numbers.remove(2)
print(numbers)   # {1, 3, 4}

```

👉 Sets are great for removing duplicates or doing math operations (union, intersection).

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # union {1, 2, 3, 4, 5}
print(a & b)   # intersection {3}

```

---

# 🔹 Quick Comparison

| Structure | Ordered? | Changeable? | Allows Duplicates? | Example Use |
| --- | --- | --- | --- | --- |
| **List** | ✅ Yes | ✅ Yes | ✅ Yes | Shopping list |
| **Tuple** | ✅ Yes | ❌ No | ✅ Yes | Coordinates `(x, y)` |
| **Dictionary** | ✅ (3.7+) | ✅ Yes | ✅ Keys unique | Student info (`name → Alice`) |
| **Set** | ❌ No | ✅ Yes | ❌ No | Unique IDs |

---

# 🔹 Practice 📝

Try to:

1. Make a **list** of your 3 favorite foods.
2. Make a **tuple** with your birth year and birth month.
3. Make a **dictionary** with keys: `"name"`, `"age"`, `"hobby"`.
4. Make a **set** with some numbers (include duplicates) and see how Python removes them.

---
