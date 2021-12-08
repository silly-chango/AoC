import sys 

def gamma(txt):
    zeros = 0
    gamma = ''
    with open(txt) as file:
        lines = file.readlines()
        for i in range(12):
            for j in lines:       
                if int(j[i]) == 0:
                    zeros = zeros+1
            if (len(lines) -zeros) < zeros:
                gamma=gamma+"0"
                zeros = 0
            else:
                gamma=gamma+"1"
                zeros = 0
                
    return gamma
                
def epsilon(txt):
    zeros = 0
    epsilon = ''
    with open(txt) as file:
        lines = file.readlines()
        for i in range(12):
            for j in lines:       
                if int(j[i]) == 0:
                    zeros = zeros+1
            if (len(lines) -zeros) < zeros:
                epsilon=epsilon+"1"
                zeros = 0
            else:
                epsilon=epsilon+"0"
                zeros = 0
                
    return epsilon
def bin_to_dec(binary):
    return int(binary,2)
    
    
def main():
    print(bin_to_dec(gamma(sys.argv[1]))*bin_to_dec(epsilon(sys.argv[1])))
    

if __name__ == '__main__':
    main()