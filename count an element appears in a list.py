list = input("enter list elements:").split()
x = input("enter elements to check occurence")
count=0
for i in list:
    if i==x:
        count+=1
print(f"{x} appears {count} times in the list.")
