def toString(List):
    return ''.join(List)


# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
result =[]
def permute(a, l, r):
    if l == r:
        h=toString(a)
        result.append(h)
        print(h)
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            intermediate = a
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack
            original = a

# Driver program to test the above function
string = "123456789"
n = len(string)
a = list(string)
permute(a, 0, n - 1)
print(len(result))