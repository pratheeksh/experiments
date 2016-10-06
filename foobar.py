

def readFile(filename, visited_files):
    input_file = open(filename, "r")

    for line in input_file.readlines():
        # print line
        if "#include" in line:
            file_name = line.split(" ")[1]
            file_name = file_name.split("\n")[0]
            # file_to_read = open(line[1], "r")
            if file_name not in visited_files:
                readFile(file_name, visited_files + [file_name])
            else:
                print "LOOP"
        else:
            print line


readFile("foo.txt", ["foo.txt"])
