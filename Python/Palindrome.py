num = int(input("Enter the enter :"))
temp=num
sum = 0
while(temp>0):
    rem=temp%10
    sum = sum*10+rem
    temp=temp//10
print(sum)
if(sum==num):
    print("The number is palindrome")
else:
    print("The number is not palindrome")
