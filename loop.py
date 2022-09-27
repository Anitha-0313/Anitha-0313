# use while loop that iterate 100 times by adding each number
# time must be noted here and calculate difference
import time

print(time.asctime())
b=time.time()
n = 100
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1
    print(sum)
print(time.asctime())


c=time.time()

print("The Difference between two time",c-b)

