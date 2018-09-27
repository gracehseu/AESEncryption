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

# helper function matrix multiplies column individually according to 
# https://en.wikipedia.org/wiki/Rijndael_MixColumns#Implementation_example
def mixColumnsHelper(column, matrixMultiply):
  a = [None] * 4
  b = [None] * 4
  for c in range(4):
    a[c] = state[c]
    h = state[i] >> 7
    b[i] = state[i] << 1
    b[i] ^= 0x1B & h

  r[0] = b[0] ^ a[3] ^ a[2] ^ b[1] ^ a[1]
  r[1] = b[1] ^ a[0] ^ a[3] ^ b[2] ^ a[2]
  r[2] = b[2] ^ a[1] ^ a[0] ^ b[3] ^ a[3]
  r[3] = b[3] ^ a[2] ^ a[1] ^ b[0] ^ a[0]

# each column of the state is multiplied 
# with a fixed polynomial
def mixColumns(state, matrixMultiply):

  for column in range(4):
    columnA = []
    for row in range(4):
      columnA.append(state[row][column])
    b = mixColumnsHelper(columnA)
    for row in range(4):
      state[row][column] = b[row]
  return state