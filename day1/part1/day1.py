import sys
def open_file(txt):
    file_object= open(txt,"r")
    c=count=0

    for i in file_object:
        if c < int(i):
            count+=1
        c = int(i)
    return count - 1
    # we subtract 1 due to the first value not counting as it is 
    # the starting valuee

def main():
    print(open_file(sys.argv[1]))

if __name__ == '__main__':
    main()

