extension = ".what"
name = "file"

def character_is_delimiter(line, index):
    delimiters = [" ", "."]
    if line[index] in delimiters:
        if line[-1] != "": return True
    else:
        return False

with open(name+extension, "r") as file:
    lineTokens = [""]
    indent = 0
    for line in file.readlines():
        for index, character in enumerate(line):
            if character == "(" or character == ")":
                if character == "(": indent += 1
                else: indent -= 1
            elif indent == 0:
                if character_is_delimiter(line, index): lineTokens.append("")
                elif character == "?":
                    if lineTokens[-1] != "": lineTokens += character
                    else: lineTokens.append(character)
                elif character == "(" or character == ")": 
                    if lineTokens[-1] == "": lineTokens[-1] += character
                    else: lineTokens.append(character)
                    lineTokens.append("")
                elif character == "\n": pass
                else: lineTokens[-1] += character

print(lineTokens)

indent = 0
open(name+".py", "w").close()
with open(name+".py", "a") as file:
    token = 0
    while token < len(lineTokens):
        if lineTokens[token] == "print": 
            file.write("print(" + lineTokens[token + 1] + ")")
            token += 2

        elif lineTokens[token + 1] == "is": 
            file.write(lineTokens[token] + " = " + lineTokens[token + 2])
            token += 3

        else: token += 1

        file.write("\n")

print("Done!")