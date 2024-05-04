n = int(input('Введите число: '))
nom = list(range(n + 1))
#nom[0] = 1
for i in range(1, n):
    nom[i + 1] = nom[i] + i
print(nom)
nom.pop(0)
print(nom)
nom2 = list(range(n + 1))
nom2[0] = 1
for i in range(1, n):
    nom2[i+1] = nom[i] + i
print(nom2)
nom2.pop(0)
print(nom2)
nom3 = list(range(n * n))
for i in range(n):
    a = nom[i]
    b = nom2[i]+1
    print(' '.join(map(str,nom3[a:b])))
