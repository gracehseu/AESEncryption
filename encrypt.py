
from cipher import cipher
from keyschedule import keyExpansion

def encrypt(inputFile, outputFile, keySize, keyFile, keyLength, numRounds):
  keySchedule = keyExpansion(keyFile, keyLength)

  # numBytes = numBits // 8
  # read file as binary
  in_file = open(inputFile, 'rb')
  out_file = open(outputFile, 'wb')
  
  # try catch surrounding, lots of testing

  file_bytes = in_file.read()
  padding_length = 16 - len(file_bytes) % 16
  file_bytes += bytes([padding_length] * padding_length)
  
  # sanity check
  assert(len(file_bytes) % 16 == 0)

  for i in range(len(file_bytes) // 16):
    state = []
    chunk = file_bytes[i * 16:(i + 1) * 16]
    for row in range(4):
      state.append([])
      for column in range(4):
        if len(state[row]) <= 0:
          state[row].append([])
        state[row].append(chunk[row * 4 + column])



    output = cipher(state, keySchedule, numRounds)
    bytes_written = out_file.write(output)
    # sanity check
    assert(bytes_written == 16)
