class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            #add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        
        else:
            #add data in the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []
        
        #Visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        
        #visit base node
        elements.append(self.data)
        #visit right tree
        if self.right:
            elements += self.right.in_order_traversal()
            
        return elements
    
    def search(self, val):
        if self.data ==  val:
            return True
        
        elif val < self.data :
           #val might be in the left subtree 
           if self.left:
              return self.left.search(val)
           else:
              return False 
        
        elif val > self.data:
            # val might be in right subtree
            if self.right:
              return self.right.search(val)
            else:
                return False
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    
    def delete(self,val):
        if val < self.data:
            if self.left:
               self.left = self.left.delete(val)
        elif val> self.data:
            if self.right:
               self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self   
    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0]) 
    
    for i in range(1, len(elements)):  
        root.add_child(elements[i])
    
    return root

if __name__ == '__main__':
    number = [17,4,1,20,9,23,18,34,60,18,4]
    numbers_tree = build_tree(number)
    print(numbers_tree.in_order_traversal())
    numbers_tree.delete(20)
    print(numbers_tree.in_order_traversal())
    numbers_tree.delete(9)
    print(numbers_tree.in_order_traversal())
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))
    
    print(country_tree.in_order_traversal())

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    
    
                    