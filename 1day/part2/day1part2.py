import sys


def open_file(txt):
    queue = []
    c=0
    count = 0
    with open(txt) as file:
        lines = file.readlines()
        for i in range(len(lines)-2):
            queue.extend((int(lines[i]),int(lines[i+1]),int(lines[i+2])))
            if c < sum(queue):
                count +=1
            c = sum(queue)
            queue.clear()
    return count -1
def main():
    print(open_file(sys.argv[1]))


if __name__ == '__main__':
    main()