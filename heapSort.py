class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
    
    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.Heapify_up(self.current_size)

    # Bottom to Top
    def Heapify_up(self, i):
        # Root node napugunjel run hunxa
        while i // 2 > 0:
            # Child parent vanda sano xa vane swap garxa
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i//2],self.heap_list[i]=self.heap_list[i],self.heap_list[i//2]
            # Parent node ko index ma janxa
            i = i // 2
    
    # Top to Bottom
    def Heapify_down(self, i):
        # Leaf node samma run hunxa
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            # parent minimun child vanda greater xa vane swap garxa
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc]= self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        # Child ko right node exist gardaina vane left node return garxa
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            # Left child right child vanda sano xa vane left ko index return garxa natra right ko index return garxa
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delete_min(self):
        popped = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop(1)
        self.Heapify_down(self.current_size)
        print(popped)

    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while (i > 0):
            self.Heapify_down(i)
            i -= 1

    def printList(self):
        print(self.heap_list)

a = BinHeap()
# a.insert(5)
# a.insert(2)
# a.insert(6)
# a.insert(1)
a.printList()