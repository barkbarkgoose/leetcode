def bubble_sort(target_list):
    for _ in range(len(target_list) - 1):
        for index in range(len(target_list) - 1):
            if target_list[index + 1] < target_list[index]:
                # Swap in-place
                target_list[index], target_list[index + 1] = target_list[index + 1], target_list[index]


class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # add nums2 into position behind nums1 (unordered)
        nums2_index = 0

        for index in range(m, (m + n)):
            nums1[index] = nums2[nums2_index]
            nums2_index += 1

        # order list
        bubble_sort(nums1)


if __name__ == '__main__':
    nums1_1 = [1, 2, 3, 0, 0, 0]
    nums2_1 = [2, 5, 6]

    Solution1 = Solution()
    Solution1.merge(nums1_1, 3, nums2_1, 3)

    print(nums1_1)