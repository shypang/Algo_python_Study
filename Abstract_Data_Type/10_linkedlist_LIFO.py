from node import Node


class LinkedListLIFO(object):
    def __init__(self):
        self.head = None
        self.length = 0

    # 헤드부터 각 노드의 값을 출력한다.
    def _printList(self):
        node = self.head
        while node:
            print(node.value,end=" ")
            node = node.pointer
        print()
    
    #이전 노드(prev)를 기반으로 노드(node)를 삭제한다.
    def _delete(self,prev, node):
        self.length -= 1
        if not prev:
            self.head = node.pointer
        else:
            prev.pointer = node.pointer

    # 새 노드를 추가한다. 다음 노드로 헤드를 가리키고, 헤드는 새 노드를 가리킨다.
    def _add(self, value):
        self.length += 1
        self.head = Node(value, self.head)
    
    #인덱스로 노드를 찾는다.
    def _find(self,index):
        prev = None
        node =self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.pointer
            i +=1
        return node, prev,i

    #값으로 노드를 찾는다.
    def _find_by_value(self,value):
        prev = None
        node = self.head
        found = False
        while node and not found:
            if node.value == value:
                found = True
            else:
                prev = node
                node = node.pointer
        return node,prev,found
    
    #인덱스에 해당하는 노드를 찾아서 삭제한다.
    