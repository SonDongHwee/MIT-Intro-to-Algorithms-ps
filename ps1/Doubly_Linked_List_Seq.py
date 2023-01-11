class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        if(self.head==None):
            self.head = Doubly_Linked_List_Node(x)
            self.tail = self.head
        else:
            node = Doubly_Linked_List_Node(x)
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insert_last(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        if(self.tail==None):
            self.tail = Doubly_Linked_List_Node(x)
            self.head = self.tail
        else:
            node = Doubly_Linked_List_Node(x)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def delete_first(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        x = self.head
        if(x==None):
            return None
        elif(x.next==None):
            self.head = None
            self.tail = None
            return x.item
        else:
            self.head = self.head.next
            self.head.prev = None
            return x.item

    def delete_last(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        x = self.tail
        if(x==None):
            return None
        elif(x.prev==None):
            self.tail = None
            self.head = None
            return x.item
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            return x.item

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ###########################
        # Part (b): Implement me! # 
        ###########################
        L2 = Doubly_Linked_List_Seq()
        L2.head = x1
        L2.tail = x2
        if x1 == self.head: 
            self.head = x2.next
        else:   
            x1.prev.next = x2.next
        if x2 == self.tail: 
            self.tail = x1.prev
        else: 
            x2.next.prev = x1.prev
        x1.prev = None
        x2.next = None
        return L2

    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! # 
        ###########################
        xn = x.next
        x1 = L2.head
        x2 = L2.tail
        L2.head = None
        L2.tail = None
        x1.prev = x
        x.next = x1
        x2.next = xn
        if xn:  
            xn.prev = x2
        else:   
            self.tail = x2

# L = Doubly_Linked_List_Seq()
# L.insert_first(1)
# L.insert_last(2)
# y = L.delete_first()
# x = L.delete_last()
# for i in L:
#     print(i)
# #print(x)
# l = [1,2,3,4,5,6,7,8,9]
# for i in l:
#     L.insert_first(i)
# for i in L:
#     print(i)
# L2 = Doubly_Linked_List_Seq()
# for i in l:
#     L2.insert_last(i)
# for i in L2:
#     print(i)
# L.splice(L.tail.prev.prev,L2)
# print("--------")
# for i in L:
#     print(i)
# print(L2.head==None and L2.tail ==None)