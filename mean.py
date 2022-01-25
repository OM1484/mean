import csv
f=open("SOCR-HeightWeight.csv")
file=csv.reader(f)
df=list(file)
df.pop(0)
weight=[]
for i in range(len(df)):
    num=df[i][2]
    weight.append(float(num))
sum=0
for i in weight:
    sum=sum+i
mean=sum/len(weight)
print(mean)
import statistics
mean=statistics.mean(weight)
print(mean)