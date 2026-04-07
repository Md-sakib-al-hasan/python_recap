# Problem 1
# Write a function introduce(name, age) that prints:
# My name is <name> and I am <age> years old.
# Call it using positional arguments.
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce("Rahim", 28)

# Problem 2
# Write a Python generator function called batch_generator. 
# It should take a list of numbers (representing data samples) and a batch_size. 
# The generator should yield one batch at a time as a list.
def batch_generator(nums, batch_size):
    for i in range(0, len(nums), batch_size):
        yield nums[i:i+batch_size]

data = [1, 2, 3, 4, 5, 6, 7, 8]
for batch in batch_generator(data, 3):
    print(batch)

# Problem 3
# Given a list [1,2,3,4], use map() and lambda to create a new list with squares of each number.
squares = list(map(lambda x: x*x, [1, 2, 3, 4]))
print(squares)

# Problem 4
# Write a function power(base, exponent) that returns the result of base raised to exponent. 
# If the exponent is not given, it should calculate the square.
def power(base, exponent=2):
    return base ** exponent

print(power(5))
print(power(5, 3))

# Problem 5 ( Conceptual Session )
# Given a list [1,2,3,4,5,6], use filter() to select even numbers and map() with lambda to square them.
newlist = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x*x, filter(lambda x: x % 2 == 0, newlist)))
print(result)
