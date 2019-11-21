import os

dir_path = "../../data/"
files_lst = os.listdir(dir_path)
result = ""
for i in files_lst:
    f = open(dir_path + i, "rb")
    for line in f:
        result += line[:100].decode('utf-8')
    result += "\n\n\n"

with open("result.txt", "w") as f1:
    f1.write(result)
    f1.close()
