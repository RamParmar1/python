class Solution:
  def findMedianSortedArrays(self, nums1, nums2) :
    n1 = len(nums1)
    n2 = len(nums2)
    if n1 > n2:
      return self.findMedianSortedArrays(nums2, nums1)

    l = 0
    r = n1

    while l <= r:
      part1 = (l + r) // 2
      part2 = (n1 + n2 + 1) // 2 - part1
      maxLeft1 = -2**31 if part1 == 0 else nums1[part1 - 1]
      maxLeft2 = -2**31 if part2 == 0 else nums2[part2 - 1]
      minRight1 = 2**31 - 1 if part1 == n1 else nums1[part1]
      minRight2 = 2**31 - 1 if part2 == n2 else nums2[part2]
      if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
        return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) * 0.5 if (n1 + n2) % 2 == 0 else max(maxLeft1, maxLeft2)
      elif maxLeft1 > minRight2:
        r = part1 - 1
      else:
        l = part1 + 1
