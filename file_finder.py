import os
files = os.listdir(".")
file_lst = []
for f in files:
    if f.endswith((".md",".txt")):
        file_lst.append(f)
words = input("please enter your words:")
for name in file_lst:
    with open(name,"r",encoding = "utf-8") as f:
        f_str = f.read()
        found = False
        for word in f_str.split():   
            if word == words:
                found = True
                print(name)
if found == False:
    print("no relevant information was found")        