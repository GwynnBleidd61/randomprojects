import sys

def automaton(wolfram_code):
    wolfram_code = bin(wolfram_code)[2:].zfill(8)
    
    wolfram_dict = {
        '111': wolfram_code[0], '110': wolfram_code[1], '101': wolfram_code[2], '100': wolfram_code[3],
        '011': wolfram_code[4], '010': wolfram_code[5], '001': wolfram_code[6], '000': wolfram_code[7]
    }

    current_line = '.' * 39 + '#' + '.' * 39
    current_line = current_line.replace('.', '0').replace('#', '1')
    
    print(current_line.replace('0', '.').replace('1', '#'))
    

    for _ in range(39):
        next_line = ''
        for i in range(len(current_line)):
            if i == 0:
                lul = current_line[-1] + current_line[:2]
            elif i == len(current_line) - 1:
                lul = current_line[-2:] + current_line[-1]
            else:
                lul = current_line[i-1:i+2]
            
            next_line += wolfram_dict[lul]
        
        print(next_line.replace('0', '.').replace('1', '#'))
        current_line = next_line


def main():
    if len(sys.argv) != 2:
        print("Usage: python solution.py <wolfram_code>")
        sys.exit(1)

    try:
        wolfram_code = int(sys.argv[1])
    except ValueError:
        print("The wolfram_code must be an integer.")
        sys.exit(1)

    if not (0 <= wolfram_code <= 255):
        print("The wolfram_code must be between 0 and 255.")
        sys.exit(1)

    automaton(wolfram_code)

if __name__ == "__main__":
    main()
