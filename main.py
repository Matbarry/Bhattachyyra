
from operator import itemgetter
import numpy as np
N = 64
Kp = 32
dsnr_db = 2
bhattacharya = np.zeros(N, dtype=float)
snr = np.power(10, dsnr_db / 10)
print('dsnr_db = {}'.format(dsnr_db))
print("snr = {}".format(snr))
bhattacharya[0] = np.exp(-snr)
print("primeiro Bhattacharyya = {}".format(bhattacharya[0]))
k = 0
canal = []
for level in range(1, int(np.log2(N)) + 1):
    B = np.power(2, level)
    print(level)
    for j in range(int(B / 2)):
        T = bhattacharya[j]
        posicoes = {}
        posicoes[k] = T
        print(posicoes)
        k = k+1
        canal.append(T)
        bhattacharya[j] = 2 * T - np.power(T, 2)#up
        bhattacharya[int(B / 2 + j)] = np.power(T, 2)#low
print("Bhattacharyya = {}".format(bhattacharya))
#print(len(bhattacharya))  
#congelados
mask = [[i, 0.0, 1] for i in range(N)]
reliability = bhattacharya
for i in range(N):
    mask[i][1] = reliability[i]
mask = sorted(mask, key=itemgetter(1), reverse=True)
for i in range(N-Kp):
    mask[i][2] = 0
mask = sorted(mask, key=itemgetter(0))   
print("posições: {}".format(np.array([i[2] for i in mask])))
