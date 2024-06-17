def minNum(source, target):
    for char in target:
        if char not in source:
            return -1

    count, i, j=0,0,0

    while j<len(target):
        count+=1
        i=0
        while i<len(source) and j<len(target):
            if source[i]==target[j]:
                j+=1
            i+=1

    return count

ans=minNum("abc", "abcbc")
print(ans)
ans=minNum("abc", "acdbc")
print(ans)
ans=minNum("xyz", "xzyxz")
print(ans)