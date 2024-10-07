class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    new = None
    a = head
    while a:
        b = a.next
        a.next = new
        new = a
        a = b
    return new

def print_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

# 创建链表 1->2->3->4->5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("原始链表:")
print_list(head)

# 翻转链表
head = reverse_list(head)

print("翻转后的链表:")
print_list(head)
