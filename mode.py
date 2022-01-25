import csv
f=open("SOCR-HeightWeight.csv")
file=csv.reader(f)
df=list(file)
df.pop(0)
weight=[]
for i in range(len(df)):
    num=df[i][2]
    weight.append(float(num))
import statistics
mode=statistics.mode(weight)
print(mode)