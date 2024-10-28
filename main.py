extension = ".what"
name = "file"

with open(name+extension, "r") as file:
    lineTokens = [[""]]
    programLine = 0
    for line in file.readlines():
        for character in line:
            match character:
                case " ":
                    lineTokens[programLine].append("")
                case ".":
                    lineTokens[programLine].append(".")
                    lineTokens.append([""])
                    programLine += 1
                case "\n":
                    pass
                case _:
                    lineTokens[programLine][-1] += character




open(name+".py", "w").close()
with open(name+".py", "a") as file:
    for line in lineTokens:
        if line[0] == "": pass
        
        elif line[0] == "print": file.write("print(" + line[1] + ")")

        elif line[1] == "=": file.write(line[0] + " = " + line[2])

        file.write("\n")
