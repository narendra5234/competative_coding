class TwoPointers:
    # Brute Force O(nlogn)
    @staticmethod
    def sq_of_sorted_arr_1(arr: list):
        arr.sort(key=lambda x: abs(x))
        return list(map(lambda x: x ** 2, arr))

    # two pointer approach
    @staticmethod
    def sq_of_sorted_arr_2(arr: list):
        start = 0
        while start<len(arr):
            if arr[start]>0:
                break
            start += 1
        start-=1

        nums2 = arr[start + 1:]
        arr = list(map(lambda x: abs(x), arr))
        nums1=arr[:start+1][::-1]
        i, j, temp = 0, 0, []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                temp.append(nums1[i]**2)
                i += 1
            else:
                temp.append(nums2[j]**2)
                j += 1
        while i < len(nums1):
            temp.append(nums1[i]**2)
            i += 1
        while j < len(nums2):
            temp.append(nums2[j]**2)
            j += 1
        return temp

print(TwoPointers().sq_of_sorted_arr_2([-4,-1,0,3,10]))
