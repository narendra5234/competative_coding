class Leaders:
    # brute force-O(n2)
    @staticmethod
    def leaders_1(arr):
        for i in range(len(arr)):
            c = 0
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    c += 1
            if c == len(arr) - 1 - i:
                print(arr[i], end="")

    @staticmethod
    def leaders_2(arr):
        for i in range(len(arr)):
            flag = False
            for j in range(i + 1, len(arr)):
                if arr[i] <= arr[j]:
                    flag = True
                    break
            if flag is False:
                print(arr[i], end="")

    @staticmethod
    def leaders_3(arr):
        curr_value = arr[len(arr) - 1]
        leaders = [curr_value]
        for j in range(len(arr) - 2, 0, -1):
            if arr[j] > curr_value:
                curr_value = arr[j]
                leaders.append(curr_value)
        print(leaders[::-1])


obj = Leaders()
obj.leaders_1([7, 10, 4, 3, 6, 5, 2])
print("\n")
obj.leaders_2([7, 10, 4, 3, 6, 5, 2])
