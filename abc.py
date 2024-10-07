class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def InsertNodeBeforeValue(head,node):
    #链表头部
    if head.val == node.val:
        node.next = head
        return node
    #链表中间
    cur = head
    while cur.next != None and cur.next.val != node.val:
        cur = cur.next
    #错误处理
    if cur.next == None:
        print("找不到指定元素")
    node.next = cur.next
    cur.next = node

    return head



    return head




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

# 在值为3的节点前插入值为6的节点
node_to_insert = ListNode(3)
head = InsertNodeBeforeValue(head, node_to_insert)

print("插入后的链表:")
print_list(head)
