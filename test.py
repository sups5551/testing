import csv
with open ('data.csv',newline='')as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
newdata=[]

for i in range(len(filedata)):
    numb=filedata[i][1]
    newdata.append(float(numb))

n=len(newdata)
total=0

for x in newdata:
    total=total+x
mean=total/n

print('mean or avrange='+str(mean))