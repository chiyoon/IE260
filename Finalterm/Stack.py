class Stack:

    def __init__(self):
        self.length = 0
        self.stack = []

    def push(self, data):
        self.stack.append(data)
        self.length += 1

    def pop(self):
        if self.length != 0:
            data = self.stack.pop()
            self.length -= 1
            return data

    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False