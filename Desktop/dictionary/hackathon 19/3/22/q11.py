"Let the games begin."
# Squid Game has become a blockbuster hit and the frontman is now finding it difficult to 
# accommodate all the participants in Squid Game 2.0. So, he decided that he will allow 
# only those participants who could solve the following problem.
# There are a total of N players who are competing in the Squid Game, numbered from 1 to 
# N. When the ith player gets eliminated from the game, Ai amount of money is added to 
# the prize pool. The game is played until N−1 players get eliminated, and the only player 
# left is declared as the winner. The winner gets all the money present in the prize pool.
# You are given an array A consisting of N elements, where Ai denotes the prize money 
# added to the prize pool when the ith player gets eliminated from the game. Find the 
# maximum prize that the winner can get, given that you can choose any player to be the 
# winner.
# Input Format
# The first line of input contains a single integer T, denoting the number of test cases.
# The description of T test cases follows.
# The first line of each test case contains an integer N, denoting the number of players.
# The second line of each test case contains N space-separated integers A1, A2,…, AN, 
# denoting the amount of money added to the prize pool when the ith (1≤i≤N) player dies.
# Output Format
# For each test case, output in a single line the maximum prize that the winner can get,
# given that you can choose any player to be the winner.
# Sample Input 1 
# 3
# 3 1 2

# 5
# 1 1 1 1 1

# 6
# 3 6 4 2 5 1
# Sample Output 1 
# 5
# 4
# 20

# Explanation
# Test Case 1:
# If we choose the first player to be the winner, he will win the game when the second 
# and third players die. Hence, the amount of money won by him will be 1+2=3.
# If we choose the second player to be the winner, he will win the game when the first 
# and third players die. Hence, the amount of money won by him will be 3+2=5.
# If we choose the third player to be the winner, he will win the game when the first 
# and second players die. Hence, the amount of money won by him will be 3+1=4.
# Therefore, we can clearly see that the maximum amount of money that can be won by 
# any player is 5.
