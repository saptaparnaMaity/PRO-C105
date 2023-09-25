import csv
import math

with open("data.csv") as f:
    reader= csv.reader(f)
    file_data=list(reader)
 
data = file_data[0]
print(file_data)

def mean(data):
  sum = 0
  for i in data:
    sum = sum + int(i)
  count = len(data)
  mean = sum / count
  return mean  

squredNum = []
for num in data:
  a = int(num) - mean(data)
  a = a ** 2
  squredNum.append(a)

total = 0 
for squared in squredNum:
  total = total + squared

count = len(squredNum)-1 
result = total / count  
sd = math.sqrt(result)
print('Sd',sd)