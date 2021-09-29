
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
        for cand in Comb: # 선택 참가자 1명씩 검사
            candTal = candTalents[candList.index(cand)]
            if tal in candTal: # 있으면 통과
                cover = True
        if not cover: # 없으면  False
            return False

    return True  # 있으면  True


def check_overlap_talent(candList: list, candTalents: list):
    """어떤 후보의 재능이 다른 후보에 의해 모두
       포함될 경우 제거

      Args:
          candList (list): [모든 참가자]
          candTalents (list): [모든 참가자의 재능]

    Returns:
          제거한
          candList (list): [모든 참가자]
          candTalents (list): [모든 참가자의 재능]
    """

    del_candList = []
    del_candTalents = []

    for i in range(len(candList)):
        for j in range(i+1, len(candList)):
            i_len = len(candTalents[i])
            j_len = len(candTalents[j])

            # print(i, j)
            # print(i_len, j_len)
            # print(candTalents[i], candTalents[j])

            # 개수가 같고 
            if i_len == j_len:
                # 포함되면 제거
                if all(map(lambda x: x in candTalents[i], candTalents[j])):
                    del_candList.append(candList[j])
                    del_candTalents.append(candTalents[j])

            # 개수가 i가 크고 
            elif i_len > j_len:
                # 포함되면 제거
                if all(map(lambda x: x in candTalents[i], candTalents[j])):
                    del_candList.append(candList[j])
                    del_candTalents.append(candTalents[j])

            # 개수가 j가 크고
            elif i_len < j_len:
                # 포함되면 제거
                if all(map(lambda x: x in candTalents[j], candTalents[i])):
                    del_candList.append(candList[i])
                    del_candTalents.append(candTalents[i])

    # 모두 포함되는 사람 제거
    for i in range(len(del_candList)):
        candList.remove(del_candList[i])
        candTalents.remove(del_candTalents[i])

    # print(candList, candTalents)
    return candList, candTalents


def Hire4Show(candList: list, candTalents: list, talentList: list):
    """최소한의 후보를 출력합니다.

    Args:
        candList (list): [모든 참가자]
        candTalents (list): [모든 참가자의 재능]
        talentList (list): [재능]
    """

    # prac 1
    # 제거 하는 함수 생성
    candList, candTalents = check_overlap_talent(candList, candTalents)

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

    print("Optimum Solution: ", hire)


if __name__ == '__main__':

    Talents = ["Sing", "Dance", "Magic", "Act", "Flex", "Code"]
    Candidates = ["Aly", "Bob", "Cal", "Don", "Eve", "Fay"]
    CandidateTalents = [["Flex", "Code"], ["Dance", "Magic"],
                        ["Sing", "Magic"], ["Sing", "Dance"],
                        ["Dance", "Act", "Code"], ["Act", "Code"]]

    Hire4Show(Candidates, CandidateTalents, Talents)
