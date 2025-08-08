
x = list(map(int, input().split()))
n = len(x)

def leftchild(i):
    return 2*i+1

def rightchild(i):
    return 2*(i+1)

is_heap = True
for i in range(n//2):
    if leftchild(i) < n:
        if x[i] > x[leftchild(i)]:
            is_heap = False
            break
    if rightchild(i) < n:
        if x[i] > x[rightchild(i)]:
            is_heap = False
            break

if is_heap:
    print("YES")
else:
    print("NO")
