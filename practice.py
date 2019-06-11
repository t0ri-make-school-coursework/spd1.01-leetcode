"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
------------------------------------------------------------------------------------------------------------
1. Write a function that takes in an array of numbers and a specific target number, and returns the indexes
of the two numbers from inside the list that add up to that target.
2. - Is each index an int?
   - Is the target always an int?
   - Is the array sorted?
3. - If the input has no solution return None
4. Brute force -- loop through adding arr[0...] to arr[0...] and checking against target
5. To reduce the runtime from O(n^2) (looping through list twice), put indexes into a hashtable
   - Keys will be remaining value needed to get to target
   - Check if each array of numbers is already in dictionary
   - If value is found, return both indexes
   - Otherwise, add new key (target - num) as equal to (num, index)
   - Return None if no match
6. This will allow faster lookup and reduce the runtime to O(n)
7/8. Using brute force is slower but easier to get through in an interview?
"""

def brute_force(numbers, target):
    for iterator in range(0, len(numbers) - 1):
      for index in range(0, len(numbers) - 1):
          if numbers[iterator] + numbers[index] == target:
              return [iterator, index]

    return None

def hashtable(numbers, target):
    dictionary = dict()

    for index, num in enumerate(numbers):
        if num in dictionary:
            return [dictionary[num][1], index]
        dictionary[target - num] = (num, index)
    
    return None

def main():
    numbers = [2, 7, 11, 15]
    target = 13
    print('brute force: {}'.format(brute_force(numbers, target)))
    print('hashtable: {}'.format(hashtable(numbers, target)))

if __name__ == "__main__":
    main()
