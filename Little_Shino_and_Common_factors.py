"""
Little Shino and Common factors

Little Shino loves maths. Today her teacher gave her two integers. 
Shino is now wondering how many integers can divide both the numbers. 
She is busy with her assignments. Help her to solve the problem.

Input:
First line of the input file contains two integers, a and b.

Output:
Print the number of common factors of a and b.
"""


arr = list(map(int, input().split()))

a = min(arr)
b = max(arr)
factor_set = set()

for i in range(1,int(a**.5)+1):
    if(a%i==0):
        if(b%i==0):
            factor_set.add(i)
        if(b%(a/i)==0):
            factor_set.add(a//i)
    
print(len(factor_set))