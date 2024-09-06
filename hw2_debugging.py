import rand


def mergeSort(arr):

    if len(arr) == 1:
        return arr

    half = len(arr)//2

    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))


def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(leftArr) + len(rightArr))
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            # print(leftIndex,rightIndex)
            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
            leftIndex += 1
        else:
            # print(leftIndex,rightIndex)
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]
            rightIndex += 1

    for i in range(rightIndex, len(rightArr)):
        mergeArr[leftIndex + i] = rightArr[i]

    for i in range(leftIndex, len(leftArr)):
        mergeArr[rightIndex + i] = leftArr[i]

    return mergeArr


arr1 = rand.random_array([None] * 20)
arr_out = mergeSort(arr1)

print(arr_out)
