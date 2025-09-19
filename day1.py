from typing import List, Tuple

def main():
    lhs, rhs = prep_data()

    total = calc(lhs, rhs)
    print("Part 1:", total)

    total2 = calc2(lhs, rhs)
    print("Part 2:", total2)
    
#Prepping data for calculations
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
                    lhs.append(int(column))
                else:
                    rhs.append(int(column))
    return (lhs,rhs)

def calc(lhs=List[int], rhs=List[int]) -> int:
    lhs.sort()
    rhs.sort()
    
    total = 0
    for idx, ln in enumerate(lhs):
        distance = abs(ln - rhs[idx])
        total += distance

    return total


def calc2(lhs=List[int], rhs=List[int]) -> int:

    total = 0
    for ln in lhs:
        counter = 0
        for rn in rhs:
            if ln == rn:
                counter += 1
        total += ln * counter


    return total

if __name__ == "__main__":
    main()