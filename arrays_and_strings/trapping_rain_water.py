class TrapRainWater:
    # brute force -O(n2)
    @staticmethod
    def get_water(arr):
        res = 0
        for i in range(1, len(arr) - 1):
            l_max, r_max = arr[i], arr[i]
            l_max = max(arr[0:i+1])
            r_max = max(arr[i+1:len(arr)])
            res += (min(l_max, r_max) - arr[i])
        print(res)# wrong.

    @staticmethod
    def get_water_1(arr):
        res = 0
        for i in range(1, len(arr) - 1):
            l_max = arr[i]
            for j in range(0, i):
                l_max = max(l_max, arr[j])
            r_max = arr[i]
            for j in range(i + 1, len(arr)):
                r_max = max(r_max, arr[j])
            res += (min(l_max, r_max) - arr[i])
        print(res)


# optimize code b pre-computing lmax and  rmax

obj = TrapRainWater()
obj.get_water_1([3, 0, 1, 2, 5])
obj.get_water_1([1, 2, 3])
