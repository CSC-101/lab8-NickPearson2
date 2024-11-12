import sys
if __name__ == '__main__':
    try:
        infile = open(sys.argv[1],"r")
        for line in infile:
            line = line.rstrip("\n")
            float_list = line.split()
            total = 0
            for num in float_list:
                total += float(num)
            print(total)
        infile.close()
    except:
        print("Couldn't open file of", sys.argv)
        exit(1)

