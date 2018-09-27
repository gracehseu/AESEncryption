sBox = [63, 7c, 77, 7b, f2, 6b, 6f, c5, 30, 01, 67, 2b, fe, d7, ab, 76,
        ca, 82, c9, 7d, fa, 59, 47, f0, ad, d4, a2, af, 9c, a4, 72, c0,
        b7, fd, 93, 26, 36, 3f, f7, cc, 34, a5, e5, f1, 71, d8, 31, 15,
        04, c7, 23, c3, 18, 96, 05, 9a, 07, 12, 80, e2, eb, 27, b2, 75,
        09, 83, 2c, 1a, 1b, 6e, 5a, a0, 52, 3b, d6, b3, 29, e3, 2f, 84,
        53, d1, 00, ed, 20, fc, b1, 5b, 6a, cb, be, 39, 4a, 4c, 58, cf,
        d0, ef, aa, fb, 43, 4d, 33, 85, 45, f9, 02, 7f, 50, 3c, 9f, a8,
        51, a3, 40, 8f, 92, 9d, 38, f5, bc, b6, da, 21, 10, ff, f3, d2,
        cd, 0c, 13, ec, 5f, 97, 44, 17, c4, a7, 7e, 3d, 64, 5d, 19, 73,
        60, 81, 4f, dc, 22, 2a, 90, 88, 46, ee, b8, 14, de, 5e, 0b, db,
        e0, 32, 3a, 0a, 49, 06, 24, 5c, c2, d3, ac, 62, 91, 95, e4, 79,
        e7, c8, 37, 6d, 8d, d5, 4e, a9, 6c, 56, f4, ea, 65, 7a, ae, 08,
        ba, 78, 25, 2e, 1c, a6, b4, c6, e8, dd, 74, 1f, 4b, bd, 8b, 8a,
        70, 3e, b5, 66, 48, 03, f6, 0e, 61, 35, 57, b9, 86, c1, 1d, 9e,
        e1, f8, 98, 11, 69, d9, 8e, 94, 9b, 1e, 87, e9, ce, 55, 28, df,
        8c, a1, 89, 0d, bf, e6, 42, 68, 41, 99, 2d, 0f, b0, 54, bb, 16]

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
  state[1][0] = stateTemp[1][1]
  state[1][1] = stateTemp[1][2]
  state[1][2] = stateTemp[1][3]
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



def cipher(state, keySchedule, numRounds):
  # sanity check
  if len(state) != 16:
    raise Exception('input isn\'t a valid size in cipher()');

  addRoundKey(state, keySchedule, 0);

  for i in range(1, numRounds):
    state = subBytes(state)
    state = shiftRows(state)
    state = mixColumns(state)
    state = addRoundKey(state, keySchedule, numRounds)

  subBytes(state)
  shiftRows(state)
  addRoundKey(state, keySchedule, numRounds)
    
  return state