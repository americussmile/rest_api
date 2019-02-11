import sys

def toString(List):
    return ''.join(List)


# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.

# Driver program to test the above function
string = "ABCDE"
n = len(string)
a = list(string)
#permute(a, 0, n - 1,2)
result = []

# def permute2 (a,l,r,d, max_time=None):
#     if r+1-d < d:
#         print('n - d must be bigger or equal to d')
#     else:
#         for i in range(r+1-d):
#             if (i + d + l) in list(range(r+1)):
#                 count = 1
#                 a[i + l] , a[i + l + d] = a[i + l + d] , a[i + l]
#                 h = toString(a)
#                 print(h)
#                 result.append(h)
#                 if count < max_time:
#                     permute2(a, l+1, r, d, max_time)
#                     count += 1
#                     a[i + l], a[i + l + d] = a[i + l + d], a[i + l]
#

#permute2(a , 0 , n-1 , 1,1)
#print(len(result))

# a : string
# start: starting position
# r: len of string
# d: d in [d,l]
# max_time is the l in [d,l]
string = "ABCDE"
n = len(string)
a = list(string)
#permute(a, 0, n - 1,2)
result = []


def toString(List):
    return ''.join(List)


def permute3(a,start,r,d,max_time=1):
    global result
    for i in range(start,r+1):
        for j in range(start,r+1):
            if (abs(i-j)>= d) and (abs(i-j)<= r+1-d) :
                count = 1
                a[i], a[j] = a[j], a[i]
                if toString(a) not in result:
                    h = toString(a)
                    result.append(h)
                if count < max_time:
                    permute3(a,start+1, r,d, max_time -1)
                    a[i], a[j] = a[j], a[i]
                    original = a
    return  result
result = permute3(a,0,n-1,2,1)
for e in result:
    print(e)
print(len(result))