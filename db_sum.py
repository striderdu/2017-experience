import os
import re
import math

lat_a = []
ops_a = []
med_a = []
P99_a = []

fr = open('perf_lat.csv','w')
fr.write('IO mode,256B,1K,4K,16K,64K,256K\n')
#fr.write(str(lat)+',')
fr.close()
fr = open('perf_med.csv','w')
fr.write('IO mode,256B,1K,4K,16K,64K,256K\n')
#fr.write(str(lat)+',')
fr.close()
fr = open('perf_ops.csv','w')
fr.write('IO mode,256B,1K,4K,16K,64K,256K\n')
#fr.write(str(lat)+',')
fr.close()
fr = open('perf_p99.csv','w')
fr.write('IO mode,256B,1K,4K,16K,64K,256K\n')
#fr.write(str(lat)+',')
fr.close()
param = ['fillseq','fillrandom','readseq','readrandom','updaterandom','overwrite']
size = ['256','1024','4096','16384','65536','262144']

for i in range(len(param)):
    for j in range(len(size)):
        path = 'log/PerfLog-bluefs/'+ param[i] +'_'+size[j]+'.log'
        fp = open(path,'r')
        #print (path)
        content = fp.read()
        #print (content)
        #content='fillrandom   :    1988.861 micros/op 502 ops/sec;    0.1 MB/s fillrandom   :    2208.619 micros/op 452 ops/sec;    0.4 MB/s'
        latP = re.compile(r'\w+\.\w+(?=\smicros/op\b)')
#        latPfs = re.compile(r'(?<=\bfillseq\s\s\s\s\s\s:\s\s\s\s)\d+\.\d*|0\.\d*[1-9]\d*$')
#        latPrr = re.compile(r'(?<=\bfillseq\s\s\s\s\s\s:\s\s\s\s)\d+\.\d*|0\.\d*[1-9]\d*$')
        opsP = re.compile(r'(?<=\bop\s)\w+\b')
        medP = re.compile(r'(?<=\bMedian:\s)\d+\.\d*|0\.\d*[1-9]\d*$')
        P99P = re.compile(r'(?<=\bP99:\s)\d+\.\d*|0\.\d*[1-9]\d*$')

        lat = round(float(latP.findall(content)[0])/1000,2)
        #print (latP.findall(content))
        #print (opsP.findall(content)[0])
        ops = int(opsP.findall(content)[0])
        med = round(float(medP.findall(content)[0]),2)
        P99 = round(float(P99P.findall(content)[0]),2)
        lat_a.append(lat)
        ops_a.append(ops)
        med_a.append(med)
        P99_a.append(P99)

for i in range(0,35):
    if i%6==0:
        fr = open('perf_lat.csv','a+')
        fr.write(param[i/6]+',')
        fr.close()
    else i:
        fr
        fr.write(lat_a[i%6+i/6]+'\n')



#print (lat)
#print (ops)
#print (med)
print (lat_a)
print (ops_a)
print (med_a)
print (P99_a)
#fr = open('perf_med.csv','w')
#fr.write('IO mode,256B,1K,4K,16K,64K,256K\n')
#fr.write(str(lat)+',')
#fr.close()

#fr = open('perf_ops','w')
#fr.write('IO mode,256B,1K,4K,16K,64K,256K\n')
fp.close()
