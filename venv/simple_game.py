def simple_game():
    for t in range(int(input())):
        chef_coins = ramsay_coins = 0
        for i in range(int(input())):
            coins = list(map(int, input().split()))[1:]
            mid = len(coins) // 2
            i = 0
            if len(coins) % 2 == 0:
                while i < mid:
                    chef_coins += coins[i]
                    ramsay_coins += coins[len(coins) - i - 1]
                    i += 1
            else:
                while i < mid:
                    chef_coins += coins[i]
                    ramsay_coins += coins[len(coins) - i - 1]
                    i += 1



        print(chef_coins)


simple_game()
