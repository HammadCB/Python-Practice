'''

sum(1) = 1
sum(2) = 1+2
sum(3) = 1+2+3
sum(n) = 1+2+3+4...+n

sum(n) = 1+2+3+4.....+ n-1 + n
sum(n) = sum(n-1) + n
'''

#Recursion is also kind of Loop 
#If we look closely, we can see that sum(n) is defined in terms of sum(n-1).

def sum(n):
    if n == 1:
        return 1
    else:
        return sum(n-1) + n
    
print(sum(8))