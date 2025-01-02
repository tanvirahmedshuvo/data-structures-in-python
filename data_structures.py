# #Big O notation

# numbers = [3,6,2,4,3,6,8,9]

# # for i in range(len(numbers)):
# #     for j in range(i+1, len(numbers)):
# #         if numbers[i] == numbers[j]:
# #             print(numbers[i], "is a duplicate")
# #             break

# #  Array
# #linked list

# class Node:
#     def __init__(self,data = None, next = None):
#         self.data = data
#         self.next = next

# class Linkedlist:
#     def __init__(self):
#         self.head = None
    
#     def insert_at_the_begining(self,data):
#         node = Node(data, self.head)
#         self.head = node
    
#     def print(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return
        
#         itr = self.head
#         llist = " "
#         while itr:
#             llist += str(itr.data) + '-->'
#             itr = itr.next
#         print(llist)
    
#     def insert_at_end(self,data):
#         if self.head is None:
#             self.head = None(data, None)
#             return
        
#         itr = self.head
#         while itr.next:
#             itr = itr.next
        
#         itr.next = Node(data, None)
#     def insert_values(self, data_list):
#         self.head = None
#         for data in data_list:
#             self.insert_at_end(data)

# if __name__ == '__main__':
#     ll = Linkedlist()
#     # ll.insert_at_the_begining(5)
#     # ll.insert_at_the_begining(89)
#     # ll.insert_at_end(109)
#     ll.insert_values(["banana", "mango", "grapes", "orange"])
#     ll.print()


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at(1,"blueberry")
    ll.remove_at(2)
    ll.print()

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print()