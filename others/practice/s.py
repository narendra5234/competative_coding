s="abcbabcbb"
i, mx, l, dc = 0, 0, len(s), {}
while i < l:
    if s[i] not in dc:
        dc[s[i]] = i
        i += 1
    else:
        mx = max(mx, len(dc))
        i = dc[s[i]] + 1
        dc = {}

print(max(mx, len(dc)))