from code_challenges.merge_sort.merge_sort import merge_sort

def test_can_merge():
    assert merge_sort

def test_merge_sort():
    actual = merge_sort([6,10,3,5,9])
    expected = [3,5,6,9,10]
    assert actual == expected

def test_merge_sort_with_negative():
    actual = merge_sort([6,10,-3,5,9])
    expected = [-3,5,6,9,10]
    assert actual == expected

def test_merge_sort_with_negative_2():
    actual = merge_sort([5,4,-3,2,-1])
    expected = [-3,-1,2,4,5]
    assert actual == expected

def test_merge_sort_with_float():
    actual = merge_sort([0.1,5.0,1,13])
    expected = [0.1,1,5.0,13]
    assert actual == expected

def test_merge_sort_with_even_nums():
    actual = merge_sort([4,2,1,3])
    expected = [1,2,3,4]
    assert actual == expected

def test_merge_sort_with_odd_nums():
    actual = merge_sort([4,5,2,1,3])
    expected = [1,2,3,4,5]
    assert actual == expected

def test_merge_sort_base_case():
    actual = merge_sort([1])
    expected = [1]
    assert actual == expected
