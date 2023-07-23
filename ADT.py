class BNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left, self.right = None, None
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __str__(self):
        val, node_value = self.value, lambda x: x.value if x else "NA"
        left, right = node_value(self.left), node_value(self.right)
        return f"(BNode: value={val}, left={left}, right={right})"


class BST:
    def __init__(self) -> None:
        self.head: BNode|None = None

    def create_tree(self, array: list):
        for x in array: self.add(x)
        return self 

    def add(self, value):
        value, head = BNode(value), self.head
        if head: self._add(head, value) 
        else: self.head = value
        return self

    def _add(self, current: BNode, value:BNode):
        if value > current:
            if not current.right: current.right = value
            else: self._add(current.right, value)
        else: 
            if not current.left: current.left = value
            else: self._add(current.left, value)
                
    def inorder(self)->list:
        result = []
        if not self.head: return result
        return self._inorder(self.head, result)
    
    def _inorder(self, current: BNode, acc: list):
        if current.left: self._inorder(current.left, acc)
        acc.append(current.value)
        if current.right: self._inorder(current.right, acc)
        return acc

    def _preorder(self, current: BNode, acc: list):
        acc.append(current.value)
        if current.left: self._preorder(current.left, acc)
        if current.right: self._preorder(current.right, acc)
        return acc

    def _postorder(self, current: BNode, acc: list):
        if current.left: self._postorder(current.left, acc)
        if current.right: self._postorder(current.right, acc)
        acc.append(current.value)
        return acc