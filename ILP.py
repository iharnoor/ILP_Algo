import sys
# define N
N = 4
# define alpha
alpha = 0.5

sys.stdout = open("constraints.txt", "w")
# generate list of possible sequences
lst = []

strng = "#0" + str(N + 2) + "b"

# define a recursive function to generate a set of elements of the correct form
def recurse(start, list, depth):
    # If at the bottom of the tree
    if depth == 1:
        # Append binary representations of the number to the array

        list.append(format((start << 1), strng))
        list.append(format((start << 1) + 1, strng))
    else:
        # Left shift the number by 1
        a = start << 1

        # Operate on the left shifted number (0ba0)
        recurse(a, list, depth - 1)
        # And the left shifted number + 1 (0ba1)
        recurse(a + 1, list, depth - 1)


# Generate the list
recurse(0, lst, N - 1)


# Iterate through list
for i in lst:
    numbers = []
    total = 0
    print_list = []
    # Remove 0b
    i = i[2:]
    # Add up all the numbers
    for j in range(1, N):
        for k in range(j + 1, N + 1):
            if i[j - 1] == i[k - 1]:
                continue
            print_list.append("(" + str(j + k) + ")" + "(x" + str(j) + str(k) + ")")
            numbers.append(str(j + k)) # weight of each edge
            # get input for each weight
    if not len(numbers):
        continue
    print("+".join(print_list), end="")
    print(" >= ", end='')
    #     print("(" + "+".join(numbers) + ")")
    sum = 0
    for i in numbers: # Sum of weights
        sum += int(i)
    sum = sum * alpha

    print("" + str(sum))
#     print(")")


# get input for the weights
# N = 10
"""
w12 = 3.5
w13 = 3.6
...
w910 = 7.3

what's the format 
"""


