import optparse

def read_input_file(filename):
    try:
        data = open(filename, "rb").read()
        print '[+] Read file: ' + filename
        return data
    except:
        error('[-] Error reading file ' + filename)

def write_output_file(filename, data):
    try:
        f = open(filename, "w")
        f.write(data)
        print '[+] Written data to: ' + filename
    except:
        error('[-] Error writing to output file ' + filename)

def xor_data(data, pattern):
    output = ""
    pattern_length = len(pattern)
    for index, c in enumerate(data):
        val = ord(c) ^ pattern[index % pattern_length]
        output += chr(val)
    print '[+] XOR:ed data'
    return output

def header():
    print 'XOR file by kza 2018'

def error(message):
    print message
    exit(0)

def main():
    header()
    parser = optparse.OptionParser("usage: %prog -f <input file name> -o <output file name> -p <hex pattern>")
    parser.add_option('-f', dest='inputFile', type='string', help='input file')
    parser.add_option('-o', dest='outputFile', type='string', help='output file')
    parser.add_option('-p', dest='hexPattern', type='string', help='hex pattern')
    (options, args) = parser.parse_args()
    inputFile = options.inputFile
    outputFile = options.outputFile
    hexPattern = options.hexPattern
    if (inputFile == None):
        error('[-] You must specify an input file')
    if (outputFile == None):
        error('[-] You must specify an output file')
    if (hexPattern == None):
        error('[-] You must specify a hex pattern')

    try:
        pattern = bytearray.fromhex(options.hexPattern)
    except:
        error('[-] Invalid hex pattern')

    file_data = read_input_file(inputFile)
    data = xor_data(file_data, pattern)
    write_output_file(outputFile, data)

if __name__ == "__main__":
    main()