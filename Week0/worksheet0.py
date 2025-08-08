# num = int(input("Enter a number: "))

# for i in range(1,num+1):
#     print(i)

numbers_str = input("Enter integers separated by spaces: ")
numbers = [int(x) for x in numbers_str.split()]

print("\nYour list of numbers:", numbers)

odd_numbers = []
for num in numbers:
    if num % 2 == 1:
        odd_numbers.append(num)

print("\nOdd numbers:", odd_numbers)

largest_even = None
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
        if largest_even is None or num > largest_even:
            largest_even = num

if largest_even is not None:
    print("\nLargest even number:", largest_even)
else:
    print("\nNo even numbers found")

# Print even numbers in reverse order
print("\nEven numbers in reverse order:", end=" ")
if even_numbers:
    for i in range(max(even_numbers), min(even_numbers)-1, -1):
        if i in even_numbers and i % 2 == 0:
            print(i, end=" ")
print()