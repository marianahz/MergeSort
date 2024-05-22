
def mergesort(mlist):
    if mlist is None:
        return None
    elif len(mlist) <= 1:
        return mlist

    mid = len(mlist) // 2
    left_Half = mlist[:mid]
    right_Half = mlist[mid:]

    left_Sort = mergesort(left_Half)
    right_Sort = mergesort(right_Half)
    return merge(left_Sort, right_Sort)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) or j < len(right):
        if j == len(right) or (i < len(left) and left[i] <= right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result
