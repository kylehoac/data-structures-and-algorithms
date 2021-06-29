from code_challenges.quick_sort.quick_sort import quick_sort, partition,swap

def test_assert_quick_sort():
    assert quick_sort

def test_quick_sort():
    list = [8,4,23,42,16,15]
    actual = quick_sort(list, 0, len(list)-1)
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_quick_sort_with_negatives():
    list = [-8,4,23,42,16,15]
    actual = quick_sort(list, 0, len(list)-1)
    expected = [-8,4,15,16,23,42]
    assert actual == expected

def test_quick_sort_with_floats():
    list = [8,4,23,42,15.5,15.6,60]
    actual = quick_sort(list, 0, len(list)-1)
    expected = [4,8,15.5,15.6,23,42,60]
    assert actual == expected

def test_quick_sort_odd_num_of_nums():
    list = [8,4,23,42,16,15,60]
    actual = quick_sort(list, 0, len(list)-1)
    expected = [4,8,15,16,23,42,60]
    assert actual == expected

def test_quick_sort_with_one_value():
    list = [8]
    actual = quick_sort(list, 0, len(list)-1)
    expected = [8]
    assert actual == expected

def test_quick_sort_empty_list():
    list = []
    actual = quick_sort(list, 0, len(list)-1)
    expected = []
    assert actual == expected

def test_quick_sort_empty_list():
    list = [4,3,2,1]
    actual = quick_sort(list, 0, len(list)-1)
    expected = [4,3,2,1]
    assert actual != expected
