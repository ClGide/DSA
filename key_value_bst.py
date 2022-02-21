from bst import User, is_bst


class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None  # useful for upwards traversals

    def __repr__(self):
        return f"instance of BSTNode." \
               f" key: {self.key}" \

    def __str__(self):
        return self.__repr__()


aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

tree = BSTNode("jadhesh", jadhesh)
tree.left = BSTNode("biraj", biraj)
tree.right = BSTNode("sonaksh", sonaksh)
tree.left.parent = tree
tree.right.parent = tree

tree.left.left = BSTNode("aakash", aakash)
tree.left.right = BSTNode("hemanth", hemanth)
tree.left.left.parent = tree.left
tree.left.right.parent = tree.left

tree.right.right = BSTNode("vishal", vishal)
tree.right.left = BSTNode("siddhant", siddhant)
tree.right.left.parent = tree.right
tree.right.right.parent = tree.right

res = is_bst(tree)


def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node


tests = {
    "test1": (tree, "Tozzi", User("Tozzi", "Alessandro Tozzi", "alessandrotozzi1996@gmail.com")),
    "test2": (tree, "Camille", User("Camille", "Camille Kopecky", "camille@kopecky.fr"))
}

insert(*tests["test1"])

print("\n", tree)