import csv
from collections import Counter
with open('class.csv',newline = '')as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
newdata = []

for i in range(len(file_data)):
    n_num = file_data[i][2]
    newdata.append(float(n_num))
n = len(newdata)

if n%2 == 0:
    median1 = float(newdata[n//2])
    median2 = float(newdata[n//2-1])
    median = (median1+median2)/2
else:
    median2 = newdata[n//2]  

print('Median is '+ str(median))
    
total = 0
for x in newdata:
    total += x
mean = total/n

print('Mean is '+ str(mean))


        
print('Mode is '+ str(3*median-2*mean))     
            


            
        
        
        
        
        
         
    
    







   








 


         