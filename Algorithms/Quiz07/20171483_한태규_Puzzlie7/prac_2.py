

def bsearch(L, input_num ,value):
  
    lo, hi = 0, len(L)-1
    print(lo, hi)

    while lo <= hi:
        mid = (lo + hi) // 2
       #To trace execution
        print ("LOW = ", lo, "HIGH = ", hi, "MID = ", mid)
        print("HIGH - LOW : ", hi - lo)

        ## prac_2 추가
        # 11 - 6 
        if hi-lo < input_num:
            print("start for loop > ")
                                # 6 ~ 11
            for i in range(lo,hi):
                if L[i] == value:
                    print ("Found at location", i + 1)
                    return i + 1

            print ("Found at location", mid)
            return mid

        if L[mid] < value:
            lo = mid + 1
        elif value < L[mid]:
            hi = mid - 1
        else:
            print ("Found at location", mid)
            return mid
            
    print ("Could not find the value", value)
    return NOTFOUND

NOTFOUND = -1

Ls = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, \
     71, 73, 79, 83, 89, 97]

# bsearch(Ls, 3, 5)
bsearch(Ls, 10, 23)