lst = [1,2,3,4,5,6,7,8]
def maskn(lst, i):
    mask = [x != 1 if x/i != (int) else x != 0 for x in lst]
    return mask
    maskn(lst, 2)
    print(mask)