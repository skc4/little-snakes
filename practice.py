'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3

'''

def numIslands(matrix):
    result = 0  
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '1':
                dfs(i, j, matrix)
                result += 1
    return result

def dfs(i, j, matrix):
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] != '1':
        return
    matrix[i][j] = '*'
    dfs(i+1, j, matrix)
    dfs(i-1, j, matrix)
    dfs(i, j+1, matrix)
    dfs(i, j-1, matrix)

island_map = [['1','1','0','0','0'],
              ['1','1','0','0','0'],
              ['0','0','1','0','0'],
              ['0','0','0','1','1']]

print(numIslands(island_map))

############################################################################################################

'''
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

    S will have length in range [1, 500].
    S will consist of lowercase letters ('a' to 'z') only.

'''

def partitionLabels(S):
    """
    :type S: str
    :rtype: List[int]
    """
    dic = {}
    for i, char in enumerate(S):
        dic[char] = i
    res = []
    currLen = 0
    hi = 0
    for i, char in enumerate(S):
        hi = max(hi, dic[char])
        if i == hi:
            res.append(i - currLen + 1)
            currLen = i+1
    return res

S = "ababcbacadefegdehijhklij"
print(partitionLabels(S))

############################################################################################################

'''
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

    If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
    Otherwise, it becomes vacant.

(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

 

Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]

'''

def prisonAfterNDays(cells, N):
    def nextday(cells):
        newcells =[]
        newcells.append(0)
        for i in range(1, len(cells)-1):
            if cells[i - 1] == cells[i + 1]:
                newcells.append(1)
            else:
                newcells.append(0)
        newcells.append(0)
        return newcells

    seen = {}
    while N > 0:
        c = tuple(cells)
        if c in seen:
            N %= seen[c] - N
        seen[c] = N

        if N >= 1:
            N -= 1
            cells = nextday(cells)

    return list(cells)

cells = [0,1,0,1,1,0,0,1]
N = 7

# cells = [1,0,0,1,0,0,1,0]
# N = 1000000000
print(prisonAfterNDays(cells, N))

############################################################################################################
'''
Description:
Implement a function to return product suggestions using products from a product repository after each character is typed by the customer in the search bar.
If there are more than THREE acceptable products, return the product name that is first in the alphabetical order.
Only return product suggestions after the customer has entered two characters.
Product suggestions must start with the characters already typed.
Both the repository and the customer query should be compared in a CASE-INSENSITIVE way.

Input:
The input to the method/function consist of three arguments:

    numProducts, an integer representing the number of various products in Amazon's product repository;
    repository, a list of unique strings representing the various products in Amazon's product repository;
    customerQuery, a string representing the full search query of the customer.

Output:
Return a list of a list of strings, where each list represents the product suggestions made by the system as the customer types each character of the customerQuery. Assume the customer types characters in order without deleting/removing any characters.

Example:
Input:
numProducts = 5
repository = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
customerQuery = "mouse"

Output:
[["mobile", "moneypot", "monitor"],
["mouse", "mousepad"],
["mouse", "mousepad"],
["mouse", "mousepad"]]

Explanation:
The chain of words that will generate in the search box will be mo, mou, mous and mouse, and each
line from output shows the suggestions of "mo", "mou", "mous" and "mouse", respectively in each line.
For the suggestions that are generated for "mo", the matches that will be generated are:
["mobile", "mouse", "moneypot", "monitor", "mousepad"]. Alphabetically, they will be reordered to
["mobile", "moneypot", "monitor", "mouse", "mousepad"]. Thus, the suggestions are ["mobile", "moneypot", "monitor"]
'''

def productSuggestion(numProducts, repository, customQuery):
    sortedRepository = sorted(repository)
    output, bucket = [], []
    for i in range(2, len(customQuery)+1):
        for j in range(numProducts):
            if customQuery[0:i] == sortedRepository[j][0:i]:
                bucket.append(sortedRepository[j])
        if len(bucket) > 3:
            output.append(bucket[0:3])
        else:
            output.append(bucket)
        bucket = []
    return output


repo = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
query = "mouse"
print(productSuggestion(5, repo, query))

############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################