import csv
from statistics import median
f=open("SOCR-HeightWeight.csv")
file=csv.reader(f)
df=list(file)
df.pop(0)
weight=[]
for i in range(len(df)):
    num=df[i][2]
    weight.append(float(num))
weight.sort()
n=len(weight)
if(n%2==0):
    m1=float (weight[n//2])
    m2=float(weight[n//2+1])
    median=(m1+m2)/2
else:
    median=float(weight[n//2])
print(median)
import statistics
median=statistics.median(weight)
print(median)