# write a program to display the word that are repeated more than or equal to N time in the text
# input 
 # first input is a string 
 # secound input is integer (count  repesetion)  
 # value of number of time word occur in text
 
str1=input("Enter the string:-> ")
n=int (input("Enter a Count:-> "))
str1=str1.split()
counts=dict()
for word in str1:
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1
word_list=[]
for key in counts:
    if counts[key]>=n:
        word_list.append(key)

if len(word_list)>0:
    print(word_list)
else:
    print("Na")                       
   