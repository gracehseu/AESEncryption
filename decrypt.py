
from decipher import decipher
from keyschedule import keyExpansion

def decrypt(inputFile, outputFile, keySize, keyFile, keyLength, numRounds):
  keySchedule = keyExpansion(keyFile, keyLength, numRounds)

  # read file as binary
  in_file = open(inputFile, 'rb')
  out_file = open(outputFile, 'wb')

  file_bytes = in_file.read()

  # sanity check
  assert(len(file_bytes) % 16 == 0)

  for i in range(len(file_bytes) // 16):
    state = []
    chunk = file_bytes[i * 16:(i + 1) * 16]
    for row in range(4):
      state.append([])
      for column in range(4):
        state[row].append(chunk[row * 4 + column])



    output = decipher(state, keySchedule, numRounds)
    output_bytes = bytearray()
    for t in range(4):
      output_bytes.extend(bytes(output[t]))

    if i < len(file_bytes) // 16 - 1:
      bytes_written = out_file.write(output_bytes)
      # sanity check
      assert(bytes_written == 16)
    else:
      padding = output[3][3]
      bytes_written = out_file.write(output_bytes[0:(16 - padding)])
      print(len(output_bytes[0:16-padding]))

      # assert(bytes_written == 16 - padding if padding != 16 else 0)
  out_file.close()
    