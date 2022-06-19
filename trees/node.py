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

    def is_balanced(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return abs(left_height - right_height) < 2

    def add(self, value):
        print(self, value)
        if self.value == value:
            return None
        elif self.value > value:
            if self.left:
                return self.left.add(value)
            else:
                self.left = Node(value)
        elif self.value < value:
            if self.right:
                return self.right.add(value)
            else:
                self.right = Node(value)
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

    def get_nodes_at_depth(self, depth, nodes=None, print_none=False):
        # print(depth, self, nodes, print_none)
        if nodes is None:
            nodes = []
        if depth == 0:
            nodes.append(self.value)
            return nodes

        if self.left:
            self.left.get_nodes_at_depth(depth-1, nodes, print_none)
        elif print_none:
            nodes.extend([None]*2**(depth-1))

        if self.right:
            self.right.get_nodes_at_depth(depth-1, nodes, print_none)
        elif print_none:
            nodes.extend([None]*2**(depth-1))
        return nodes

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.value

    def delete(self, target, parent=None):
        if self.value == target:
            if self.left and self.right:
                min_value = self.find_min()
                self.value = min_value
                self.right = self.right.delete(min_value)
                return self
            else:
                # No or one child.
                return self.left or self.right
        elif self.left and (self.value > target):
            self.left =  self.left.delete(target, self)
        elif self.right and (self.value < target):
            self.right = self.right.delete(target, self)
        return self

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

    def get_nodes_at_depth(self, depth, print_none):
        return self.root.get_nodes_at_depth(depth, [], print_none)

    def add(self, value):
        self.root.add(value)

    def add_multiple(self, values):
        for value in values:
            self.add(value)

    def _node_to_char(self, n, spacing):
        if n is None:
            return '_'+(' '*spacing)
        spacing = spacing-len(str(n))+1
        return str(n)+(' '*spacing)

    def print(self, label=''):
        print(self.name+' '+label)
        height = self.root.height()
        spacing = 3
        width = int((2**height-1) * (spacing+1) + 1)
        # Root offset
        offset = int((width-1)/2)
        for depth in range(0, height+1):
            if depth > 0:
                # print directional lines
                print(' '*(offset+1)  + (' '*(spacing+2)).join(['/' + (' '*(spacing-2)) + '\\']*(2**(depth-1))))
            row = self.root.get_nodes_at_depth(depth, [])
            print((' '*offset)+''.join([self._node_to_char(n, spacing) for n in row]))
            spacing = offset+1
            offset = int(offset/2) - 1
        print('')

    def delete(self, target):
        self.root = self.root.delete(target)

    def is_balanced(self):
        return self.root.is_balanced()


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

    print("Nodes at depth 2 ", t.get_nodes_at_depth(2, True))
    print("--------------------------------------------------")

    tree = Tree(Node(50))
    tree.add_multiple([25, 75, 45, 35, 89, 90, 91, 100, 23, 45, 45, 78])
    tree.print()

    tree.delete(90)
    tree.print()

    print("--------------------------------------------------")

    print(tree.root.is_balanced())
    print(tree.root.left.is_balanced())

