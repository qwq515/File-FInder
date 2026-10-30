import os
files = os.listdir(".")

file_lst = []

for f in files:
    if f.endswith((".md",".txt")):
        file_lst.append(f)
order = True
while order == True:
    words = input("please enter your words or quit:")
    
    if words == "quit":
        order = False
        print("bye")
    else:
        found = 0
        for name in file_lst:
            with open(name,"r",encoding = "utf-8") as f:
                f_str = f.read()
                for word in f_str.split():   
                    if word == words:
                        found += 1
                        print(name)
                        break
        if not found:
            print("no relevant information was found")        
        else:
            print("the number of file:",found)    