# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a 
# list of favorite restaurants represented by strings.
# You need to help them find out their common interest with the least list index sum. 
# If there is a choice tie between answers, output all of them with no order requirement. 
# You could assume there always exists an answer.

# Example 1:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], 
# list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".

# Example 2:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], 
# list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).



list1 = ["Shogun","Tapioca Express","Burger King","KFC"], 
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

i=0
list3=[]
while i<len(list1):
   j=0
   while j<len(list2):
      if list1[i] in list2[j]:
         list3.append(list1[i])
      j+=1
   i+=1
print(list3)
# print(list3)
# list3=[]
# for x in list1:
#    for y in list2:
#       if x==y:
#          list3.append(x)
# print(list3)
