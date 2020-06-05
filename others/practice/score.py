for t in range(int(input())):
    n = int(input())
    from collections import defaultdict
    score_dict = defaultdict(list)
    for i in range(n):
        q, s = map(int, input().split())
        score_dict[q].append(s)
    score_sum=0
    for i in score_dict.keys():
        if 1<=i<=8:
            score_sum+=max(score_dict[i])
    print(score_sum)
