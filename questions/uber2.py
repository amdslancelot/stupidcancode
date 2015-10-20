def func(s1, s2):
    if s1 == s2:
        return False
    i1 = 0
    i2 = 0
    r = 0
    l1 = len(s1)
    l2 = len(s2)
    if l1 == l2:
        return False

    while i1 <= l1-1 and i2 <= l2-1:
        if s1[i1] == s2[i2]:
            i1 += 1
            i2 += 1
            continue
        r += 1
        if l1 > l2:
            i1 += 1
        else:
            i2 += 1

    return (i1 == l1 and i2 == l2 and r==1) or (r==0 and (l1-i1)+(l2-i2) == 1)

print func("abc", "ac"), True
print func("abcd", "ac"), False
print func("abd", "ac"), False
print func("abd", "ac"), False

print func("bdc", "ac"), False
print func("ac", "ac"), False
print func("abd", "ace"), False

print func("aaa", "aa"), True
print func("aaaa", "aa"), False

