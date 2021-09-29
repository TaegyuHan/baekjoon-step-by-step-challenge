# 메모리 사용량 최적화 하기

def IniteDinnerOptimized(guestList, dislikePairs):
    n, invite = len(guestList), []
    init_like = 0 ## 애정도 합 초기화

    for i in range(2**n):
        Combination = []
        num = i
        like_sum = 0 ## 애정도 합 저장
        for j in range(n):
            if (num % 2 == 1):
                ##                   이름만 추출 [0] < 추가
                Combination = [guestList[n-1-j][0]] + Combination
                like_sum += guestList[n-1-j][1] ## 애정도 합 구하기
            num = num // 2
        good = True

        for j in dislikePairs:
            if j[0] in Combination and j[1] in Combination:
                good = False

        if good:
            # print(Combination)
            # print(like_sum)
            # 애정도 합으로 if문
            if (like_sum > init_like):
                init_like = like_sum
                invite = Combination

    print("Optimun Solution: ", invite)


if __name__ == '__main__':
    dislikePairs = [['Alice', 'Bob'], ['Bob', 'Eve']]
    guestList = [("Alice", 2), ("Bob", 6), ("Cleo", 3),
                 ("Don", 10), ("Eve",3)]
    IniteDinnerOptimized(guestList, dislikePairs)
    # 정답 : Optimun Solution:  ['Bob', 'Cleo', 'Don']