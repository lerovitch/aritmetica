from collections import deque
import copy

def generador(n):
    maxim = (n / 2) + 1
    if maxim == n: maxim = maxim - 1
    for i in range(1,maxim + 1):
        yield i

def suma_sequencia(sequencia):
    total = 0
    for i in sequencia:
        total = total + i
    return total

n = 1000 

resultats = {}
bad_result = []
for i in range(1,n):
    sequencia = deque([])
    ok = 0
    for j in generador(i):
        sequencia.append(j)
        if suma_sequencia(sequencia) == i: 
            ok = ok + 1
            resultats["%d %d" % (i, ok)] = copy.copy(sequencia)
        while suma_sequencia(sequencia) > i:
            sequencia.popleft()
            if suma_sequencia(sequencia) == i: 
                ok = ok + 1
                resultats["%d %d" % (i, ok)] = copy.copy(sequencia)
    while len(sequencia) > 1:
        if suma_sequencia(sequencia) == i:
            ok = ok + 1
            resultats["%d %d" % (i, ok)] = copy.copy(sequencia)
        sequencia.popleft()
    if ok == 0:
        bad_result.append(i)
          


for resultat in sorted(resultats.keys()):
    print '%s %s' % (resultat, resultats[resultat] )

print bad_result
