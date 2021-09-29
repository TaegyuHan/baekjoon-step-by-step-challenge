# -*- coding: utf-8 -*-
"""
    퍼즐로 배우는 알고리즘 with 파이썬
    순천향대학교 빅데이터공학과
    20171483 한태규
    ------------------------- memo -------------------------
    퍼즐 08
    누가 저녁 파티에 오지 않게 될까?
    --------------------------------------------------------
    update : 2021.09.13
"""

# 8-2
# 1. 싫어하는 관계를 우선은 생각하지 말고,
# 저녁 파티에 초대할 수 있는 친구들의 가능한
# 모든 조합을 생성합니다.

# 2. 각 조합에 싫어하는 관계에 있는 친구들이 
# 같이 들어있는지 확인하고, 그렇다면 해당 조합을
# 제거합니다.

# 3. 남아있는 가능한 조합들중 가장 많은 사람이 
# 포함된 조합을 찾습니다.
# 이것이 바로 최선의 결과 입니다.
# 여기에는 같은 수의 친구들을 가진 여러 조합이 있을
# 수 있습니다.



# 8 - 3 모든 조합 생성하기
def Combinations(n, guestList):
    allCombL = []

    # 나올 수 있는 모든 경우의 수 
    # 2^n
    # i : 0 ~ 31
    for i in range(2**n):
      # num 값을 변경하는 연산을 수행해야하기 때문에
      num = i
      cList = []
      
      for j in range(n):
        # i 가 홀수 인 경우
        if num % 2 == 1:
          print("nun : ", num)
          print("j : ", j)
          print("cList1 : ",cList)
          print("guestList[{0} - 1 - {1}] : {2}".format(n, j, guestList[n - 1 - j]))
          cList = [guestList[n - 1 - j]] + cList
          print("cList2 : ", cList)
        num = num//2
        print("nun : ", num)
      allCombL.append(cList)
    
    return allCombL

# 친하지 않는 조합 제거하기
def removeBadCombinations(allCombL, dislikePairs):
    allGoodCombinations = []
    for i in allCombL:
        good = True
        for j in dislikePairs:
            if j[0] in i and j[1] in i:
                good = False
        if good:
            allGoodCombinations.append(i)
    return allGoodCombinations

# 최대 조합 고르기
def InviteDinner(guestList, dislikePairs):
    # 모든 조합 생성
    allCombL = Combinations(len(guestList), guestList)

    # 친하지 않는 조합 제거하기
    allGoodCombinations = \
        removeBadCombinations(allCombL, dislikePairs)

    invite = []
    for i in allGoodCombinations:
        if len(i) > len(invite):
            invite = i

    print("Optimun Solution: ", invite)


if __name__ == '__main__':
    dislikePairs = [['Alice', 'Bob'], ['Alice', 'Eve']]
    questList = ["Alice", "Bob", "Cleo", "Don", "Eve"]
    InviteDinner(questList, dislikePairs)

    LargeDislikes



