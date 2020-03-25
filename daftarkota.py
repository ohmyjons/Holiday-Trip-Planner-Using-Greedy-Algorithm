# -*- coding: utf-8 -*-
def daftarkota(name):
    listkota = []
    count = 0
    for i in name:
        listkota.append('-')
        listkota.append(i)
        count+=1

        if count%4 == 0:
            listkota.append('\n')

    listkota = ' '.join(listkota)
    print(listkota)

