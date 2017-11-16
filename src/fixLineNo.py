import sys
import os




def main():


#    fileName = "/home/sw167/PostdocLarge/BEASTRun/Project_OrigFungi/indRun/cluster_2944    /cluster_2944.log"
#    fileName = "/home/sw167/PostdocLarge/BEASTRun/Project_OrigFungi/indRun/cluster_2888/cluster_2888.log"
#    fixLineNo(fileName)
#    sys.exit(-1)

#    sys.argv = ["", "/home/sw167/PostdocLarge/BEASTRun/Project_OrigFungi/MultiRegion_R5/allLogs/"]
    print "arg", sys.argv
    dir = sys.argv[1]
    if(len(sys.argv) > 1):
#        for f in os.listdir(dir):
#            print f
#            fileName = dir + f
            fileName = sys.argv[1]
            fixLineNo(fileName)
            sys.exit(-1)

def fixLineNo(fileName):

#    sys.argv = ["", "/home/sw167/PostdocLarge/BEASTRun/Project_OrigFungi/MultiRegion_R5/clusterR5_10/clusterR5_10.log2"]

#    print "arg", sys.argv
#    if(len(sys.argv) > 1):
#        fileName = sys.argv[1]
    fileNameOut = fileName + "2"
#        iteration_gap = int(sys.argv[2])
#    else:
#        print "no arugment\n python fixLineNo.py logFileName\n"
#        sys.exit(-1)
    f = open(fileName, 'r')
    f2 = open(fileNameOut, 'w')

    all_lines = f.readlines()

    cut = len(all_lines[10]) * 1.1
#    offset = 4

    i = 0
    new_file = []

    iteration_gap = 0
    while i < len(all_lines):
        if all_lines[i].find("0") is 0:
            spaceIndex = all_lines[i].index("\t")
            state_0 = int(all_lines[i][0:spaceIndex])

            spaceIndex = all_lines[i + 1].index("\t")
            state_1 = int(all_lines[i + 1][0:spaceIndex])

            iteration_gap = state_1 - state_0
            break
        i += 1
        
    new_file.append(all_lines[0])
    new_file.append(all_lines[1])
    new_file.append(all_lines[2])
    
    i = 3
    while i < (len(all_lines)-2):
        line = all_lines[i]
        
        spaceIndex = line.index("\t") + 1

        state = int(line[0:spaceIndex])
        # print i, len(all_lines),  i>3 , i < (len(all_lines)-3),  i>3 and i < (len(all_lines)-3)
        next_line = all_lines[i+1]
        spaceIndex = next_line.index("\t") + 1
        next_line_state = int(next_line[0:spaceIndex])
        
        if(next_line_state - state != iteration_gap):
            jump = False
            jump_line = all_lines[i+2]
            spaceIndex = jump_line.index("\t") + 1
            jump_line_state = int(jump_line[0:spaceIndex])
            
            print state, next_line_state, jump_line_state, iteration_gap

            print "currentState", state
            print "jumpState", jump_line_state
            print "gap", iteration_gap
        
            new_file.append(line)
            stat_count = line.count("\t")
            for j in range(state / iteration_gap + 1, jump_line_state / iteration_gap):
        
                new_line = str(iteration_gap * (j)) + "\t0"*stat_count + "\n"  # + bk_line[(spaceIndex + 1):len(bk_line)]
                new_file.append(new_line)
        #
            i = i + 1
            print "===End IF skip steps==="

        elif (line.find(chr(ord("\00"))) is not -1) | (line.find("\\00") is not -1):
            print "badline method 1:", i, all_lines.index(line)

        elif (len(line) > cut) :
            print "badline method 2:", i, all_lines.index(line)
            bk_line = all_lines[(i - 1)]

            x = 0
            while len(all_lines[i + x]) > cut:
                x += 1

            to_line = all_lines[i + x]
            print to_line
            spaceIndex = bk_line.index("\t") + 1

            start_bk_state = int(bk_line[0:spaceIndex])
            jump_to_state = int(to_line[0:spaceIndex])

#            iteration_gap = int(all_lines[i + x + 1][0:spaceIndex]) - jump_to_state


#            print "bk", x, all_lines[(i - 1)],
            print "bkstat", len(bk_line), bk_line[0:spaceIndex], int(bk_line[0:spaceIndex])
            print "toList", len(to_line), to_line[0:spaceIndex], int(to_line[0:spaceIndex]) / (iteration_gap)
            print "gap", iteration_gap

            stat_count = bk_line.count("\t")
            for j in range(start_bk_state / iteration_gap + 1, jump_to_state / iteration_gap):

                new_line = str(iteration_gap * (j)) + "\t0"*stat_count + "\n"  # + bk_line[(spaceIndex + 1):len(bk_line)]
                new_file.append(new_line)

            print "===End IF==="
            i = i + x - 1

        else:
            new_file.append(line)


        i += 1
    print "END"

    i = 0
    while i < (len(new_file) - 1):
        new_line = new_file[i]
#        if i > offset and ((int(new_file[i + 1].split()[0]) - int(new_line.split()[0])) != iteration_gap) :
#            print "Jump:", int(new_file[i + 1].split()[0]) , int(new_file[i].split()[0])
#            bk_line = new_file[i]
#            to_line = new_file[i + 1]
#            spaceIndex = bk_line.index("\t")
#            print "aoeuaoeu:", (bk_line[0:spaceIndex]), i, offset
#            print "bkstat", len(bk_line), bk_line[0:spaceIndex], int(bk_line[0:spaceIndex]) / (i - 1 - offset)
#            print "toLise", len(to_line), to_line[0:spaceIndex], int(to_line[0:spaceIndex]) / (iteration_gap)
#            for j in range(i + 1 - offset, int(to_line[0:spaceIndex]) / (iteration_gap)):
#                new_line = str(iteration_gap * (j)) + "\t" + bk_line[(spaceIndex + 1):len(bk_line)]
# #                 print j, new_line
#                f2.write(new_line)
#            print "===End IF==="
#        else:
        f2.write(new_line)
        i += 1



if __name__ == "__main__":
    main()
