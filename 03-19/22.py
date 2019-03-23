'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''
from functools import reduce
from unittest import TestCase


def solution(array=[]):
  number_of_zeros = array.count(0)
  if number_of_zeros > 1:
    return [0 for x in array]
  elif number_of_zeros == 1:
    is_not_zero = lambda x: x if not 0 else None
    zero_free_array = filter(is_not_zero, array)
    total = reduce(lambda a,b: a*b, zero_free_array)
    return list(map(lambda x: 0 if x else total, array))
  else:
    total = reduce(lambda a,b: a*b, array)
    return list(map(lambda x: total/x if x else total, array))


class Test(TestCase):
  def test_without_zeros(self):
    self.assertEqual(solution([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
  
  def test_with_one_zero(self):
    self.assertEqual(solution([1,3,0,5]), [0, 0, 15, 0])

  def test_with_two_zeros(self):
    self.assertEqual(solution([0,0,1,2]), [0, 0, 0, 0])