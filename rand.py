import subprocess


def random_array(arr):
    """
    random generate array
    """
    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        # print(shuffled_num.stdout,int(shuffled_num.stdout))
        arr[i] = int(shuffled_num.stdout)
    return arr
