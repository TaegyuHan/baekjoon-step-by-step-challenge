# 구간 이분 탐색
def bisectionSearchForSquareRoot(x, epsilon):

    if x < 0:
        print ('Sorry, imaginary numbers are out of scope!')
        return
    
    numGuesses = 0
    
    low = 0.0
    high = max(x, 1.0)

    # 0.125
    ans = (high + low)/2.0

    # print(ans) # 0.125

          
    while abs(ans**2 - x) >= epsilon:

        # print("ans**2 : ", ans**2)
        if ans**2 < x:
            low = ans
        else:
            high = ans

        ans = (high + low)/2.0
        numGuesses += 1

        print("numGuesses : ", numGuesses)
        print('low = ', low, 'high = ', high, 'guess = ', ans)
        print()

    print(abs(ans**2 - x))
    print ('numGuesses =', numGuesses)
    print (ans, 'is close to square root of', x)

    return

bisectionSearchForSquareRoot(0.25, .01)


