class MedianOfTwoSortedArrays:
    # brute force O(nlogn)- using sort()
    @staticmethod
    def median_of_two_sorted_arrays(nums1: list, nums2: list):
        nums1.sort()
        nums2.sort()
        new_arr = nums1 + nums2
        new_arr.sort()

        if len(new_arr) % 2 == 1:
            return new_arr[len(new_arr) // 2]
        else:
            return (new_arr[len(new_arr) // 2] + new_arr[(len(new_arr) // 2) - 1]) / 2

    # O(n)- merge part of merge sort technique
    @staticmethod
    def median_of_to_sorted_arrays_1(nums1: list, nums2: list):
        i, j, temp = 0, 0, []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1
        while i < len(nums1):
            temp.append(nums1[i])
            i += 1
        while j < len(nums2):
            temp.append(nums2[j])
            j += 1
        # now temp is the sorted array

        if len(temp) % 2 == 1:
            return temp[len(temp) // 2]
        else:
            return (temp[len(temp) // 2] + temp[(len(temp) // 2) - 1]) / 2

    # can be also solved in O(logn) using Binary Search.
