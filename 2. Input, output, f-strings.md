# 🔹 1. Output in Python

You use `print()` to display something.

```python
print("Hello, World!")

```

You can print variables too:

```python
name = "Roy"
age = 25
print(name)
print(age)

```

---

# 🔹 2. Input in Python

`input()` lets the user type something in.

```python
user_name = input("What is your name? ")
print("Hello, " + user_name)

```

⚡ Note: `input()` always gives you a **string** (even if you type a number).

If you want a number, you need to convert:

```python
age = int(input("Enter your age: "))   # convert to int
height = float(input("Enter your height: "))  # convert to float

print("Next year you will be", age + 1)

```

---

# 🔹 3. f-Strings (formatted strings)

Instead of writing:

```python
name = "Roy"
age = 25
print("My name is " + name + " and I am " + str(age) + " years old.")

```

You can use **f-strings** (cleaner and faster):

```python
print(f"My name is {name} and I am {age} years old.")

```

### More examples:

```python
pi = 3.14159
print(f"Pi is approximately {pi:.2f}")   # 2 decimal places

```

```python
x = 5
y = 10
print(f"{x} + {y} = {x+y}")   # f-strings can do calculations too!

```

---

# 🔹 4. Practice 📝

Try this:

1. Ask the user for their **name** and **favorite number**.
2. Convert the number to an integer.
3. Print out a message using an **f-string**, like:
    
    ```
    Hello Roy! Your favorite number is 7, and double of it is 14.
    
    ```
