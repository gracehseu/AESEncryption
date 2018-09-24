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
  byteArray = readFile()

def state():
  stateArray = [4][4]

  # setting up column-major order array
  for i in range(4):
    for j in range(4):
      stateArray[j][i] = byteArray[i][j]
