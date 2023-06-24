class BNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left, self.right = None, None
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __str__(self):
        val, left, right = self.value, self.left, self.right
        if left: left = left.value
        if right: right = right.value 
        return f"(BNode: value={val}, left={left}, right={right})"


def add_rec(current: BNode, value:BNode):
    if value > current:
        if not current.right: current.right = value
        else: add_rec(current.right, value)
    else: 
        if not current.left: current.left = value
        else: add_rec(current.left, value)

def inorder_rec(current: BNode, acc: list):
    if current.left: inorder_rec(current.left, acc)
    acc.append(current.value)
    if current.right: inorder_rec(current.right, acc)
    return acc


class BST:
    def __init__(self) -> None:
        self.head: BNode|None = None

    def add(self, value):
        value, head = BNode(value), self.head
        if head: add_rec(head, value) 
        else: self.head = value
        return self
    
    def create_tree(self, array: list):
        for x in array: self.add(x)
        return self 
    
    def inorder(self)->list:
        result = []
        if not self.head: return result
        return inorder_rec(self.head, result)