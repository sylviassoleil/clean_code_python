''' get the max depth of xml '''
# maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    maxdepth = level + 1

    # check childrens of current node
    for child in elem:
        maxdepth = max(maxdepth, depth(child, level+1))

    return maxdepth