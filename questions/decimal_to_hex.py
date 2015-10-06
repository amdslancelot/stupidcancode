def decimalToHex(n):
    r = ""
    
    count = 0
    while n/(16**count) > 0:
        count += 1
    count -= 1 
    
    while count > 0:
        t = n / 16**count
        n = n % 16**count
        
        if t >= 10:
            r = r + chr(t+55)
        else:
            r = r + str(t)
        count -= 1
        
    remain = n%16
    if remain >= 10:
        r = r + chr(remain+55)
    else:
        r = r + str(remain)
        
    return r

print decimalToHex(16)
print decimalToHex(1000)

