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
            fixTreeNo(fileName)
            sys.exit(-1)

def fixTreeNo(fileName):

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
        if all_lines[i].find("tree") is 0:
            stateIndex = all_lines[i].index("STATE_")+len("STATE_")
            spaceIndex = all_lines[i].index(" [", stateIndex)
            state_0 = int(all_lines[i][stateIndex:spaceIndex])

            stateIndex = all_lines[i+1].index("STATE_")+len("STATE_")
            spaceIndex = all_lines[i+1].index(" [", stateIndex)
            state_1 = int(all_lines[i+1][stateIndex:spaceIndex])
            iteration_gap = state_1 - state_0
            break
        else:
            new_file.append(all_lines[i])
            i = i+1
    # print(i)
    # print(iteration_gap)
    # sys.exit(1)
    # i = 3
    while i < (len(all_lines)-2):
        line = all_lines[i]
        
        # spaceIndex = line.index("\t") + 1

        stateIndex = all_lines[i+1].index("STATE_")+len("STATE_")
        spaceIndex = all_lines[i+1].index(" [", stateIndex)
        next_state = int(all_lines[i+1][stateIndex:spaceIndex])

        stateIndex = all_lines[i].index("STATE_")+len("STATE_")
        spaceIndex = all_lines[i].index(" [", stateIndex)
        state_0 = int(all_lines[i][stateIndex:spaceIndex])

        
        if(next_state - state_0 != iteration_gap):
            
            stateIndex = all_lines[i+2].index("STATE_")+len("STATE_")
            spaceIndex = all_lines[i+2].index(" [", stateIndex)
            jump_state = int(all_lines[i+2][stateIndex:spaceIndex])
            jump_state = next_state
            
            spaceIndex = all_lines[i-5].index(" [")
            new_line_template = all_lines[i-5][spaceIndex:len(all_lines[i-5])]
            print state_0, next_state, jump_state, iteration_gap, all_lines[i-5][0:spaceIndex]

            print "currentState", state_0
            print "jumpState", jump_state
            print "gap", iteration_gap
            print i, state_0 / iteration_gap , jump_state / iteration_gap
        
            # new_file.append(line)
            # iteration_gap = line.count("\t")
            for j in range(state_0 / iteration_gap , jump_state / iteration_gap-1):
        
                new_line = "tree STATE_"+str(iteration_gap * (j)) + new_line_template
                new_file.append(new_line)
        #
            # i = i + 1
            print "===End IF skip steps==="

        elif (line.find(chr(ord("\00"))) is not -1) | (line.find("\\00") is not -1):
            print "badline method 1:", i, all_lines.index(line)

#         elif (len(line) > cut) :
#             print "badline method 2:", i, all_lines.index(line)
#             bk_line = all_lines[(i - 1)]
#
#             x = 0
#             while len(all_lines[i + x]) > cut:
#                 x += 1
#
#             to_line = all_lines[i + x]
#             print to_line
#             spaceIndex = bk_line.index("\t") + 1
#
#             start_bk_state = int(bk_line[0:spaceIndex])
#             jump_to_state = int(to_line[0:spaceIndex])
#
# #            iteration_gap = int(all_lines[i + x + 1][0:spaceIndex]) - jump_to_state
#
#
# #            print "bk", x, all_lines[(i - 1)],
#             print "bkstat", len(bk_line), bk_line[0:spaceIndex], int(bk_line[0:spaceIndex])
#             print "toList", len(to_line), to_line[0:spaceIndex], int(to_line[0:spaceIndex]) / (iteration_gap)
#             print "gap", iteration_gap
#
#             stat_count = bk_line.count("\t")
#             for j in range(start_bk_state / iteration_gap + 1, jump_to_state / iteration_gap):
#
#                 new_line = str(iteration_gap * (j)) + "\t0"*stat_count + "\n"  # + bk_line[(spaceIndex + 1):len(bk_line)]
#                 new_file.append(new_line)
#
#             print "===End IF==="
#             i = i + x - 1

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
