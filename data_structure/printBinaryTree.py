class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def preOrder(root):
    pre_order_list = []
    def traverse_preorder(rt):
        if rt is not None:
            pre_order_list.append(str(rt))
            traverse_preorder(rt.left)
            traverse_preorder(rt.right)

        return pre_order_list
    print(' '.join(traverse_preorder(root)))

    # traverse_preorder(root)
    # print(' '.join(pre_order_list))
def inOrder(root):
    inorder_list = []
    def get_inorder_list(root):
        if root is not None:
            get_inorder_list(root.left)
            inorder_list.append(root.info)
            get_inorder_list(root.right)
        return inorder_list
    return get_inorder_list(root)

def postOrder(root):
    post_order_list = []
    def get_post_order_list(root):
        if root is not None:
            get_post_order_list(root.left)
            get_post_order_list(root.right)
            post_order_list.append(root.info)
        return post_order_list
    return get_post_order_list(root)


class Node:
    def __init__(self, val):
        self.info = val
        self.left = None
        self.right = None
        self.level = None

class BinarySearch:
    def __init__(self):
        self.root = None

    def create_tree(self, arr):
        if len(arr)<1:
            return
        current_value = arr[0]
        if self.root:
            self.root = Node(current_value)
        # current_node = self.root

        for i in range(1, len(arr)):
            current_node = self.root
            while 1:
                current_value = current_node.value
                if arr[i]<current_value:
    #                 do something
                    if current_node.left is not None:
                        current_node = current_node.left
                    else:
                        current_node.left = Node(arr[i])
                        break

                elif arr[i]>current_value:
                    if current_node.right is not None:
                        current_node = current_node.right
                    else:
                        current_node.right = Node(arr[i])
                        break

                else:
                    break



if __name__ == '__main__':
    pass
