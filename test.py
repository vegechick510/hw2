from hw2_debugging import merge_sort

def test_case_1():
    arr_in = [4,-3,2,5,4,0,1,1,3]
    arr_sorted = [-3,0,1,1,2,3,4,4,5]
    arr_out = merge_sort(arr_in)
    assert arr_out == arr_sorted

def test_case_2():
    arr_in = [0,0,0,0,1,0,0,0,0]
    arr_sorted = [0,0,0,0,0,0,0,0,1]
    arr_out = merge_sort(arr_in)
    assert arr_out == arr_sorted

def test_case_3():
    arr_in = [5, 5, 1, 6, -1, 4, 3, 7, 5]
    arr_sorted = [-1, 1, 3, 4, 5, 5, 5, 6, 7]
    arr_out = merge_sort(arr_in)
    assert arr_out == arr_sorted
