# 메모리 사용량 최적화 하기
import itertools


def check_list(guestList, dislikePairs):
    """ 싫어 하는 사람이 있는 사람과
        없는 사람을 나누는 함수

    Args:
        guestList ([list]]): [손님 리스트]
        dislikePairs ([list]): [싫어하는 쌍]

    Returns:
        [list]: [싫어하는 사람이 있는사람 / 없는 사람]
    """
    # 싫어하는 사람이 있는 사람 집합으로 만들기
    dislike_people = set(itertools.chain(*dislikePairs))

    have_dislike = [] # 싫어 하는 사람이 있는 사람
    like = [] # 싫어 하는 사람이 없느 사람

    for man in guestList:
        if man in dislike_people:
            have_dislike.append(man)
        else:
            like.append(man)

    # print(like, have_dislike)

    return like, have_dislike


def IniteDinnerOptimized(guestList, dislikePairs):

    # 싫어하는 사람이 없는 사람 제외
    exception_people, guestList = \
        check_list(guestList, dislikePairs)

    # print(exception_people, guestList)
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


    # 제외 했던 사람 추가
    invite = invite + exception_people
    print("Optimun Solution: ", invite)


if __name__ == '__main__':
    dislikePairs = [['Alice', 'Bob'], ['Bob', 'Eve']]
    guestList = ["Alice", "Bob", "Cleo", "Don", "Eve"]
    IniteDinnerOptimized(guestList, dislikePairs)
    # 정답 : Optimun Solution:  ['Alice', 'Eve', 'Cleo', 'Don']