'''
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''
import unittest


def solution(list_of_numbers, target_number):
  low = 0
  high = len(list_of_numbers) - 1
  while low < high:
    case_sum = list_of_numbers[low] + list_of_numbers[high]
    if case_sum < target_number:
      low += 1
    elif case_sum > target_number:
      high += 1
    elif case_sum == target_number:
      return True
  return False

class SolutionTest(unittest.TestCase):  
  def test_if_workig(self):
    self.assertTrue(solution([10, 15, 3, 7], 17))
    self.assertFalse(solution([1,3,3,7], 11))
    self.assertTrue(solution([-4,1,2,3,10],6))
