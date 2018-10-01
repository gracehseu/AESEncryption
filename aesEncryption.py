import sys
from encrypt import encrypt
from decrypt import decrypt

def main():


  # getting arguments for each line
  keySize = int(sys.argv[sys.argv.index("--keysize") + 1])
  keyFile = sys.argv[sys.argv.index("--keyfile") + 1]
  inputFile = sys.argv[sys.argv.index("--inputfile") + 1]
  outputFile = sys.argv[sys.argv.index("--outputfile") + 1]
  mode = sys.argv[sys.argv.index("--mode") + 1]


  # print ( keySize, keyFile, inputFile, outputFile, mode)
  # error checking for keysize and mode
  # print (type(keySize))
  if keySize != 128 and keySize != 256:
    print("keysize not valid")
    return
  if mode != "encrypt" and mode != "decrypt":
    print("mode not valid")
    return 

  # determining the number of rounds based on keysize
  numRounds = 0
  keyLength = 0
  if keySize == 128:
    numRounds = 10
    keyLength = 4
  else:
    numRounds = 14
    keyLength = 8
  
  key_file = open(keyFile, 'rb')
  key_bytes = key_file.read()
  # return outputfile based on mode
  if mode == "encrypt":
    # print("encrypting")

    return encrypt(inputFile, outputFile, keySize, key_bytes, keyLength, numRounds)
  else:
    print("decrypting")
    return decrypt(inputFile, outputFile, keySize, key_bytes, keyLength, numRounds)

# def state():
#   state = [4][4]

#   # setting up column-major order array
#   for row in range(4):
#     for column in range(4):
#       state[row][column] = byteArray[row][column]



if __name__ == '__main__':
  main()