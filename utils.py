"""
Utility file.

"""
samples = 60

def pairwise(it):
    i = 0
    for i in range(len(it) - 1):
        yield it[i], it[i + 1]

def eud_dist(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def gen_line(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2

    dx = (x2 - x1)/samples
    dy = (y2 - y1)/samples

    return [(int(x1 + (i*dx)), int(y1 + (i*dy))) for i in range(samples)]