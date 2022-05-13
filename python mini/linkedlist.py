''' linked lists '''
class Node(object):
    def __init__(self, value = None, pointer = None):
        self.value = value
        self.pointer = pointer

    def getData(self):
        return self.value

    def getNext(self):
        return self.pointer

    def setData(self, newdata):
        self.value = newdata

    def setNext(self, newpointer):
        self.pointer = newpointer

if __name__ == "__main__":
    l = Node("a", Node("b", Node("c", Node("d"))))

    # assert pointer points to 'c
    assert(l.pointer.pointer.value == 'c')

    print(l.getData())
    print(l.getNext().getData())

    l.setData('aa')
    l.setNext(Node('e'))

    print(l.getData())
    print(l.getNext().getData())