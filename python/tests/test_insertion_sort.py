from code_challenges.insertion_sort.insertion_sort import insertion_sort

def test_insertion_sort():
    arr = [1,2,4,5,3]
    insertion_sort(arr)
    expected = [1,2,3,4,5]
    assert arr == expected

def test_insertion_sort_negatives():
    arr = [48,-14,31,1,10]
    insertion_sort(arr)
    expected = [-14,1,10,31,48]
    assert arr == expected

def test_insertion_sort_floats():
    arr = [48,-14,31.1,1,10.0]
    insertion_sort(arr)
    expected = [-14,1,10.0,31.1,48]
    assert arr == expected

def test_insertion_sort_fails():
    arr = [48,-14,31.1,1,10.0]
    insertion_sort(arr)
    expected = [48,31,1,10.0,1,-14]
    assert arr != expected
