nums=eval(input("Input-> "))
target=int(input("Target-> "))
output=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target and len(output)==0:
            output.append(i)
            output.append(j)

print("Output-> ",output) 
           