
from cipher import cipher
from keyschedule import keyExpansion

def encrypt(inputFile, outputFile, keySize, keyFile, keyLength, num_rounds):
  keySchedule = keyExpansion(keyFile, keyLength, num_rounds)

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
        state[row].append(chunk[row * 4 + column])

    output = cipher(state, keySchedule, num_rounds)
    output_bytes = bytearray()
    for t in range(4):
      output_bytes.extend(bytes(output[t]))

    bytes_written = out_file.write(output_bytes)
    # sanity check
    assert(bytes_written == 16)
  out_file.close()
