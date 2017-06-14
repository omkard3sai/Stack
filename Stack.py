class Stack:

    def __init__(self, size):
        self.stack = list()
        self.size = size

    def push(self, item=20):
        if not self.isfullstatus():
            self.stack.append(item)
            return True
        else:
            return False

    def pop(self):
        if not self.isemptystatus():
            return self.stack.pop()
        else:
            return False

    def peek(self):
        if not self.isemptystatus():
            return self.stack[-1]
        else:
            return False

    def isfullstatus(self):
        if len(self.stack) == self.size:
            return True
        else:
            return False

    def isemptystatus(self):
        if not self.stack:
            return True
        else:
            return False

    def print(self):
        print('->', ','.join(str(a) for a in reversed(self.stack)))
