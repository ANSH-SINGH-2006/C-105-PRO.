import math
import csv

with open('data.csv', newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]
# finding mean

def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)
    
    mean=total/n

    return mean


        
#squaring and getting the values

sq_list=[]

for number in data:
    a=int(number)-mean(data)
    a=a**2
    sq_list.append(a)

sum=0

for i in sq_list:
    sum=sum+i

result=sum/(len(data)-1)

stdDev= math.sqrt(result)

print(stdDev)