extension = ".what"
name = "file"

with open(name+extension, "r") as file:
    lineTokens = [""]
    for line in file.readlines():
        for character in line:
            match character:
                case " ":
                    if lineTokens[-1] != "": lineTokens.append("")
                case ".":
                    if lineTokens[-1] != "": lineTokens.append("")
                case "\n":
                    pass
                case _:
                    lineTokens[-1] += character

print(lineTokens)


open(name+".py", "w").close()
with open(name+".py", "a") as file:
    token = 0
    while token < len(lineTokens):

        if lineTokens[token] == "": token += 1
        
        elif lineTokens[token] == "print": 
            file.write("print(" + lineTokens[token + 1] + ")")
            token += 2

        elif lineTokens[token + 1] == "=": 
            file.write(lineTokens[token] + " = " + lineTokens[token + 2])
            token += 3
        
        else: token += 1

        file.write("\n")
