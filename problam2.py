str=input("Enter the string in the format [B7A1R3]:-> ")
#str="B7A1R3"
alphabets=[]
numbers=[]

for i in str:
    if i.isalpha():
        alphabets.append(i)
    else:
        numbers.append(i)

final=list=sorted(alphabets)+sorted(numbers)
output=''.join(final)                    
print(output)