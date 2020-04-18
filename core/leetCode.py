from listNode import ListNode

class Solution:

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
  def twoSum(self, nums: [int], target: int) -> [int]:
    # Baseline t o(n^2), s o(1)
    # for i, num1 in enumerate(nums):
    #   for j, num2 in enumerate(nums[1:]):
    #     if (num1 + num2 == target):
    #       return [i, j + 1]

    # Single pass hash map t o(n), s o(n)
    h = {}
    for i, num in enumerate(nums):
      if target - num not in h:
        h[num] = i
      else: 
        return [h[target - num], i] 

  # You are given two non-empty linked lists representing two non-negative integers. 
  # The digits are stored in reverse order and each of their nodes contain a single digit. 
  # Add the two numbers and return it as a linked list.
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    # Baseline t o(n), s o(n)
    summation = ListNode(0)
    head = summation
    carry = 0
    while (l1 is not None or l2 is not None):
      n1 = 0
      if (l1 is not None):
        n1 = l1.value()
        l1 = l1.next()
      n2 = 0  
      if (l2 is not None):
        n2 = l2.value()
        l2 = l2.next()
      summation.next = ListNode((n1 + n2 + carry) % 10)
      carry = (n1 + n2) // 10
      summation = summation.next
    if (carry > 0):
      summation.next = ListNode(carry)
    return (head.next)

  # Given a string, find the length of the longest substring without repeating characters.
  def lengthOfLongestSubstring(self, s: str) -> int:
    # Baseline t o(n^3), s o(n)
    max = 0
    for i in range(len(s)):
      print(s[i])
    return 0


  #There are two sorted arrays nums1 and nums2 of size m and n respectively.
  # Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
  # You may assume nums1 and nums2 cannot be both empty.
  # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
  #   isOdd = True
  #   if(len(nums1) + len(nums2) % 2 == 0):
  #     isOdd = False
    