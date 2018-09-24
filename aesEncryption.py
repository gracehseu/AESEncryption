# function for reading file
def readFile(file, numBits):
  # count the number of bits to read 
  numBytes = numBits // 8
  # read file as binary
  in_file = open(file, rb)
  byteArray = []
  for 16 in range(8):
    byteArray.append(in_file.read(1))
  return byteArray

def main():

  keyValue = int(input("Length of the Cipher Key? "))

  rounds = -1
  if keyValue == 128:
    rounds = 10
  else if keyValue == 128:
    rounds = 10
  else if keyValue == 128:
    rounds = 10 
  else:
    # not a valid key value
    return

def byteTable(file):
  in_file = open(string(file), "r")
  lookupTable = []
  for line in in_file:
    splitLine = line.split()
    lookupTable.append(line)
  return lookupTable

def subBytes():
  # for each byte in array, use value to find an fixed-256 element lookup
  for i in range(4):
    for j in range(4):
      
def cipher(inputArray, ):

def state():
  stateArray = [4][4]

  # setting up column-major order array
  for i in range(4):
    for j in range(4):
      stateArray[j][i] = byteArray[i][j]


