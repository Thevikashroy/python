# convert the array to linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList :
    def generateList(self,arr):
        head = None
        temp = None
        for e in arr:
            if head == None:
                head = Node(e)
                temp = head 
            else:
                temp.next = Node(e)
                temp = temp.next
        return head
    
# print linked list

    def printList(self,head):
        while head is not None:
            print(head.data, end=" ")
            head = head.next
        print()

# reverse list in linkedlist

    def reverseList(self,head):
        st = []
        temp = head
        while temp is not None:
            st.append(temp.data)
            temp = temp.next
        temp = head
        while temp is not None:
            temp.data = st.pop()
            temp = temp.next
        return head
    

    
# palindrome or not
    def isPalindrome(self,head):
       st = []
       temp = head
       while temp is not None:
           st.append(temp.data)
           temp = temp.next
           
        
           
       




def main():
    arr = [1, 2, 3, 4, 5]
    myListOperator = LinkedList()
    head = myListOperator.generateList(arr)
    myListOperator.printList(head)
    head = myListOperator.reverseList(head)
    myListOperator.printList(head)

main()
