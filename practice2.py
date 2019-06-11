"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


https://leetcode.com/problems/palindrome-number/
------------------------------------------------------------------------------------------------------------
1. Write a function that takes in an integer and determines if it is a palindrome.
2. - Are single-index integers palindromes?
   - If input type is unexpected (str, list, etc), return None or False?
3. - If the integer is negative, it's always False.
   - Output is a bool.
4. Brute force?: loop through each index of int and compare to its matching index on the other end
5. There is a one liner in Python that could achieve this with string manipulation
6/7. They are both O(n) but the algorithmic option has a better best cases, including O(1)
Whereas the one liner is always O(n)
8. There's definitely a better way to solve this without converting to strings
"""

def is_palindrome(number):
    # convert to string
    number = str(number)
    
    # check if negative
    if number[0] == '-':
        return False

    # loop through til midpoint of number
    for index in range(0, len(number) // 2):
        # if indexes don't match
        if number[index] != number[len(number) - 1 - index]:
            return False
    
    return True
      
def is_palindrome_one_liner(number):
    return str(number) == str(number)[::-1]

def main():
    print(is_palindrome(2002))
    print(is_palindrome_one_liner(2002))

if __name__ == "__main__":
    main()