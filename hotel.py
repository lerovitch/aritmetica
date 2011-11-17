
n = 100 
hotel  = dict([(i, 0) for i in range(0,n)])


for i in range(1,n):
    for j in range(0,n,i):
        if hotel[j] == 1:
            print i,' pasa i tanca porta',j
            hotel[j] = 0
        else:
            print i,'passa i obre porta',j
            hotel[j] = 1

for i in range(1,n):
    if hotel[i] == 1:
        print i

resultat = [i for i in range(1,n) if hotel[i] == 1]
print resultat


terme = 0
n = 0
termes = []
while terme < 1000:
    terme = terme + (1 + 2*n)
    n = n + 1
    termes.append(terme)

print termes
