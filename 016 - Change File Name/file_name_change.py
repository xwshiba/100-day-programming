import os
path = "D: \Wu_After Works\Photo\2021_06_14\morning\group2\cr2\"


def rename_files():
    for filename in os.listdir(path):
        my_source = path + filename
        new_name = filename[:6] + str(int(filename[6:8]) + 84) + filename[8:]
        my_dest = path + new_name
        os.rename(my_source, my_dest)
    return "success!"
