from typing import Tuple


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

#result = users.list()
#mails = [i.email for i in result]
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


#res = parse_tuple(simple_tree)
#print(res.left.right)


def parse_tree(tree, recursion=0):
    print(f"recursion : {recursion}")
    if not isinstance(tree, TreeNode):
        raise TypeError("we prolly need to get to bis solution")

    recursion += 1
    if tree.left is None and isinstance(tree.right, TreeNode):
        return None, tree.key, parse_tree(tree.right, recursion)
    elif tree.right is None and isinstance(tree.left, TreeNode):
        return parse_tree(tree.left, recursion), tree.key, None
    elif not (tree.left is None and tree.right is None):
        return parse_tree(tree.left, recursion), tree.key, parse_tree(tree.right, recursion)
    elif tree.left is None and tree.right is None:
        return tree.key


#res = parse_tree(tree0)
#print(res)


def parse_tree_bis(tree: TreeNode):
    if tree is None:
        return
    elif not (tree.left is None and tree.right is None):
        return parse_tree_bis(tree.left), tree.key, parse_tree_bis(tree.right)
    else:
        return tree.key


#res = parse_tree_bis(tree0)
#print(res)



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


def traverse_inorder(node):
    if node is None:
        return
    return (traverse_inorder(node.left),
            node.key,
            traverse_inorder(node.right))


def traverse_preorder(node):
    if node is None:
        return
    return (node.key,
            traverse_preorder(node.left),
            traverse_preorder(node.right))


def traverse_postorder(node):
    if node is None:
        return
    return(traverse_postorder(node.left),
           traverse_postorder(node.right),
           node.key)


res_inorder = traverse_inorder(tree_right)
res_preorder = traverse_preorder(tree_right)
res_postorder = traverse_postorder(tree_right)

#print(str(res_inorder)+"\n"+str(res_preorder)+"\n"+str(res_postorder))


# (1) Complete the parse_tuple function above. DONE
# (2) write the postorder and the preorder. DONE (3) Also, write a func calc
# a binary tree's depth. As a hint, that's how you calc it's size. DONE

def tree_size(tree):
    if tree is None:
        return 0
    return 1 + tree_size(tree.left) + tree_size(tree.right)


def tree_depth(tree):
    if tree is None:
        return 0
    return 1 + max(tree_depth(tree.left), tree_depth(tree.right))


tests = {
    "test1": {
        "input": (3, 1, 4),
        "output": False
    },
    "test2": {
        "input": (10, 12, (0, 13, 15)),
        "output": False
    },
    "test3": {
        "input": ((1, 3, 4), 10, (None, 17, (None, 18, 19))),
        "output": True
    }
}

def remove_none(nums):
    return [x for x in nums if x is not None]


def check_bst(node: TreeNode, bst=True, max_left=None, min_right=None):
    if node is None:
        return True
    elif bst is False:
        print(bst)
        return False
    else:
        if max_left is None or node.key < max_left.key:
            left = check_bst(node.left, True, max_left=node.key, min_right=None)
        else:
            return check_bst(TreeNode(1), bst=False)

        if min_right is None or node.key > min_right.key:
            right = check_bst(node.right, True, max_left=None, min_right=node.key)
        else:
            return check_bst(TreeNode(1), bst=False)
    return any([left, right])


tree1 = parse_tuple(tests["test1"]["input"])
res = check_bst(tree1)
print(res)

"""
Below's the right way to solve the problem. 
The question then becomes can I check if a binary tree is a bst w/o calc the
min and the max values ? It seems that no. It seems inherent to the solution.  

Now, second question, (a) can I write a function that won't 
need to systematically go as down as the None nodes ? 
Or that (b) would stop going down when a False value is detected ?
Let's separate the two questions.

(a) is not always possible since some nodes only have one child. Therefore, if
I only check on both subtrees is node.left and node.right are None, an error 
would be triggered since None has no left and right attributes. 
Thus, best I can do is check for both conditions : if a node has no children 
AND if the node is None. Is that more efficient ? that's a third question (c).

(b) The problem is that we first recursively get as down as the leaves AND ONLY
THEN start to check if each subtree is itself a bst. In other words, the only
base condition is a Node being None. What we want, is having three base 
conditions. 
_The first is Node being None. 
_The second is the subtree NOT being a bst. 
_The third is the Node being a leaf. 
I think that's the right order to avoid any errors. 
Given that after I detected the first False, the goal is to ONLY propagate the 
info up through the calls, checking if the binary tree is a bst comes down to 
recursively checking two conditions =>
_Is max_left < node.key ? 
_Is min_right > node.key ? 
If the two conditions are met, we go down on both sides. If they aren't met, in the next
call, the third base condition should be triggered. NOW comes the real problem. 
There are two parallel calls and the third base conditions will be triggered in only 
one of them. The other parallel call is like another universe. Can we travel to it ?
Not needed, we can let it go until it's own base condition. 

NOW, the above function should work if I could modify the default value arg. I'll read 
about default values and recursion tommorow. 
N.B: it would be a naive solution. If 10 is at depth 1 and 12 at depth 3 
rightly placed in the left subtree of 10, the tree wouldn't be a bst but the function
would return True.     
"""


def is_bst(node):
    if node is None:
        return True, None, None

    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    is_bst_node = (is_bst_l and is_bst_r and (max_l is None
                   or node.key > max_l) and
                   (min_r is None or node.key < min_r))

    min_key = min(remove_none(min_l, node.key, min_r))
    max_key = max(remove_none((max_l, node.key, max_r)))

    return is_bst_node, min_key, max_key
