import random
numbers = []
for i in range(20):
    numbers.append(random.randint(1, 100))
print("list of numbers:",numbers)
average = sum(numbers) / len(numbers)
print("Average of the list elements:",average);

smallest = min(numbers)
largest = max(numbers)
print("Smallest value:", smallest)
print("Largest value:", largest)


sorted_numbers = sorted(numbers)

second_smallest = sorted_numbers[1]
second_largest = sorted_numbers[-2]

print("Second smallest value:", second_smallest)
print("Second largest value:", second_largest)


even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1

print("Number of even numbers:", even_count)


