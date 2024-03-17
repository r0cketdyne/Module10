



def two_sum(num_arr, target):
    """
    Finds indices of two numbers in the given list that add up to the target sum.

    Args:
    - num_arr: List of integers
    - target: Target sum

    Returns:
    - List containing indices of the two numbers, or None if no such pair exists
    """

    # Create a dictionary to store the indices of numbers
    num_indices = {}

    # Iterate through the list of numbers along with their indices
    for i, num in enumerate(num_arr):
        # Calculate the complement of the current number required to reach the target sum
        complement = target - num

        # Check if the complement exists in the num_indices dictionary
        if complement in num_indices:
            # If found, return the indices of the current number and its complement
            return [num_indices[complement], i]

        # If the complement doesn't exist in the dictionary,
        # store the current number's index in the num_indices dictionary
        num_indices[num] = i

    # If no such pair is found, return None
    return None

# Example usage:
num_arr = [2, 7, 11, 15]
target = 9

# complement 4, complement 2, complement , -3, -6
print(two_sum(num_arr, target))  # Output: [0, 1]



"""
Given an array of integers nums and an integer target,
#return indices of the two numbers such that they add up to target.
#You may assume that each input would have
#exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

#first we create a function, or mini problem solving prog
#like a knife at a swiss army knife
# we will make a dict. probably a kind of obj

