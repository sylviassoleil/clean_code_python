class Node:
    def __init__(self, val=None):
        self.val: int = val
        self.left: Node = None  # Node()
        self.right: Node = None  # Node()


class BTree:
    def __init__(self):
        self.root = None

    def insert_val(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val > current.val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                elif val < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break

    # @property
    def create_tree(self, values: list):
        for i in values:
            self.insert_val(i)


# A = 0


def compare_2_trees(tree_0, tree_1):
    if (not tree_0) and (not tree_1):
        return True
    if (not tree_0) or (not tree_1) or (tree_0.val != tree_1.val):
        return False
    # if tree_0.val != tree_1.val:
    #     return False

    return compare_2_trees(tree_0.left, tree_1.left) & compare_2_trees(
        tree_0.right, tree_1.right)


if __name__ == '__main__':
    pass
    # global A
    # nonlocal A
    A = 5
    vals1 = [1, 3, 4, 2, 5]
    vals0 = [1, 3, 4, 2, 0]
    t0 = BTree()
    t0.create_tree(vals0)

    t1 = BTree()
    t1.create_tree(vals1)
    is_same = compare_2_trees(t0.root, t1.root)
