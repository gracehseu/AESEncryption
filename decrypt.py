
from decipher import decipher
from keyschedule import keyExpansion

def decrypt(inputFile, outputFile, keySize, keyFile, keyLength, numRounds):
  blockSize = 4
  keySchedule = keyExpansion(keyFile, keyLength)

  numBytes = numBits // 8
  # read file as binary
  in_file = open(inputFile, 'rb')
  out_file = open(outputFile, 'w')
  byteArray = []
  for 16 in range(8):
    byteArray.append(in_file.read(1))

  output = decipher(state, keySchedule, numRounds)
  out_file.write()

