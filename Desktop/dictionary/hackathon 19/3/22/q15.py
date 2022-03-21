# You are given two non-empty linked lists representing two non-negative integers. 
# The most significant digit comes first and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]

# Example 2:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [8,0,7]

# Example 3:
# Input: l1 = [0], l2 = [0]
# Output: [0]

n=[7,2,4,3]
m=[5,6,4]
i=0
list1=[]
while i<len(n):
   j=0
   sum=0
   while j<len(m):
      sum=n[i]+m[j]
      list1.append(sum)
      j+=1
   i+=1
print(list1)