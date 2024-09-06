from hw2_debugging import merge_sort

def test_case_1():
    arr_1 = [4,-3,2,5,4,0,1,1,3]
    arr_1_sorted = [-3,0,1,1,2,3,4,4,5]
    merge_out_1 = merge_sort(arr_1)
    assert merge_out_1 == arr_1_sorted
