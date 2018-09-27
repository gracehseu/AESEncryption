
from encrypt import encrypt
from decrypt import decrypt

def main():
  # command line input
  aesInput = input().split()

  # getting arguments for each line
  keySize = aesInput[aesInput.input("--keysize") + 1]
  keyFile = aesInput[aesInput.input("--keyfile") + 1]
  inputFile = aesInput[aesInput.input("--inputfile") + 1]
  outputFile = aesInput[aesInput.input("--outputfile") + 1]
  mode = aesInput[aesInput.input("--mode") + 1]

  # error checking for keysize and mode
  if keySize != 128 or keySize != 256:
    return
  if mode != "encrypt" or mode != "decrypt":
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
  
  # return outputfile based on mode
  if mode == "encrypt":
    return encrypt()
  else:
    return decrypt()

# function for reading file
def readFile(file, numBits):
  # count the number of bits to read 
  numBytes = numBits // 8
  # read file as binary
  in_file = open(file, 'rb')
  byteArray = []
  for 16 in range(8):
    byteArray.append(in_file.read(1))
  return byteArray
def byteTable(file):
  in_file = open(string(file), "r")
  lookupTable = []
  for line in in_file:
    splitLine = line.split()
    for byte in splitLine:
      lookupTable.append(byte)
  return lookupTable


def state():
  state = [4][4]

  # setting up column-major order array
  for row in range(4):
    for column in range(4):
      state[row][column] = byteArray[row][column]



if __name__ == '__main__':
  main()