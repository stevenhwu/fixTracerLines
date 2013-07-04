import sys
def main():

    print "',.paoeu;qkj"
    if(len(sys.argv) > 2):
        fileName = "/home/sw167/PostdocLarge/BEASTRun/ProjectB_Jess/" + sys.argv[1]
        fileNameOut = fileName + "2"
        intGap = int(sys.argv[2])
    else:
        print "no arugment\n python fixLineNo.py logFileName\n"
        sys.exit(-1)
    f = open(fileName, 'r')
    f2 = open(fileNameOut, 'w')

    all_lines = f.readlines()
    print len(all_lines)
    cut = len(all_lines[10]) * 2
    offset = 4
    i = 0
    cc = 0
    new_file = []

    while i < len(all_lines):
        line = all_lines[i]

#         if i > 7954 and i < 7958:
#             print all_lines[i+1].split()
#             print int(all_lines[i+1].split()[0])
#             print int(all_lines[i].split()[0])

        if len(line) > cut:
            print "badline:", i, all_lines.index(line)
            bk_line = all_lines[(i - 1)]

            x = 0
            while len(all_lines[i + x]) > cut:
                x += 1

            to_line = all_lines[i + x]
            spaceIndex = bk_line.index("\t")
            print "bk", all_lines[(i - 1)],
            print "bkstat", len(bk_line), bk_line[0:spaceIndex], int(bk_line[0:spaceIndex]) / (i - 1 - offset)
            print "toLise", len(to_line), to_line[0:spaceIndex], int(to_line[0:spaceIndex]) / (intGap)
            print "gap", (int(to_line[0:spaceIndex]) - int(bk_line[0:spaceIndex])) / intGap


            for j in range(i + 1 - offset, int(to_line[0:spaceIndex]) / (intGap)):
#                 print j
                new_line = str(intGap * (j)) + "\t" + bk_line[(spaceIndex + 1):len(bk_line)]
#                 print new_line
                new_file.append(new_line)
            print j, "===End IF==="
            i = i + x - 1

        else:
            new_file.append(line)


        i += 1
    print "END"

    i = 0
    while i < (len(new_file) - 1):
        new_line = new_file[i]
        if i > offset and ((int(new_file[i + 1].split()[0]) - int(new_line.split()[0])) != intGap) :
            print "Jump:", int(new_file[i + 1].split()[0]) , int(new_file[i].split()[0])
            bk_line = new_file[i]
            to_line = new_file[i + 1]
            spaceIndex = bk_line.index("\t")
            print "aoeuaoeu:", (bk_line[0:spaceIndex]), i, offset
            print "bkstat", len(bk_line), bk_line[0:spaceIndex], int(bk_line[0:spaceIndex]) / (i - 1 - offset)
            print "toLise", len(to_line), to_line[0:spaceIndex], int(to_line[0:spaceIndex]) / (intGap)
            for j in range(i + 1 - offset, int(to_line[0:spaceIndex]) / (intGap)):
                new_line = str(intGap * (j)) + "\t" + bk_line[(spaceIndex + 1):len(bk_line)]
#                 print j, new_line
                f2.write(new_line)
            print j, "===End IF==="
        else:
            f2.write(new_line)

        i += 1



if __name__ == "__main__":
    main()
