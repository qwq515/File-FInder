import os
files = os.listdir(".")
file_lst = []
for f in files:
    if f.endswith((".md",".txt")):
        file_lst.append(f)
for name in file_lst:
    with open(name,"r",encoding = "utf-8") as f:
        f_str = f.read()
        print(f_str)
print(file_lst)