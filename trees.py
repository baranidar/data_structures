class Tree:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level
    
    def print_tree(self):
        space = "  " * self.get_level() + "|__"
        print(space + self.data)
        for child in self.children:
            child.print_tree()

root = Tree("Healthy Food")

fruits = Tree("Fruits")
root.add_child(fruits)
fruits.add_child(Tree("Apple"))
fruits.add_child(Tree("Orange"))

vegetables = Tree("Vegetables")
root.add_child(vegetables)
vegetables.add_child(Tree("Carrot"))
vegetables.add_child(Tree("Beetss"))

juices = Tree("Juices")
root.add_child(juices)
juices.add_child(Tree("OJ"))
juices.add_child(Tree("Pineapple"))

root.print_tree()
print("--------------------------")
fruits.print_tree()
print("--------------------------")
vegetables.print_tree()
print("--------------------------")
juices.print_tree()
