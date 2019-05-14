numbers=[]
for x in range(1,21):
    numbers.append(x)
for x in numbers:
    if x % 3 == 0 and x % 5 == 0:
        numbers.insert(numbers.index(x), "FizzBuzz")
        numbers.pop(numbers.index(x))
    elif x % 3 == 0:
        numbers.insert(numbers.index(x), "Fizz")
        numbers.pop(numbers.index(x))
    elif x % 5 == 0:
        numbers.insert(numbers.index(x), "Buzz")
        numbers.pop(numbers.index(x))
print(numbers)