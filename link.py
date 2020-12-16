class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count = count + 1
            current = current.getNext()

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()

    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self, item):
        current = self.head #first element
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop  = True
            else:
                previous = current
                current =  current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current) # it feels like tieing
            previous.setNext(temp)

def deleteDuplicates(head: ListNode) -> ListNode:
    current = head
    while current != None and current.next != None:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head






def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    while l1 != None and l2 != None:

        if l1.val > l2.val:

            old =  l1.next
            l1.next = l2
            l1.next.next = old

            l1 = l1.next.next
            l2 = l2.next

        else:
            








        return l1

a = ListNode(1)
b = ListNode(2)
c = ListNode(4)
a.next = b
b.next = c

d = ListNode(2)
e = ListNode(3)
g = ListNode(5)
d.next = e
e.next = g


list = mergeTwoLists(a,d)

while list.next != None:
    print(list.val)
    list = list.next
