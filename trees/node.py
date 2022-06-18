class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def search(self, target):
        print(self, target)
        if self.value == target:
            return "Found target"
        elif self.left and (self.value > target):
            return self.left.search(target)
        elif self.right and (self.value < target):
            return self.right.search(target)
        return "Target Not found."

    def traverse_preorder(self):
        print(self)
        if self.left:
            self.left.traverse_preorder()

        if self.right:
            self.right.traverse_preorder()

    def traverse_postorder(self):
        if self.left:
            self.left.traverse_postorder()

        if self.right:
            self.right.traverse_postorder()

        print(self)

    def traverse_inorder(self):
        if self.left:
            self.left.traverse_inorder()

        print(self)

        if self.right:
            self.right.traverse_inorder()

    def height(self, h=0):
        left = self.left.height(h+1) if self.left else h
        right = self.right.height(h+1) if self.right else h
        return max(left, right)

    def __str__(self):
        l = None
        r = None
        if self.left:
            l = self.left.value
        if self.right:
            r = self.right.value
        return "Node {}, left {}, right {}".format(self.value, l, r)


class Tree:
    def __init__(self, root: Node, name: str = "tree"):
        self.root = root
        self.name = name

    def __str__(self):
        if self.root:
            templ = None
            tempr = None

            if self.root.left:
                templ = Tree(self.root.left)
            if self.root.right:
                tempr = Tree(self.root.right)
            return str(self.root) + " --L-- " + str(templ) + " --R-- " + str(tempr) + "\n"

    def search(self, target):
        return self.root.search(target)

    def traverse_preorder(self):
        self.root.traverse_preorder()

    def traverse_postorder(self):
        self.root.traverse_postorder()

    def traverse_inorder(self):
        self.root.traverse_inorder()

    def get_height(self):
        return self.root.height(0)


if __name__ == "__main__":
    n = Node(26)
    n.left = Node(25)
    n.right = Node(33)
    n.right.left = Node(28)
    n.right.left.right = Node(29)
    n.right.right = Node(35)
    print(n.left)
    print(n)

    print("--------------------------------------------------")
    t = Tree(n)
    print(t)

    print("--------------------------------------------------")
    print(t.search(35))

    print("--------------------------------------------------")
    print(t.search(45))

    print("--------------------------------------------------")
    t.traverse_inorder()
    print("--------------------------------------------------")
    t.traverse_preorder()
    print("--------------------------------------------------")
    t.traverse_postorder()
    print("--------------------------------------------------")

    print("height is ", t.get_height())
    print("--------------------------------------------------")

