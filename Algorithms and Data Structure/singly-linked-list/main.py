class SList:
    # Initialize empty list
    def __init__(self):
        self.head = None
        
    # Add a node to the front
    def add_to_front(self, val): 
        new_head = SLNode(val)
        new_head.next = self.head
        self.head = new_head
        return self
    
    # Get the last node in the list
    def get_last_node(self):
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        return runner
    
    # Add a node to the end
    def add_to_back(self, val): 
        new_node = SLNode(val) 
        runner = self.get_last_node()
        runner.next = new_node
        return self
    
    # Remove the first node
    def remove_from_front(self):
        self.head = self.head.next
        return self
        
    # Remove the last node
    def remove_from_back(self):
        if self.head.next is None:
            self.head = None 
            return self
        runner = self.head
        while runner.next.next is not None:
            runner = runner.next
        runner.next = None
        return self
    
    # Remove node by value
    def remove_val(self, val):
        if self.head.value == val:
            self.head = self.head.next 
            return self
        runner = self.head
        while runner.next is not None:
            if(runner.next.value == val):
                runner.next = runner.next.next
                return self
            runner = runner.next
        return self
    
    # Insert node at index n
    def insert_at(self, val, n):
        new_node = SLNode(val)
        if n == 0:
            self.add_to_front(val)
            return self
        
        runner = self.head
        index = 0
        while runner is not None and index < n - 1:
            runner = runner.next
            index += 1
            
        if runner is None:
            return self
        
        new_node.next = runner.next
        runner.next = new_node
        return self

    # Print all values in the list
    def print_values(self):
        runner = self.head
        while(runner != None):
            print(runner.value)
            runner = runner.next
        return self

  
class SLNode:
    # Node structure (value + next pointer)
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
        
my_list = SList()    # create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").insert_at("test" , 1).print_values()    # chaining, yeah!
# output should be:
# Linked lists
# are
# fun!