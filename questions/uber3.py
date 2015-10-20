def func(lists):
    if len(lists) == 0:
        return [None]
    else:
        new = []
        t = func(lists[1:])
        for x in t:
            for y in lists[0]:
                if not x:
                    new.append([y])
                else:
                    new.append([y]+x)
        return new

print func([[1,2,3], [1], [2,3]])
