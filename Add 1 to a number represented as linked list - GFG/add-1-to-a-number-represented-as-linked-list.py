#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def revl(self, head):
        prev = None
        cur = head
        while(cur):
            after = cur.next
            cur.next = prev
            prev = cur
            cur = after
        return prev
    def addOne(self,head):
        #Returns new head of linked List.
        head = self.revl(head)
        carry = 0
        temp = head
        prev = None
        temp.data += 1
        while(temp):
            val =temp.data + carry
            temp.data = val%10
            carry = val//10
            prev = temp
            temp = temp.next
        if(carry):
            prev.next = Node(1)
        return self.revl(head)
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

def PrintList(head):
    while head:
        print(head.data,end='')
        head = head.next

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        num = input()
        ll = LinkedList() # create a new linked list 'll1'.
        for digit in num:
            ll.insert(int(digit))  # add to the end of the list
        
        resHead = Solution().addOne(ll.head)
        PrintList(resHead)
        print()


# } Driver Code Ends