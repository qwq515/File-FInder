import os

file_lst = []

for root,dirs,files in os.walk("."):
    for f1 in files:
        if f1.endswith((".md",".txt")):
            file_lst.append(f1)
print(file_lst)
order = True
while order == True:
    words = input("please enter your words or quit:")   #如果用户想搜索quit怎么办
    
    if words == "quit":
        order = False
        print("bye")
    else:
        found = 0
        for name in file_lst:
            with open(name,"r",encoding = "utf-8") as f:
                f_str = f.read()
                i = 0
                for line in f_str:
                    i += 1
                    for word in line.split():   
                        if word.lower() == words:
                            found += 1
                            print(name)
                            print("line",i,line)
                            break
        if not found:
            print("no relevant information was found")        
        else:
            print("the number of file:",found)    