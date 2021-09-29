# 메모리 사용량 최적화 하기

def IniteDinnerOptimized(guestList, dislikePairs):
    n, invite = len(guestList), []

    for i in range(2**n):
        Combination = []
        num = i
        for j in range(n):
            if (num % 2 == 1):
                Combination = [guestList[n-1-j]] + Combination
            num = num // 2
        good = True

        for j in dislikePairs:
            if j[0] in Combination and j[1] in Combination:
                good = False

        if good:
            if len(Combination) > len(invite):
                invite = Combination

    print("Optimun Solution: ", invite)


if __name__ == '__main__':
    dislikePairs = [['Alice', 'Bob'], ['Bob', 'Eve']]
    guestList = ["Alice", "Bob", "Cleo", "Don", "Eve"]
    IniteDinnerOptimized(guestList, dislikePairs)