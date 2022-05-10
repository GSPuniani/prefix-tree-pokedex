import pygraphviz as pgv
import random


class Node:
    insertion_step = []

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addNode(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
                self.printSubtree()
            else:
                self.left.addNode(data)  # recursively calling addNode method
        else:
            if self.right is None:
                self.right = Node(data)
                self.printSubtree()
            else:
                self.right.addNode(data)

    def printSubtree(self):
        if not (self.left is None or self.right is None):
            print self.left.data, self.data, self.right.data
            self.insertion_step.append(
                (self.left.data, self.data, self.right.data))

        elif self.left is None and not self.right is None:
            print None, self.data, self.right.data
            self.insertion_step.append((None, self.data, self.right.data))

        elif not self.left is None and self.right is None:
            print self.left.data, self.data, None
            self.insertion_step.append((self.left.data, self.data, None))

        else:
            print None, self.data, None
            self.insertion_step.append((None, self.data, None))

    def drawTree(self, tree, f):
        print self.insertion_step
        for step in self.insertion_step:
            if not step[0] is None:
                tree.add_node(step[0], color='goldenrod2', style='filled')

            tree.add_node(step[1], color='goldenrod2', style='filled')

            if not step[2] is None:
                tree.add_node(step[2], color='goldenrod2', style='filled')

            if step[0] is None or step[1] is None or step[2] is None:
                tree.add_node('', color='goldenrod1',
                              shape='box', style='filled')

            if not step[0] is None:
                tree.add_edge(step[1], step[0], color='sienna', style='filled')
            else:
                tree.add_edge(step[1], '', color='sienna', style='filled')
            if not step[2] is None:
                tree.add_edge(step[1], step[2], color='sienna', style='filled')
            else:
                tree.add_edge(step[1], '', color='sienna', style='filled')

        tree.write(f)
        img = pgv.AGraph(f)
        img.layout()
        img.draw(f.split('.')[0] + '.pdf')
        img.close()


if __name__ == '__main__':
    lst = [random.randint(1, 10) for i in range(10)]
    print lst
    n = Node(lst[0])
    n.printSubtree()
    for num in lst[1:]:
        n.addNode(num)

    tree = pgv.AGraph(directed=True, strict=True)
    filename = 'tree.dot'
    n.drawTree(tree, filename)
