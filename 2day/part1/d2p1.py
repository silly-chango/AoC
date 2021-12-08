import sys 
def plot(txt):
    hor = 0
    ver = 0
    with open(txt) as file:
        for i in file:
            if "forward" in i:
                hor = hor +int(i[-2])
            else:
                if "down" in i:
                    ver = ver + int(i[-2])
                elif "up" in i:
                    ver = ver - int(i[-2])
    return hor * ver
                
                

def main():
    print(plot(sys.argv[1]))

if __name__ == '__main__':
    main()