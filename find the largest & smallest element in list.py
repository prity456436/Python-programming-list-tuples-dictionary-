# Program to find the largest and smallest element in a list
numbers = [10, 25, 5, 67, 134, 89, 12]
if len(numbers) == 0:
    print("The list is empty.")
else:
    largest = numbers[0]
    smallest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    print("Largest element:", largest)
    print("Smallest element:", smallest)
    