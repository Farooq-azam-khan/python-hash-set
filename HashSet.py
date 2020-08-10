class MyHashSet:
    def __init__(self, bucket_len=10):
        self.buckets = [] 
        for i in range(bucket_len):
            self.buckets.append(Node())
        self.current_size = 0 
    
    def add(self, value):
        h = hash(value)
        if (h < 0):
            h = -h 
        h = h % len(self.buckets)
        current_node = self.buckets[h]
        while (current_node != None):
            if current_node.data == value:
                return False 
            current_node = current_node.next_node 
        new_node = Node(value)
        new_node.next_node = self.buckets[h]
        self.buckets[h] = new_node
        self.current_size+=1
        return True 
        
    
    def contains(self, value):
        h = hash(value)
        if h<0:
            h = -h 
        h = h % len(self.buckets)
        current = self.buckets[h]
        while (current!=None):
            if current.data == value:
                return True 
            current = current.next_node 
        return False 
    
    def remove(self, value):
        h = hash(value)
        if h<0:
            h = -h 
        h = h % len(self.buckets)
        current_node = self.buckets[h]
        previous_node = None 
        while current_node != None: 
            if current_node.data == value: 
                if previous_node == None: 
                    self.buckets[h] = current_node.next_node
                else:
                    previous_node.next_node = current_node.next_node
                self.current_size -= 1 
                return True 
            previous_node = current_node
            current_node = current_node.next_node 
        return False 
        

class Node: 
    def __init__(self, data=None, next_node=None):
        self.data = data 
        self.next_node = next_node

    def __str__(self):
        if self.next_node == None:
            return f'Node({self.data})'
        return f'Node({self.data}, {self.next_node.__str__()})'

    def __repr__(self):
        return self.__str__()

def main():
    hashSet = MyHashSet()
    print('added 1:', hashSet.add(1))
    print('added 2:', hashSet.add(2)) 
    
    print('contians 1:', hashSet.contains(1))
    print('contains 3:', hashSet.contains(3))
    # print('added 2:', hashSet.add(2))
    print('contians 2:', hashSet.contains(2))
    print('remove 2:', hashSet.remove(2))
    print('contains 2:', hashSet.contains(2)) 

if __name__ == '__main__':
    main() 