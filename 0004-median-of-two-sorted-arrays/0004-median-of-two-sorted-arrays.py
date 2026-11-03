class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num = nums1 + nums2
        num.sort()
        l = len(num)
        if l % 2 == 0:
            return (num[l//2] + num[(l//2)-1]) / 2
        else:
            return num[l//2]
        