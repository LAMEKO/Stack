class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None


class Stack:
    def __init__(self, value=None):
        self.top = None
        if not value is None:
            self.push(value)

    def __len__(self):
        cur = self.top
        count = 0
        while cur:
            count+=1
            cur = cur.prev
        return count

    def push(self, value):
        node = Node(value)
        if self.top is None:
            self.top = node
        else:
            node.prev = self.top
            self.top = node

    def pop(self):
        if self.top:
            node = self.top
            self.top = self.top.prev
            return node.data
        else:
            return None

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    def __str__(self):
        result = 'Stack('
        cur = self.top
        count = 0
        while cur:
            if count == 0:
                result += str(cur.data)
                count += 1
            else:
                result += ', ' + str(cur.data)
            cur = cur.prev
        result += ')'
        return result

    def __next__(self):
        cur = self.top
        while cur:
            yield cur.data
            cur = cur.prev

    def __iter__(self):
        return self.__next__()

    def __getitem__(self, item):
        cur = self.top
        for i in range(item):
            cur = cur.prev
        return cur.data

    def __copy__(self):
        new = Stack()
        for i in self:
            new.push(i)
        res = Stack()
        for i in new:
            res.push(i)
        return res

    def __reversed__(self):
        res = Stack()
        for i in self:
            res.push(i)
        return res
