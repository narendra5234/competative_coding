for t in range(int(input())):
    n = int(input())
    prices = list(map(int, input().split()))
    good_days = 1
    for i in range(len(prices)):
        j = 0
        count = 0
        while j < i:
            if i <= 5:
                if prices[i] <= prices[j]:
                    count += 1
                j += 1
            else:
                j += i - 5
                if prices[i] < prices[j]:
                    count += 1
        if count == 5:
            good_days += 1
    print(good_days)
