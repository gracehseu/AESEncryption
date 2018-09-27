invsBox =  [52, 09, 6a, d5, 30, 36, a5, 38, bf, 40, a3, 9e, 81, f3, d7, fb,
            7c, e3, 39, 82, 9b, 2f, ff, 87, 34, 8e, 43, 44, c4, de, e9, cb,
            54, 7b, 94, 32, a6, c2, 23, 3d, ee, 4c, 95, 0b, 42, fa, c3, 4e,
            08, 2e, a1, 66, 28, d9, 24, b2, 76, 5b, a2, 49, 6d, 8b, d1, 25,
            72, f8, f6, 64, 86, 68, 98, 16, d4, a4, 5c, cc, 5d, 65, b6, 92,
            6c, 70, 48, 50, fd, ed, b9, da, 5e, 15, 46, 57, a7, 8d, 9d, 84,
            90, d8, ab, 00, 8c, bc, d3, 0a, f7, e4, 58, 05, b8, b3, 45, 06,
            d0, 2c, 1e, 8f, ca, 3f, 0f, 02, c1, af, bd, 03, 01, 13, 8a, 6b,
            3a, 91, 11, 41, 4f, 67, dc, ea, 97, f2, cf, ce, f0, b4, e6, 73,
            96, ac, 74, 22, e7, ad, 35, 85, e2, f9, 37, e8, 1c, 75, df, 6e,
            47, f1, 1a, 71, 1d, 29, c5, 89, 6f, b7, 62, 0e, aa, 18, be, 1b,
            fc, 56, 3e, 4b, c6, d2, 79, 20, 9a, db, c0, fe, 78, cd, 5a, f4,
            1f, dd, a8, 33, 88, 07, c7, 31, b1, 12, 10, 59, 27, 80, ec, 5f,
            60, 51, 7f, a9, 19, b5, 4a, 0d, 2d, e5, 7a, 9f, 93, c9, 9c, ef,
            a0, e0, 3b, 4d, ae, 2a, f5, b0, c8, eb, bb, 3c, 83, 53, 99, 61,
            17, 2b, 04, 7e, ba, 77, d6, 26, e1, 69, 14, 63, 55, 21, 0c, 7d]

# each byte in the state is replaced with 
# its entry in a fixed 8-bit lookup table (S-box)
def invSubBytes(state):
  for row in range(4):
    for column in range(4):
      state[row][column] = invsBox[state[row][column]]
  return state

# bytes in each row of the state are shifted 
# cyclically to the left
def invshiftRows(state):
  stateTemp = state
  # do nothing for row 0

  # shift row 1 one over
  state[1][0] = stateTemp[1][3]
  state[1][1] = stateTemp[1][0]
  state[1][2] = stateTemp[1][1]
  state[1][3] = stateTemp[1][2]

  # shift row 2 two over
  state[2][0] = stateTemp[2][2]
  state[2][1] = stateTemp[2][3]
  state[2][2] = stateTemp[2][0]
  state[2][3] = stateTemp[2][1]  

  # shift row 3 three over
  state[3][0] = stateTemp[3][1]
  state[3][1] = stateTemp[3][2]
  state[3][2] = stateTemp[3][3]
  state[3][3] = stateTemp[3][0]  
  return state

def helperMultiply(a, b):
  p = 0
  iterations = 8
  currIter = 0
  while ( a < iterations and b < iterations and currIter < iterations):
    if (b & 0x01):
      p ^= a
    b = (b >> 1) & 0x7f
    carry = !!(a & 0x80)
    a = (a << 1)
    if carry:
      a ^= 0x011b
    currIter++
  return p

# each column of the state is multiplied 
# with a fixed polynomial
def invmixColumns(state):

  for column in range(4):
    copy = []
    for row in range(4):
      copy.append(state[row][column])

    state[0][column] = multiply(0x0e, copy[0]) ^ multiply(0x0b, copy[1]) ^ multiply(0x0d, copy[2]) ^ multiply(0x09, copy[3]);
    state[1][column] = multiply(0x09, copy[0]) ^ multiply(0x0e, copy[1]) ^ multiply(0x0b, copy[2]) ^ multiply(0x0d, copy[3]);
    state[2][column] = multiply(0x0d, copy[0]) ^ multiply(0x09, copy[1]) ^ multiply(0x0e, copy[2]) ^ multiply(0x0b, copy[3]);
    state[3][column] = multiply(0x0b, copy[0]) ^ multiply(0x0d, copy[1]) ^ multiply(0x09, copy[2]) ^ multiply(0x0e, copy[3]);

    return state

def decipher(state, keySchedule, numRounds):
  addRoundKey(state, keySchedule, numRounds);

  for _round in range(numRounds, 0, -1):
    state = invshiftRows(state)
    state = invsubBytes(state)
    state = addRoundKey(state, keySchedule, _round)
    state = invmixColumns(state)

  invShiftRows(state);
  invSubBytes(state);
  addRoundKey(state, keySchedule, 0);

  return state