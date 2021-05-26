def bisectionSearchForSquareRoot(start, end, epsilon):

    numGuesses = 0
    low = start # -10
    high = end # 10

    # 0
    ans = (high + low)/2.0

    print("start > ", ans)

    # 수정
    while abs(ans**3 + ans**2 - 11) >= epsilon:

        # 수정
        if ans**3 + ans**2 < + 11:
            low = ans
        else:
            high = ans

        ans = (high + low)/2.0
        numGuesses += 1

        print('low = ', low, 'high = ', high, 'guess = ', ans)

    print(abs(ans**3 + ans**2 + 11))
    print ('numGuesses =', numGuesses)
    print (ans, 'is close to square root of', -11)

    return

# https://www.wolframalpha.com/input/?i=x%5E3%2Bx%5E2%2B11%3D0

bisectionSearchForSquareRoot(-10, 10, .01)

# bisectionSearchForSquareRoot(65535, .01)
