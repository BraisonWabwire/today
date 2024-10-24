# ****************Part 2****************
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to print a linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()  # Just to move to the next line after printing the list


print("----Part 2----")
# Part 2: Sorting an array (merge sort)
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    
    return merge(left, right)

def merge(left, right):
    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array

# Example usage for sorting an array
nums1 = [5, 2, 3, 1]
sorted_nums1 = merge_sort(nums1)
print("Sorted Array Example 1:")
print(sorted_nums1)

nums2 = [5, 1, 1, 2, 0, 0]
sorted_nums2 = merge_sort(nums2)
print("Sorted Array Example 2:")
print(sorted_nums2)



print("----Part 3----")
# ****************Part 3*****************
# Remove duplicates from sorted linked list
def remove_duplicates(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


# Example 1: Input: head = [1, 1, 2]
head1 = ListNode(1, ListNode(1, ListNode(2)))
result1 = remove_duplicates(head1)
print("Example 1: List after removing duplicates (Input: [1, 1, 2]):")
print_linked_list(result1)


# Example 2: Input: head = [1, 1, 2, 3, 3]
head2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
result2 = remove_duplicates(head2)
print("Example 2: List after removing duplicates (Input: [1, 1, 2, 3, 3]):")
print_linked_list(result2)



print("----Part 4----")
# ***************Part 4************************
# Remove Linked List Elements
def remove_elements(head, val):
    dummy = ListNode(next=head)
    current = dummy
    
    while current and current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
    
    return dummy.next

# Example usage for removing elements
head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
val = 6
new_head = remove_elements(head, val)
print("List after removing elements with value 6:")
print_linked_list(new_head)

# Example usage for an empty list
head = None
val = 1
new_head = remove_elements(head, val)
print("List after removing elements with value 1 (empty list):")
print_linked_list(new_head)

# Example usage for a list with all values the same
head = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
val = 7
new_head = remove_elements(head, val)
print("List after removing elements with value 7 (all same):")
print_linked_list(new_head)




print("----Part 5----")

# ******************Part 5*************************
# Reverse a linked list iteratively
def reverse_list_iterative(head):
    prev, current = None, head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Example usage for reversing the list iteratively
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reversed_head = reverse_list_iterative(head)
print("Iteratively Reversed List:")
print_linked_list(reversed_head)


# Reverse a linked list recursively
def reverse_list_recursive(head):
    if not head or not head.next:
        return head
    reversed_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return reversed_head

# Example usage for reversing the list recursively
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reversed_head = reverse_list_recursive(head)
print("Recursively Reversed List:")
print_linked_list(reversed_head)

