import unittest

def reverseList(ulist):
    if len(ulist) % 2 == 0:
        for i in range(0, int(len(ulist) / 2)):
            ulist[i], ulist[len(ulist) - 1 - i] = ulist[len(ulist) - 1 - i], ulist[i]
        return ulist
    else:
        print('nah son')

print(reverseList([0,1,2,3]))
