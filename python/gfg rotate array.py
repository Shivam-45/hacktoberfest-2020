# Input:
# 2
# 5 2
# 1 2 3 4 5 
# 10 3
# 2 4 6 8 10 12 14 16 18 20

# Output:
# 3 4 5 1 2
# 8 10 12 14 16 18 20 2 4 6

a = int(input())
for _ in range(a) :
    arr1 = []
    n,m = list(map (int, input().split())) [:2]
    arr = list(map(int,input().split())) [:n]
    for i in range(m,n):
        arr1.append(arr[i])
    for j in range(m) :
        arr1.append(arr[j])
    for k in range(n):
        print (arr1[k],end = ' ')
    print () 