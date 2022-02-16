class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return self.username



class Users:
    def __init__(self):
        self.user_list = []

    def insert(self, user):
        if type(user) != User:
            raise ValueError("the user must be of the right class")

        self.user_list.append(user)

    def search(self, username):
        if type(username) != str:
            raise ValueError("the username must be a string")

        for user in self.user_list:
            if user.username == username:
                return user

    def update(self, username, attribute, value):
        if type(username) != str or type(value) != str:
            raise ValueError("the username and the new value must be a string")
        if attribute not in ["username", "users", "email"]:
            raise ValueError("the user has only three attributes: username,"
                             " users, email. Please check your spelling")
        user = self.search(username)
        setattr(user, attribute, value)

    def list(self):
        sorted_list = sorted(self.user_list, key=lambda x: x.username)
        return sorted_list


users = Users()

gide = User("ClGide", "Gide", "gide81")
luca = User("AyloSrd", "Luca", "lucamarongiu")
amy = User("iciamyplant", "Emma", "iciamyplant")


users.insert(gide)
users.insert(luca)
users.insert(amy)
users.update('AyloSrd', 'email', 'lucamarongiu@hotmail.com')

result = users.list()
mails = [i.email for i in result]
#print(mails)


"""So this is the brute force solution. Now, let's try to understand bst.
Below is a simple binary tree. Of course, this way of inserting elements
won't scale."""


class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


tree0 = TreeNode(2)

tree_left = TreeNode(3)
tree_left_left = TreeNode(1)

tree_right = TreeNode(5)
tree_right_right = TreeNode(7)
tree_right_right_right = TreeNode(8)
tree_right_right_left = TreeNode(6)
tree_right_left = TreeNode(3)
tree_right_left_right = TreeNode(4)

tree0.left = tree_left
tree_left.left = tree_left_left

tree0.right = tree_right
tree_right.right = tree_right_right
tree_right_right.right = tree_right_right_right
tree_right_right.left = tree_right_right_left
tree_right.left = tree_right_left
tree_right_left.right = tree_right_left_right

#print(tree0.left.key)

"""Let's do the same with a helper function"""

simple_tree = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))


def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        return
    elif isinstance(data, int):
        return TreeNode(data)
    return node

res = parse_tuple(simple_tree)
print(res.left.right)

def parse_tree():
    pass


"""let's copy this func to check if our parse_tree is doing the job right"""


def display_keys(node, space='\t', level=0):
    if node is None:
        print(space*level + 'o')
        return
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left, space, level+1)


def traverse_in_order(node):
    if node is None:
        return []
    return (traverse_in_order(node.left),
            [node.key],
            traverse_in_order(node.right))

# (1) Complete the parse_tuple function above.
# (2) write the postorder and the preorder. (3) Also, write a func calc
# a binary tree's depth. As a hint, that's how you calc it's size.
# (4) try to calc it's diameter. Finally, encapsulate all the data and func
# with parse_tuple as a static method.


def tree_size(tree):
    if tree is None:
        return 0
    return 1 + tree_size(tree.left) + tree_size(tree.right)
