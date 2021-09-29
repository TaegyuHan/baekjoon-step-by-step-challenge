def Good(Comb: list, candList: list, candTalents: list, AllTalents: list):
    """선택된 참가자의 프로그램에 모든 재능이
       방송 되는지 확인한다.

    Args:
        Comb (list): [선택 참가자]
        candList (list): [모든 참가자]
        candTalents (list): [참가자 각각의 재능]
        AllTalents (list): [참가자의 모든 재능]

    Returns:
        [bool]: [모든 재능을 포함했는지 확인합니다.]
    """

    for tal in AllTalents:  # 모든 재능 검사
        cover = False
        for cand in Comb:  # 선택 참가자 1명씩 검사
            candTal = candTalents[candList.index(cand)]
            if tal in candTal:  # 있으면 통과
                cover = True
        if not cover:  # 없으면  False
            return False

    return True  # 있으면  True


def check_unique_talent(candList: list, candTalents: list, talentList: list):
    """유일하게 특정 재능을 가지고 있는 후보들을 찾고
       이와 같은 후보들이 가지고 있는 모든 재능을 
       테이블에서 제거해서 테이블을 줄입니다.

    Args:
        candList (list): [모든 참가자]
        candTalents (list): [모든 참가자의 재능]
        talentList (list): [재능]

    Returns:
        제거한
        unique_candList (list): [가지고 있는 후보]
        candList (list): [모든 참가자]
        candTalents (list): [모든 참가자의 재능]
        talentList (list): [재능]
    """

    # print(candList, candTalents, talentList)

    # 테이블 생성
    talent_table = {}
    for key in talentList:
        talent_table[key] = []

    # 유일하게 특정 재능을 
    # 가지고 있는 후보
    unique_candList = []

    # 테이블 데이터 넣기
    for i in range(len(candList)):
        for key in candTalents[i]:
            talent_table[key].append(candList[i])
    # print(talent_table)

    for key, val in talent_table.items():
        if len(val) == 1: # 특정 1개의 재능을 가진 사람
            unique_candList.append(val[0]) # list에 따로 추가

            for talent_item in candTalents[candList.index(val[0])]:
                talentList.remove(talent_item) # table 항목에서 제거

            del candTalents[candList.index(val[0])] # 기존 항목에서 제거
            candList.remove(val[0])  # 기존 항목에서 제거

    # print(candList)
    # print(candTalents)
    # print(talentList)

    return unique_candList, candList, candTalents, talentList


def Hire4Show(candList: list, candTalents: list, talentList: list):
    """최소한의 후보를 출력합니다.

    Args:
        candList (list): [모든 참가자]
        candTalents (list): [모든 참가자의 재능]
        talentList (list): [재능]
    """

    # prac 2
    # 
    unique_candList, candList, candTalents, talentList = \
      check_unique_talent(candList, candTalents, talentList)

    n = len(candList)
    hire = candList[:]

    # 모든 경우의 수
    for i in range(2**n):
        Combination = []
        num = i

        # 조합 뽑기
        for j in range(n):
            if (num % 2 == 1):
                Combination = [candList[n-1-j]] + Combination
            num = num // 2

        # 모든 재능 만족하는지 확인
        if Good(Combination, candList, candTalents, talentList):
            if len(hire) > len(Combination):
              hire = Combination
        # print(Combination)

    print("Optimum Solution: ", unique_candList + hire)


if __name__ == '__main__':

    Talents = ["Sing", "Dance", "Magic", "Act", "Flex", "Code"]
    Candidates = ["Aly", "Bob", "Cal", "Don", "Eve", "Fay"]
    CandidateTalents = [["Flex", "Code"], ["Dance", "Magic"],
                        ["Sing", "Magic"], ["Sing", "Dance"],
                        ["Dance", "Act", "Code"], ["Act", "Code"]]

    Hire4Show(Candidates, CandidateTalents, Talents)