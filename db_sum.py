import re
import linecache

fp=open('fillrandom_256.log','r')
#print(1)
#a=linecache.getline(r'C:\py\fillrandom_256.log',14)
content=fp.read()
#print content
#s=re.findall(r'^Median:\s(.\s)',content,re.M)
#print(s)

#import re

#a='Min: 6027.0000  Median: 32102.9845  Max: 175218.0000'

#regex = re.compile(r'(?<=\bMedian:\s)\w+\b') 30102
lat = re.compile(r'(?<=\bfillrandom\s\s\s:\s\s\s\s)\d+\.\d*|0\.\d*[1-9]\d*$')
ops = re.compile(r'(?<=\bop\s)\w+\b')
med = re.compile(r'(?<=\bMedian:\s)\d+\.\d*|0\.\d*[1-9]\d*$')
P99 = re.compile(r'(?<=\bP99:\s)\d+\.\d*|0\.\d*[1-9]\d*$')

print (lat.findall(content))
print (ops.findall(content))
print (med.findall(content))
print (P99.findall(content))
