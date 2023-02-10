import sys, os, getopt

def main(argv):
    calc_file = ''
    exe_file = ''

    try:
        opts, args = getopt.getopt(argv, "hi:",["help",'ifile='])
    except getopt.GetoptError as err:
        # print help information and exit
        print(err)      
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-i", "--ifile"):
            calc_file = a + '.cpp'
            exe_file = a
            run(calc_file, exe_file)


def usage():
    print('main.py -i <filename> (without .cpp extension)')

def run(calc_file, exe_file):
    os.system("echo Compiling " + calc_file)
    os.system('g++ ' + calc_file + ' -o ' + exe_file)
    os.system("echo -------------------")
    os.system(exe_file)

if __name__=='__main__':
    main(sys.argv[1:])
