"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        largest = 0
        start = 0
        end = 0

        for idx, line in enumerate(height):
            seek = idx + 1
            while seek < len(height):
                distance = abs(idx - seek)
                alt = min(line, height[seek])
                volume = distance * alt

                if volume > largest:
                    largest = volume
                    start = min(idx, seek)
                    end = max(idx, height[seek])

                seek += 1
        
        return largest

    def maxAreaOptimized(self, height):
        """
        Optimized O(n) solution using two pointers.
        
        Key insight: Start with maximum width (pointers at both ends).
        The area is limited by the shorter line, so we move the pointer
        with the smaller height inward. This is safe because moving the
        taller pointer can only decrease the area (width decreases, height
        is still limited by the shorter line).
        
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate current area
            width = right - left
            min_height = min(height[left], height[right])
            area = width * min_height
            max_area = max(max_area, area)

            # Move the pointer with the smaller height
            # This is the key optimization: we can skip many pairs
            # because moving the taller pointer can only decrease area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == '__main__':
  solution = Solution()

  height_array = [1,8,6,2,5,4,8,3,7]
  
  # Test original solution
  volume = solution.maxArea(height_array)
  print('Original solution - volume:', volume)
  print('Pass:', volume == 49)
  
  # Test optimized solution
  volume_optimized = solution.maxAreaOptimized(height_array)
  print('\nOptimized solution - volume:', volume_optimized)
  print('Pass:', volume_optimized == 49)
  
  # Test with larger array to demonstrate performance
  import time
  large_array = list[int](range(5000))
  
  start = time.time()
  result_original = solution.maxArea(large_array)
  time_original = time.time() - start
  
  start = time.time()
  result_optimized = solution.maxAreaOptimized(large_array)
  time_optimized = time.time() - start
  
  print(f'\nLarge array (5000 elements):')
  print(f'Original: {time_original:.4f}s, Optimized: {time_optimized:.4f}s')
  print(f'Results match: {result_original == result_optimized}')