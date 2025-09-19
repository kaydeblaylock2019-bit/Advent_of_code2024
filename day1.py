
#pair up smallest numbers from left and right list, then second smallest from each list and so on
from typing import List, Tuple

def main():
    lhs, rhs = prep_data()

    total = calc(lhs, rhs)
    print("Part 1:", total)

    total2 = calc2(lhs, rhs)
    print("Part 2:", total2)
    

def prep_data() -> Tuple[List[int], List[int]]:
    file = open("real.txt", "r")
    content = file.read()
    file.close()

    lhs = []
    rhs = []

    for row in content.splitlines():    
        for idx, column in enumerate(row.split(" ")):
            if not column == "":
                if idx == 0:
                    lhs.append(column)
                else:
                    rhs.append(column)
    return (lhs,rhs)

#calculate distance from the numbers, ex. 3 and 7 distance = 4, 9 and 3 distance = 6
def calc(lhs=List[int], rhs=List[int]) -> int:
    lhs.sort()
    rhs.sort()
    
    total = 0
    for idx, ln in enumerate(lhs):
        distance = abs(int(ln) - int(rhs[idx]))
        total += distance

    return total

#find total distance between both lists ex. 4 + 6 = 10
def calc2(lhs=List[int], rhs=List[int]) -> int:

    total = 0
    for ln in lhs:
        counter = 0
        for rn in rhs:
            if ln == rn:
                counter += 1
        total += int(ln) * counter


    return total

if __name__ == "__main__":
    main()