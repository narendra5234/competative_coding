class TwoSum:
    @staticmethod
    def two_sum(arr, target):
        h = {}
        for _index, each_ele in enumerate(arr):
            n = target - each_ele
            if n not in h:
                h[each_ele] = _index
            else:
                print([h[n], _index])


obj = TwoSum()
obj.two_sum([2, 7, 11, 15], 9)
