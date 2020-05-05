import sys

sys.stdout = open("constraints.txt", "w")
# define N
N=4
# define alpha
alpha = 0.5

# generate list of possible sequences
lst = []

strng = "#0" + str(N+2) + "b"


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
        recurse(a, list, depth-1)
        # And the left shifted number + 1 (0ba1)
        recurse(a+1, list, depth-1)

# Generate the list
recurse(0, lst, N-1)

# debug print
# print(lst)

weights = {}
with open("input.txt", "r") as f:
    for line in f:
        s = line.replace(" ", "")
        vals = s.split("=")
        weights[vals[0]] = float(vals[-1])

# Iterate through list
for i in lst:
    numbers = []
    total = 0
    print_list = []
    calc = []
    # Remove 0b
    i = i[2:]
    # Add up all the numbers
    for j in range(1, N):
        for k in range(j+1, N+1):
            if i[j-1] == i[k-1]:
                continue
            # print_list.append( "(" + str(j+k) + ")" + "x" + str(j)+str(k))
            weight = weights.get("w" + str(j) + str(k), 1)
            print_list.append("({})(x{})".format(weight, str(j)+str(k)))
            # print_list.append(str(j+k))
            calc.append((weight) * int(str(j) + str(k)))
            numbers.append(weight)
    if not len(numbers):
        continue

    if(sum(calc) < alpha*sum(numbers)):
        continue
    print("+".join(print_list), end='')
    print(" >= ",end='')
    print(str(alpha * sum(numbers)))
