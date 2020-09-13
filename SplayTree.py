from random import randrange


class SplayTreeNode:
    def __init__(self, data):
        self.parent = None
        self.data = data
        self.left = None
        self.right = None


class SplayTree:
    def __init__(self):
        self.root = None

    def zig(self,splay_node):
        temp = splay_node.left
        splay_node.left = temp.right

        if temp.right is not None:
            temp.right.parent = splay_node
        temp.parent = splay_node.parent

        if splay_node.parent is None:
            self.root = temp
        elif splay_node == splay_node.parent.right:
            splay_node.parent.right = temp
        else:
            splay_node.parent.left = temp
        temp.right = splay_node
        splay_node.parent = temp

    def zag(self,splay_node):
        temp = splay_node.right
        splay_node.right = temp.left

        if temp.left is not None:
            temp.left.parent = splay_node

        temp.parent = splay_node.parent

        if splay_node.parent is None:
            self.root = temp
        elif splay_node.parent.left == splay_node:
            splay_node.parent.left = temp
        else:
            splay_node.parent.right = temp

        temp.left = splay_node
        splay_node.parent = temp

    def splay_tree(self,splay_node):
        while splay_node.parent is not None:
            if splay_node.parent == self.root: #splay_node is child of root
                if splay_node == splay_node.parent.left:
                    self.zig(splay_node.parent)
                else:
                    self.zag(splay_node.parent)

            else:
                parent_node = splay_node.parent
                grand_parent = parent_node.parent #grandparent

                if(splay_node == splay_node.parent.left) and (parent_node == parent_node.parent.left):
                    self.zig(grand_parent)
                    self.zig(parent_node)
                elif (splay_node == splay_node.parent.right)and (parent_node == parent_node.parent.right):
                    self.zag(grand_parent)
                    self.zag(parent_node)
                elif (splay_node == splay_node.parent.right) and (parent_node == parent_node.parent.left):
                    self.zag(parent_node)
                    self.zig(grand_parent)
                else:
                    self.zig(parent_node)
                    self.zag(grand_parent)

    def insert_node(self, data):
        new_node = SplayTreeNode(data)

        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            q = None
            while temp is not None:
                q = temp
                if new_node.data < temp.data:
                    temp = temp.left
                else:
                    temp = temp.right

            if (q.left is None) and (new_node.data < q.data):
                q.left = new_node
            else:
                q.right = new_node
            new_node.parent = q

            self.splay_tree(new_node)



    def display_inorder(self, temp):
        if temp is not None:
            self.display_inorder(temp.left)
            print(int(temp.data), end=' ')
            self.display_inorder(temp.right)

    def display_preorder(self, temp):
        if temp is not None:
            print(int(temp.data), end=' ')
            self.display_inorder(temp.left)
            self.display_inorder(temp.right)


if __name__ == '__main__':
    splaytree = SplayTree()

    for i in range(5):
        splaytree.insert_node(randrange(10, 100, 3))
        splaytree.display_preorder(splaytree.root)
        print('\n' + str("*" * 20))
        splaytree.display_inorder(splaytree.root)
        print('\n' + str("#" * 20))




