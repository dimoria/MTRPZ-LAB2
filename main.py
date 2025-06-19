from circular_linked_list import CircularLinkedList
from array_list import ArrayList

def demo_list_operations(lst):
    print("Append 'a', 'b', 'c'")
    lst.append('a')
    lst.append('b')
    lst.append('c')
    print("Length:", lst.length())

    print("Insert 'x' at index 1")
    lst.insert('x', 1)

    print("Get index 1:", lst.get(1))

    print("Delete index 2:", lst.delete(2))
    print("Find first 'a':", lst.findFirst('a'))
    print("Find last 'a':", lst.findLast('a'))

    print("Clone and reverse the list")
    cloned = lst.clone()
    cloned.reverse()
    print("Cloned first element after reverse:", cloned.get(0))

    print("Extend with ['y', 'z']")
    if isinstance(lst, CircularLinkedList):
        extension = CircularLinkedList()
    else:
        extension = ArrayList()
    extension.append('y')
    extension.append('z')
    lst.extend(extension)

    print("Delete all 'a'")
    lst.deleteAll('a')

    print("Clear list")
    lst.clear()
    print("Length after clear:", lst.length())

if __name__ == "__main__":
    print("== CircularLinkedList Demo ==")
    clist = CircularLinkedList()
    demo_list_operations(clist)

    print("\n== ArrayList Demo ==")
    alist = ArrayList()
    demo_list_operations(alist)
