from code_challenges.linked_lists.linked_lists.linked_lists import LinkedList, Node, zip_list

# instantiates an empty linked list
def test_import():
    assert LinkedList

# Inserts single and multiple values into linked list
def test_can_insert():
    list = LinkedList(Node("1"))
    assert list.head.value == "1"
    assert list.head.next == None
    list.insert("2")
    assert list.head.value == "2"
    assert list.head.next.value == "1"
    list.insert("3")
    assert list.head.value == "3"
    assert list.head.next.value == "2"

# Tests that the head points to the first node
def test_has_head():
    list = LinkedList(Node("1"))
    assert list.head.value == "1"
    list.insert("2")
    assert list.head.value == "2"

# Test will return true when a value is included in a list
def test_can_include():
    list = LinkedList()
    list.insert("1")
    list.insert("2")

    actual = list.include("2")
    expected = True
    assert actual == expected

# Test will return false when a value is not included in a list
def test_false_when_not_included():
    list = LinkedList()
    list.insert("1")
    list.insert("2")

    actual = list.include("3")
    expected = False
    assert actual == expected

# Returns a collection (list) of all values in linked list
def test_return_all_values():
    list = LinkedList()
    list.insert("1")
    list.insert("2")

    actual = list.get_all_values()
    expected = ["2", "1"]
    assert actual == expected

# Takes all values of a linked list, and returns them in a formatted string
def test_to_string():
    list = LinkedList()
    list.insert("{ c }")
    list.insert("{ b }")
    list.insert("{ a }")
    actual = list.__str__()

    expected = "{ a } -> { b } -> { c } -> None"

    assert actual == expected

# Returns message if __str__ is ran on an empty list
def test_to_string_with_empty_list():
    list = LinkedList()
    actual = list.__str__()

    expected = "List is empty"

    assert actual == expected

def test_append_node():
    list = LinkedList()
    list.insert("{ b }")
    list.insert("{ a }")
    list.append("{ c }")

    actual = list.__str__()
    expected = "{ a } -> { b } -> { c } -> None"
    assert actual == expected


def test_insert_before():
    list = LinkedList()
    list.insert("{ d }")
    list.insert("{ b }")
    list.insert("{ a }")
    list.insert_before("{ d }","{ c }")

    actual = list.__str__()
    expected = "{ a } -> { b } -> { c } -> { d } -> None"

    assert actual == expected

def test_insert_after():
    list = LinkedList()
    list.insert("{ c }")
    list.insert("{ b }")
    list.insert("{ a }")
    list.insert_after("{ c }","{ d }")

    actual = list.__str__()
    expected = "{ a } -> { b } -> { c } -> { d } -> None"

    assert actual == expected

# def test_kth_from_end():
#     list = LinkedList()
#     list.insert("c")
#     list.insert("b")
#     list.insert("a")

#     actual = list.kth_from_end(0)
#     expected = "c"

#     assert actual == expected

def test_zip():
    lista = LinkedList()
    listb = LinkedList()

    lista.insert("b")
    lista.insert("a")
    listb.insert("2")
    listb.insert("1")
    actual = str(zip_list(lista, listb))
    expected = "a -> 1 -> b -> 2 -> None"
    assert actual == expected

# def test_add_odd():
#     lista = LinkedList()
#     lista.insert(3)
#     lista.insert(2)
#     lista.insert(1)
#     actual = lista.add_odd()
#     expected = 4
#     assert actual == expected

def test_reverse_list():
    list = LinkedList()
    list.insert(3)
    list.insert(2)
    list.insert(1)
    actual = str(list.reverse_list(list))
    expected = "3 -> 2 -> 1 -> None"
    assert actual == expected
