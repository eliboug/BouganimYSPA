# define list to be bubble sorted
list = [5, 0, 9, 8, 7, 1, 4, 3, 2, 6]
numbers = list.copy()
# for loop to iterate through list, compare values, and swap
isSorted = False
swap_counter = 0
while not isSorted:
    status = True
    for k in range(len(list)-1): 
        if list[k] > list[k+1]:
            list[k], list[k+1] = list[k+1], list[k]
            status = False
            swap_counter += 1
    if status:
        isSorted = True
print(list)
print("It took  " + str(swap_counter) + " swaps to sort this list using bubble sort")

# COMB SORT

# Initial gap value
gap = len(numbers)
# Shrink factor
shrink = 1.3
sorted = False
# swap counter
swap2_counter = 0

while not sorted:
    # change gap value
    gap = int(gap / shrink)
    if gap <= 1:
        gap = 1
        sorted = True  # once gap is less than one, the list has been sorted

    # A single comb over the input list
    for i in range(len(numbers) - gap):
        if numbers[i] > numbers[i + gap]:
            # Swap values
            numbers[i], numbers[i + gap] = numbers[i + gap], numbers[i]
            sorted = False  
            swap2_counter += 1
            

print(numbers)
print(print("It took  " + str(swap2_counter) + " swaps to sort this list using the comb method"))


