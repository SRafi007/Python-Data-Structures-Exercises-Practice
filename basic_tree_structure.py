class TreeNode: #TreeNode class represents a node in the tree
    def __init__(self, value):
        self.value=value        #Each node has a value and a list of children
        self.children = []

    def add_child(self, child_node):#Adds a child node to the current node's list of children
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children = [child for child in self.children if child != child_node]

    def traverse_tree(self):
        print(self.value)
        for child in self.children:
            child.traverse_tree()

#By wrapping code inside the if __name__ == "__main__": block, you ensure that this code only runs when the script is executed directly
if __name__=="__main__":

    root =TreeNode("r")    #creating a new node
    child1=TreeNode("c1")   #creating a new node
    child2=TreeNode("c2")   #creating a new node


    root.add_child(child1)  #adding child1 & child2 as children of root node
    root.add_child(child2)

    grandchild1= TreeNode("gc1")    #creating a new node

    child2.add_child(grandchild1)

    root.traverse_tree()