import os
import re
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

lat_a = []
ops_a = []
med_a = []
p99_a = []

bench = ['fillseq','fillrandom','readseq','readrandom','updaterandom','overwrite']
size = ['256','1024','4096','16384','65536','262144']
system = ['PerfLog-ext4','PerfLog-btrfs','PerfLog-xfs','PerfLog-bluefs','PerfLog-rocksfs']
param = ['iops','lat','med','p99']
cparam = ['IOPS','LAT','MED','P99']

#生成.csv文件
def createCsv():
    for i in range(len(param)):
        for j in range(len(bench)):
            lat_a = []
            ops_a = []
            med_a = []
            p99_a = []
            for k in range(len(system)):
                for l in range(len(size)):
                    path = 'log/'+system[k]+'/'+ bench[j] +'_'+size[l]+'.log'
                    #print (path)
                    fp = open(path,'r')
                    #print (path)
                    content = fp.read()
                    #print (content)
                    latP = re.compile(r'\w+\.\w+(?=\smicros/op\b)')
                    opsP = re.compile(r'(?<=\bop\s)\w+\b')
                    medP = re.compile(r'(?<=\bMedian:\s)\d+\.\d*|0\.\d*[1-9]\d*$')
                    p99P = re.compile(r'(?<=\bP99:\s)\d+\.\d*|0\.\d*[1-9]\d*$')
                    if (i==0):
                        ops = int(opsP.findall(content)[0])
                        ops_a.append(ops)
                    elif (i==1):
                        lat = round(float(latP.findall(content)[0])/1000,2)
                        lat_a.append(lat)
                    elif (i==2):
                        med = round(1000000/float(medP.findall(content)[0]),2)
                        med_a.append(med)
                    elif (i==3):
                        p99 = round(1000000/float(p99P.findall(content)[0]),2)
                        p99_a.append(p99)
            filename = 'csv/'+bench[j]+' '+param[i]+'.csv'

            if i==0:
                for u in range(0,30):
                    if u%6==5:
                        fr = open(filename,'a+')
                        fr.write(str(ops_a[u])+'\n')
                        fr.close()
                    else:
                        fr = open(filename,'a+')
                        fr.write(str(ops_a[u])+',')
                        fr.close()
            elif i==1:
                for u in range(0,30):
                    if u%6==5:
                        fr = open(filename,'a+')
                        fr.write(str(lat_a[u])+'\n')
                        fr.close()
                    else:
                        fr = open(filename,'a+')
                        fr.write(str(lat_a[u])+',')
                        fr.close()
            elif i==2:
                for u in range(0,30):
                    if u%6==5:
                        fr = open(filename,'a+')
                        fr.write(str(med_a[u])+'\n')
                        fr.close()
                    else:
                        fr = open(filename,'a+')
                        fr.write(str(med_a[u])+',')
                        fr.close()
            elif i==3:
                for u in range(0,30):
                    if u%6==5:
                        fr = open(filename,'a+')
                        fr.write(str(p99_a[u])+'\n')
                        fr.close()
                    else:
                        fr = open(filename,'a+')
                        fr.write(str(p99_a[u])+',')
                        fr.close()

    fp.close()

#生成图表
def createImg():
    for l in range(len(bench)):
        for k in range(len(param)):
            path = 'csv/'+ bench[l] +' '+param[k]+'.csv'
            L=[[float (x) for x in y.split(',')] for y in open(path).read().rstrip().split('\n')[0:]]
            for i in range(1,5):
                for j in range(6):
                    L[i][j]=L[i][j]/L[0][j]
            for j in range(6):
                L[0][j]=1
            size = 6
            x = np.arange(6)
            a = L[0]
            b = L[1]
            c = L[2]
            d = L[3]
            e = L[4]
            labels = ['256B','1K','4K','16K','64K','256K'];
            #调整画布大小
            plt.figure(figsize=(13,8),dpi=80)
            matplotlib.rcParams['xtick.direction'] = 'in'
            matplotlib.rcParams['ytick.direction'] = 'in'
            total_width, n = 0.5, 5
            width = total_width / n
            x = x - (total_width - width) / 5

            plt.bar(x, a,  width=width, label='RocksDB-Ext4',ec='black', ls='-', lw=2,color='w',hatch='/')
            plt.bar(x + width+0.03,b, width=width, label='RocksDB-Btrfs',ec='black', ls='-', lw=2,color='w',hatch='-')
            plt.bar(x + 2 * width+0.06,c, width=width, label='RocksDB-XFS',ec='black', ls='-', lw=2, tick_label=labels,color='w',hatch='*')
            plt.bar(x + 3 * width+0.09, d, width=width, label='RocksDB-BlueFS',ec='black', ls='-', lw=2,color='w',hatch='X')
            plt.bar(x + 4 * width+0.12, e, width=width, label='RocksDB-RocksFS',ec='black', ls='-', lw=2,color='w',hatch='.')
            #plt.bar(range(len(data)), data, ec='black', ls='-', lw=2)
            plt.ylabel('Normalized '+cparam[k],fontsize=12)
            plt.xlabel('Value Size',fontsize=12)
            plt.grid(linewidth=0.5)
            plt.legend(frameon='false',loc=0,fancybox='false')
            plt.savefig('img/'+bench[l]+' '+param[k]+'.png')

createCsv()
createImg()
