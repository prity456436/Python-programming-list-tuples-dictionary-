list=[2,3,4,6,7,9,43,24]
even=0
odd=0
for i in list:
    if i%2==0:
        even+=i
    else:
        odd+=i
print("sum of even numbers: ",even)
print("sum of odd numbers: ",odd)