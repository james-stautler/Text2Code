
print("Enter/Paste your code. Ctrl-Z (Windows) or Ctrl-D (MacOS and Linux) and enter on the final line to save it.")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

outputCode = contents[0]
for line in contents[1:]:
    outputCode += "\\n"
    
    if not line: 
        continue

    spaceCount = 0
    index = 0
    while index < len(line) and line[index] == " ":
        spaceCount += 1
        index += 1
    line = line[index:]

    for i in range(spaceCount // 4):
        outputCode += "\\t"
    
    outputCode += line

print(outputCode)

input("Press any key to exit")
