n = int(input())
a = list(map(int, input().split()))

max_sum = 0
for i in range(n):
    s = a[i] + a[i-1 if i > 0 else n-1] + a[i+1 if i < n-1 else 0]
    max_sum = max(max_sum, s)

print(max_sum)


n = int(input("Введите количество элементов первого множества: "))
set1 = set(map(int, input("Введите элементы первого множества: ").split()))
m = int(input("Введите количество элементов второго множества: "))
set2 = set(map(int, input("Введите элементы второго множества: ").split()))

common = sorted(list(set1 & set2))

print("Элементы, которые встречаются в обоих множествах: ", end="")
for num in common:
    print(num, end=" ")
