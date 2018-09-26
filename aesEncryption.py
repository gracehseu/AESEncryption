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
    for byte in splitLine:
      lookupTable.append(byte)
  return lookupTable

# each byte in the state is replaced with 
# its entry in a fixed 8-bit lookup table (S-box)
def subBytes(state, sBox):
  for row in range(4):
    for column in range(4):
      state[row][column] = sBox[state[row][column]]
  return state

# bytes in each row of the state are shifted 
# cyclically to the left
def shiftRows(state):
  stateTemp = state
  # do nothing for row 0
  # shift row 1 one over
  state[1][0] = stateTemp[1][3]
  state[1][1] = stateTemp[1][2]
  state[1][2] = stateTemp[1][1]
  state[1][3] = stateTemp[1][0]

  # shift row 2 two over
  state[2][0] = stateTemp[2][2]
  state[2][1] = stateTemp[2][3]
  state[2][2] = stateTemp[2][0]
  state[2][3] = stateTemp[2][1]  

  # shift row 3 three over
  state[3][0] = stateTemp[3][3]
  state[3][1] = stateTemp[3][0]
  state[3][2] = stateTemp[3][1]
  state[3][3] = stateTemp[3][2]  
  return state

# helper function matrix multiplies column 
# individually 
def mixColumnsHelper(column, matrixMultiply):
  b = []
  # go through each row of the matrix
  for row in range(len(matrix)):
    newB = 0
    for a in range(len(column)):
      newB += matrix[row][a] * column[a]
    b.append(newB)
  return b

# each column of the state is multiplied 
# with a fixed polynomial
def mixColumns(state, matrixMultiply):
  # helper function returns rows want to make sure 
  # that we put those in the right place
  for column in range(4):
    columnA = []
    for row in range(4):
      columnA.append(state[row][column])
    b = mixColumnsHelper(columnA)
    for row in range(4):
      state[row][column] = b[row]
  return state



def cipher(inputArray, ):

def state():
  state = [4][4]

  # setting up column-major order array
  for row in range(4):
    for column in range(4):
      state[row][column] = byteArray[row][column]


