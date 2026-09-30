import os
file = os.listdir(".")
file_lst = []
for f in file:
    if f.endswith(".md") or f.endswith("txt"):
        file_lst.append(f)
print(file_lst)