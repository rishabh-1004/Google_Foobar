from fractions import Fraction  
def solution(pegs):
    arrLength = len(pegs)
    if ((not pegs) or arrLength == 1):
        return [-1,-1]

    even = True if (arrLength % 2 == 0) else False
    sum = (- pegs[0] + pegs[arrLength - 1]) if even else (- pegs[0] - pegs[arrLength -1])

    if (arrLength > 2):
        for index in xrange(1, arrLength-1):
            sum += 2 * (-1)**(index+1) * pegs[index]

    GearRadius = Fraction(2 * (float(sum)/3 if even else sum)).limit_denominator()

    if GearRadius < 2:
        return [-1,-1]

    currentRadius = GearRadius
    for index in xrange(0, arrLength-2):
        CenterDistance = pegs[index+1] - pegs[index]
        NewRadius = CenterDistance - currentRadius
        if (currentRadius < 1 or NewRadius < 1):
            return [-1,-1]
        else:
            currentRadius = NewRadius

    return [GearRadius.numerator, GearRadius.denominator]

print(solution([4,17,50]))