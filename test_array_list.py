from array_list import ArrayList

def test_append_and_length():
    lst = ArrayList()
    assert lst.length() == 0
    lst.append('a')
    lst.append('b')
    assert lst.length() == 2

def test_insert_and_get():
    lst = ArrayList()
    lst.append('a')
    lst.append('b')
    lst.insert('x', 1)
    assert lst.get(1) == 'x'

def test_delete():
    lst = ArrayList()
    lst.append('a')
    lst.append('b')
    assert lst.delete(1) == 'b'
    assert lst.length() == 1

def test_find_first_last():
    lst = ArrayList()
    lst.append('a')
    lst.append('b')
    lst.append('a')
    assert lst.findFirst('a') == 0
    assert lst.findLast('a') == 2

def test_clone_and_reverse():
    lst = ArrayList()
    lst.append('a')
    lst.append('b')
    clone = lst.clone()
    clone.reverse()
    assert clone.get(0) == 'b'
