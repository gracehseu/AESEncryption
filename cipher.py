from keyschedule import addRoundKey, sBox



# each byte in the state is replaced with 
# its entry in a fixed 8-bit lookup table (S-box)
def subBytes(state, substitution_table):
  for row in range(4):
    for column in range(4):
      state[row][column] = substitution_table[state[row][column]]
  return state

# bytes in each row of the state are shifted 
# cyclically to the left
def shiftRows(state):
  stateTemp = []
  for row in range(4):
    stateTemp.append([])
    for column in range(4):
      stateTemp[row].append(state[row][column])

  # do nothing for row 0
  # shift row 1 one over
  state[0][0] = stateTemp[0][0]
  state[0][1] = stateTemp[1][1]
  state[0][2] = stateTemp[2][2]
  state[0][3] = stateTemp[3][3]

  state[1][0] = stateTemp[1][0]
  state[1][1] = stateTemp[2][1]
  state[1][2] = stateTemp[3][2]
  state[1][3] = stateTemp[0][3]

  state[2][0] = stateTemp[2][0]
  state[2][1] = stateTemp[3][1]
  state[2][2] = stateTemp[0][2]
  state[2][3] = stateTemp[1][3]

  state[3][0] = stateTemp[3][0]
  state[3][1] = stateTemp[0][1]
  state[3][2] = stateTemp[1][2]
  state[3][3] = stateTemp[2][3]
   
  return state

# each column of the state is multiplied 
# with a fixed polynomial
def mixColumns(state):

  for column in range(4):
    copy = []
    shift = []

    for row in range(4):
      copy.append(state[column][row])

      shift.append(state[column][row] << 1 ^ 0x011b if state[column][row] & 0x80  else state[column][row] << 1)

    state[column][0] = shift[0] ^ copy[1] ^ shift[1] ^ copy[2] ^ copy[3]
    state[column][1] = copy[0] ^ shift[1] ^ copy[2] ^ shift[2] ^ copy[3]
    state[column][2] = copy[0] ^ copy[1] ^ shift[2] ^ copy[3] ^ shift[3]
    state[column][3] = copy[0] ^ shift[0] ^ copy[1] ^ copy[2] ^ shift[3]

  return state




def cipher(state, keySchedule, numRounds):
  # sanity check
  if len(state) != 4:
    raise Exception('input isn\'t a valid size in cipher()')

  addRoundKey(state, keySchedule, 0)

  for i in range(1, numRounds):
    state = subBytes(state, sBox)
    state = shiftRows(state)
    state = mixColumns(state)
    state = addRoundKey(state, keySchedule, i)

  subBytes(state, sBox)
  shiftRows(state)
  addRoundKey(state, keySchedule, numRounds)
    
  return state