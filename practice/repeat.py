# nums=list(map(int,input().split()))
# count={}
# for i in nums:
#     count[i]=nums.count(i)
# m=max(nums)
# missing=list(set(list(range(1,m+1)))-set(nums))
# B=missing[0]
# for i in nums:
#     if count.get(i) == 2:
#         A=i
#         break
#
#
# A=list(map(int,input().split()))
# A1=set(A)
# A1=list(A1)
# a=sum(A)-sum(A1)
# n=len(A)
# b=int((n*(n+1)/2)-)
# print(a,b)

l=list(map(int,input().split()))
n=len(l)
occurrence=n/3
count=[0]*n
for i in l:
    count[i] += 1
for i in l:
    if count[i]>=occurrence:
        print(i)
        break



