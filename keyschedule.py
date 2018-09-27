# global variable 
roundConstant = [
  [0x00, 0x00, 0x00, 0x00],
  [0x01, 0x00, 0x00, 0x00],
  [0x02, 0x00, 0x00, 0x00],
  [0x04, 0x00, 0x00, 0x00],
  [0x08, 0x00, 0x00, 0x00],
  [0x10, 0x00, 0x00, 0x00],
  [0x20, 0x00, 0x00, 0x00],
  [0x40, 0x00, 0x00, 0x00],
  [0x80, 0x00, 0x00, 0x00],
  [0x1b, 0x00, 0x00, 0x00],
  [0x36, 0x00, 0x00, 0x00],
]

# AES uses a key schedule to expand a short key into a number of separate round keys
# https://en.wikipedia.org/wiki/Rijndael_key_schedules
def keyExpansion(keyFile, keyLength):
  keySchedule = []

  for row in range(keyLength):
    keyRow = []
    for i in range(4):
      keyFile[4 * i]
      keyFile[4 * i + 1]
      keyFile[4 * i + 2]
      keyFile[4 * i + 3]

    keySchedule.append(keyRow)

  # expanding the key
  temp = []
  for i in range(keyLength, len(keySchedule)):
    keySchedule[i]
    for t in range(4):
      temp.append(keySchedule[i - 1, t])

    if (i % keyLength == 0)
      temp = subWord(rotWord(temp, Sbox))
      for t in range(len(temp)):
        temp[t] ^= roundConstant[i // keyLength][t]
    elif (keyLength > 6 and i % keyLength == 4):
      temp = subWord(temp)

    for t in range(4):
      keySchedule[i][t] = keySchedule[i - keyLength][t] ^ temp[t]

  return keySchedule


# applies the S-box transformation to every word
def subWord(word, Sbox):
  for i in range(len(word)):
    word[i] = Sbox[word[i]]
  return word

# rotates every word one byte to the left
def rotWord(word):
  # temp valuable for keeping first word before shift destroys
  first = word[0]
  # shift one byte over
  for i in range(len(word)):
    word[i] = word[i + 1]
  # last word is now first 
  word[len(word) - 1] = first
  return word

# addititon in place, AES addition is XOR
def addRoundKey(state, keySchedule, numRounds):
  for row in range(4):
    for colum in range(4):
      state[row][column] ^= keySchedule[numRounds * 4 + column][row]
  return state