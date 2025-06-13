list=[2,7,11,15]
target=17
def two_sum(nums,target):
    n=len(list)
    for i in range(n):
        for j in range(i+1,n):
            if list[i]+list[j]==target:
                return[i,j]
    return
result=two_sum(list,target)
print(result)
