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

    # print(guestList, dislikePairs)

    dislike_people = set(itertools.chain(*dislikePairs))

    have_dislike = [] # 싫어 하는 사람이 있는 사람
    like = [] # 싫어 하는 사람이 없느 사람

    for man in guestList:
        if man[0] in dislike_people:
            have_dislike.append(man)
        else:
            like.append(man)

    # print(like, have_dislike)

    return like, have_dislike


def check_like_high(guestList, dislikePairs):
    """ 서로 싫어 하는 1쌍 중에서 친밀도가 가장
        높은 1쌍을 찾고 그 쌍과 연결되어 있는
        사람을 제거 합니다.

    Args:
        guestList ([list]]): [손님 리스트]
        dislikePairs ([list]): [싫어하는 쌍]

    Returns:
        guestList ([list]]): [1쌍제거, 1쌍과 연결되어있는 사람 제거]
        dislikePairs ([list]]): [1쌍과 연결 안되어 있는 서로 싫어하는 쌍]
        order_max  ([list]]): [1쌍 중에서 친밀도가 가장 높은 1쌍]
    """

    # print(guestList, dislikePairs)
    max_pairs = [] # 애정도가 가장 높은 1쌍
    max_like_sum = 0 # 애정도 저장 값

    # 딕셔너리로 변환
    guestListDict = dict(guestList)

    for pairs in dislikePairs:
        tmp_like_sum = 0
        for man in pairs: # 딕셔너리 안에서 값 꺼냄
            tmp_like_sum += guestListDict[man]

        #  가장 큰 값 생성
        if tmp_like_sum > max_like_sum:
            max_like_sum = tmp_like_sum
            max_pairs = pairs

    # 1쌍 찾기
    pair1 = (max_pairs[0], guestListDict[max_pairs[0]])
    pair2 = (max_pairs[1], guestListDict[max_pairs[1]])

    # 1쌍 제거
    del guestList[guestList.index(pair1)]
    del guestList[guestList.index(pair2)]

    # 1쌍에 연결되어 제거되는 사람 찾기
    order_max = [pair1, pair2]
    delete_set = set() # 제거 될 사람 저장 공간
    no_delete_set = []
    for pairs in dislikePairs:
        if pair1[0] not in pairs and\
           pair2[0] not in pairs:
           no_delete_set.append(pairs)
        
        if pair1[0] in pairs or\
           pair2[0] in pairs:
           delete_set.update(pairs)
           

    # print(delete_set)
    dislikePairs = no_delete_set
    # print(no_delete_set)

    # guestList 에서 제거하기
    # 1쌍에 연결 안된 사람 추출
    guestList = [man for man in guestList if man[0] not in delete_set]
    # print(guestList)

    # print(order_max)
    # print(dislikePairs) # dislikePairs 제거 해야함 
    return guestList, dislikePairs, order_max 


def choose_another_friend(guestList, dislikePairs):
    """ 남은 사람중에서 가장 친밀도가 높은 사람을 선택하고
        그 선택된 사람과 연결되어 있는 사람들을 모두 제거

    Args:
        guestList ([list]]): [손님 리스트]
        dislikePairs ([list]): [싫어하는 쌍]

    Returns:
        max_man ([list]]): [쌍이 아닌 혼자인 가장 친밀도가 높은사람]
    """

    if len(guestList) <= 0:
        return []

    # 남은 사람중에 가장 친한사람 1명
    max = 0
    for man in guestList:
        if man[1] > max:
            max = man[1]
            max_man = man

    # print(max_man)

    delete_set = set()
    # 그 한명과 연결된 사람 찾기
    for pairs in dislikePairs:
        if max_man[0] in pairs or\
           max_man[0] in pairs:
           delete_set.update(pairs)

    # 연결된 사람 제거
    guestList = [man for man in guestList if man[0] not in delete_set]

    # print(guestList, dislikePairs)

    return [max_man] + choose_another_friend(guestList, dislikePairs)

    


def IniteDinnerOptimized(guestList, dislikePairs):


    # 싫어하는 사람이 없는 사람 제외
    exception_people, guestList = \
        check_list(guestList, dislikePairs)

    # 친밀 도가 가장 높은 서로 싫어하는 1쌍 추출
    # 위의 1쌍과 연결된 다른 인원 제거
    guestList, dislikePairs, max_pairs = \
        check_like_high(guestList, dislikePairs)
    # print(guestList, dislikePairs, max_pairs)

    # 나머지 가장 큰 값 1개씩 찾기
    other_friend = choose_another_friend(guestList, dislikePairs)
    # print(other_friend)

    invite = []
    invite += max_pairs
    invite += exception_people
    invite += other_friend
    
    like_sum = 0
    for mas in invite:
        like_sum += mas[1]

    # 결과
    print("Optimun Solution: ", invite)
    print("Weight is : {}".format(like_sum))

if __name__ == '__main__':
    LargeDislikes = [['B','C'],['C','D'],['D','E'],['F','G'],
                     ['F','H'],['F','I'],['G','H']]

    LargeGustList = [('A',2),('B',1),('C',3),
                     ('D',2),('E',1),('F',4),
                     ('G',2),('H',1),('I',3)]
                     
    IniteDinnerOptimized(LargeGustList, LargeDislikes)
    # 정답 v
    # Optimun Solution:  [('F', 4), ('I', 3), ('A', 2), ('C', 3), ('E', 1)]
    # Weight is : 13