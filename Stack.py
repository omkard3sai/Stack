from Node import Node


class Stack:

    def __init__(self):
        self.top = None

    def push(self, item):
        insert = Node(item)
        if self.empty_status():
            insert.below = None
            self.top = insert
        else:
            insert.below = self.top
            self.top = insert
        return True

    def pop(self):
        if not self.empty_status():
            pop_data = self.top.data
            self.top = self.top.below
            return pop_data
        else:
            return False

    def peek(self):
        if not self.empty_status():
            return self.top.data
        else:
            return False

    def empty_status(self):
        if self.top is None:
            return True
        else:
            return False

    def print(self):
        stack = self.top
        print("Top/Push/Pop", end=" -> ")
        while stack:
            print(stack.data, end=" -> ")
            stack = stack.below
        print("Bottom")
