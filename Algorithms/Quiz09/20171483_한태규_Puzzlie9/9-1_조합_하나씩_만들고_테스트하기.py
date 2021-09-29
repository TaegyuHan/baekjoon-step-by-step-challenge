
def Good(Comb: list, candList: list, candTalents: list, AllTalents: list) -> bool:
    for tal in AllTalents:
        cover = False
        for cand in Comb:
            candTal = candTalents[candList.index(cand)]
            if tal in candTal:
                cover = True
        if not cover:
            return False
    
    return True


def Hire4Show(candList: list,candTalents: list, talentList: list):
    n = len(candList)
    hire = candList[:]

    for i in range(2**n):
        Combination = []
        num = i
        for j in range(n):
            if (num % 2 == 1):
                Combination = [candList[n-1-j]] + Combination
            num = num // 2
        if Good(Combination, candList, candTalents, talentList):
            if len(hire) > len(Combination):
              hire = Combination
    
    print("Optimum Solution: ", hire)


if __name__ == '__main__':

    Talents = ["Sing", "Dance", "Magic", "Act", "Flex", "Code"]
    Candidates = ["Aly", "Bob", "Cal", "Don", "Eve", "Fay"]
    CandidateTalents = [["Flex", "Code"], ["Dance", "Magic"],
                        ["Sing", "Magic"], ["Sing", "Dance"],
                        ["Dance", "Act", "Code"], ["Act", "Code"]]

    ShowTalent2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    CandidateList2 = ["A", "B", "C", "D", "E", "F", "G"]
    CandToTalents2 = [[4, 5, 7], [1, 2, 8], [2, 4, 6, 9],
                      [3, 6, 9], [2, 3, 9], [7, 8, 9],
                      [1, 3, 7]]

    Hire4Show(Candidates, CandidateTalents, Talents)
    Hire4Show(CandidateList2, CandToTalents2, ShowTalent2)
