"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

 

Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106

---- Optimization Suggestions ----
1. Current implementation has O((m+n)log(m+n)) time complexity and O(m+n) space complexity.
2. To achieve O(log(m+n)) time complexity, use binary search approach:
   - Instead of merging arrays, find the partition points in both arrays
   - Use binary search to find the correct partition
   - The median will be the average of the maximum of the left partition and minimum of the right partition
3. This approach would reduce space complexity to O(1) as it doesn't require creating a new array.
"""
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_length = len(nums1) + len(nums2)
        half_length = total_length // 2

        sorted_array = sorted(nums1 + nums2)

        # If the total number of elements is even, return the average of the two middle elements
        if len(sorted_array) % 2 == 0:
            return (sorted_array[half_length - 1] + sorted_array[half_length]) / 2

        # If the total number of elements is odd, return the middle element
        else:
            return sorted_array[half_length]
    
    def optimizedFindMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Optimized solution using binary search to achieve O(log(m+n)) time complexity.
        
        The key insight is that we don't need to merge the arrays. Instead, we can find
        the partition points in both arrays that divide the combined array into two equal halves.
        
        Time Complexity: O(log(min(m,n))) - we only need to binary search on the smaller array
        Space Complexity: O(1) - we only use a constant amount of extra space
        
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array to minimize binary search iterations
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_length = m + n
        is_even = total_length % 2 == 0
        
        # If one array is empty, return median of the other array
        # we only need to check m because we made sure nums1 is the smaller array
        if m == 0:
            if is_even:
                return (nums2[n//2 - 1] + nums2[n//2]) / 2
            else:
                return nums2[n//2]
        
        # Binary search on the smaller array (nums1)
        left, right = 0, m
        
        while left <= right:
            # --- Find partition points in both arrays ---
            """
            A partition is a point where we divide an array into two parts: a left part and a right part. In this problem, we're trying to find partitions in both arrays such that:
            
            All elements to the left of both partitions form the left half of the merged array
            
            All elements to the right of both partitions form the right half of the merged array

            nums1 = [1, 3, 8, 9]
            nums2 = [2, 4, 7, 10, 12]

            Let's say we partition nums1 after index 1 and nums2 after index 1:

            nums1: [1, 3 | 8, 9]
            nums2: [2, 4 | 7, 10, 12]

            Left partition elements:  [1, 3, 2, 4]
            Right partition elements: [8, 9, 7, 10, 12]

            ---

            All elements in the left partition should be less than or equal to all elements in the right partition

            The number of elements in the left partition should be (m+n+1)/2 for odd total length, or (m+n)/2 for even total length

            In the example above, this partition isn't valid because the left partition has 4 elements while the right partition has 5 elements, which doesn't satisfy the balanced partition requirement.

            All elements in the left partition ≤ all elements in the right partition

            - The left partition should have (m+n+1)/2 elements in total
            - In this example, with a total of 9 elements, the left partition should have 5 elements (for an odd-length array), but it only has 4. This is why the partition isn't valid.

            ---

            nums1: [1, 3, 8 | 9]
            nums2: [2, 4 | 7, 10, 12]

            Left partition:  [1, 3, 8, 2, 4]
            Right partition: [9, 7, 10, 12]


            since maxLeft1 (8) > minRight2 (7), we need to move partition1 to the left and partition2 to the right

            ---

            nums1: [1, 3 | 8, 9]
            nums2: [2, 4, 7 | 10, 12]
            

            in this case both min/max conditions are satisfied

            - maxLeft1 (3) <= minRight2 (10)
            - maxLeft2 (7) <= minRight1 (8)

            ---


            Once we find the correct partitions, the median is either:

            The average of max(left partition) and min(right partition) if total length is even

            The max(left partition) if total length is odd

            This partitioning approach is what allows us to find the median without actually merging the arrays, achieving the O(log(min(m,n))) time complexity.
            """

            # partition1 is the number of elements from nums1 in the left half
            # partition2 is the number of elements from nums2 in the left half
            partition1 = (left + right) // 2
            partition2 = (total_length + 1) // 2 - partition1
            
            # Get the four boundary elements
            # maxLeft1: maximum element in the left partition of nums1
            # minRight1: minimum element in the right partition of nums1
            # maxLeft2: maximum element in the left partition of nums2
            # minRight2: minimum element in the right partition of nums2
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if we found the correct partition
            # For a valid partition, all elements in the left half should be less than
            # all elements in the right half
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # We found the correct partition
                if is_even:
                    # For even length, median is average of max of left half and min of right half
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    # For odd length, median is max of left half
                    return max(maxLeft1, maxLeft2)
            
            # If maxLeft1 > minRight2, we need to move partition1 to the left
            # (reduce the number of elements from nums1 in the left half)
            elif maxLeft1 > minRight2:
                right = partition1 - 1
            
            # If maxLeft2 > minRight1, we need to move partition1 to the right
            # (increase the number of elements from nums1 in the left half)
            else:
                left = partition1 + 1
        
        # This should never happen if the input arrays are valid
        raise ValueError("Input arrays are not sorted or contain invalid elements")
    

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 3]
    nums2 = [2]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Test case 1: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Result: {result}")
    print(f"Expected: 2.0")
    print()
    
    # Test case 2
    nums1 = [1, 2]
    nums2 = [3, 4]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Test case 2: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Result: {result}")
    print(f"Expected: 2.5")
    print()
    
    # Test case 3 (empty array)
    nums1 = []
    nums2 = [1]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Test case 3: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Result: {result}")
    print(f"Expected: 1.0")
    
    # Test optimized solution
    print("\n--- Testing Optimized Solution ---")
    
    # Test case 1
    nums1 = [1, 3]
    nums2 = [2]
    result = solution.optimizedFindMedianSortedArrays(nums1, nums2)
    print(f"Test case 1: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Result: {result}")
    print(f"Expected: 2.0")
    print()
    
    # Test case 2
    nums1 = [1, 2]
    nums2 = [3, 4]
    result = solution.optimizedFindMedianSortedArrays(nums1, nums2)
    print(f"Test case 2: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Result: {result}")
    print(f"Expected: 2.5")
    print()
    
    # Test case 3 (empty array)
    nums1 = []
    nums2 = [1]
    result = solution.optimizedFindMedianSortedArrays(nums1, nums2)
    print(f"Test case 3: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Result: {result}")
    print(f"Expected: 1.0")

    
