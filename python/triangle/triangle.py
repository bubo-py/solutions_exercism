def equilateral(sides):
    if is_triangle(sides):
        return all(x == sides[0] for x in sides[1:])
    else:
        return False


def isosceles(sides):
    if is_triangle(sides):
        return len(sides) != len(set(sides))
    else:
        return False


def scalene(sides):
    if is_triangle(sides):
        return all(x != sides[0] for x in sides[1:])
    else:
        return False


def is_triangle(values):
    if sum(values) != 0:
        if (values[0] <= values[1] + values[2] and
            values[2] <= values[1] + values[0] and
            values[1] <= values[2] + values[0]):
            return True
        else:
            return False
