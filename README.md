# AESEncryption
AES Encryption assignment for CS361


**Python 3 must be installed**

```
$ python3 ./aesEncryption.py --keysize $KEYSIZE --keyfile $KEYFILE --inputfile $INPUTFILE --outputfile $OUTFILENAME --mode $MODE
```

> aesEncryption.py

This file takes in the system arguments for the AES Encryption and then starts the process depending on the arguments

> encrypt.py

This file creates the key schedule and reads the file. If the number of bytes in the file is not an even number then it pads the file with the proper amount of bytes needed. It also pads the file with the rest of the numbers set as (16 - num_bytes % 16) in order for the decryption algoritm to know what the original padding of the message is set to. It then starts the algorithm by taking in a chunk (16 bytes) and running the cipher on each chunk. 

>cipher.py

subBytes: makes it so that each byte in the state is replaced with its entry in a fixed 8-bit lookup table called [sBox](https://en.wikipedia.org/wiki/Rijndael_S-box "Wikipedia for Rijndael S-box"). 

shiftRows: shifts the bytes in each row of the state in a fixed manner

mixColumns: each column of the state is multiplied with a [fixed polynomial equation](https://en.wikipedia.org/wiki/Rijndael_MixColumns "Wikipedia for Rijndael MixColumns")

cipher: Starts the modifying of each chunk of code by calling addRoundKey and then for either 9 or 13 rounds it calls subBytes, shiftRows, mixColumns, and addRoundKey, then on the last round it only calls subBytes, shiftRows, and addRoundKey

> decrypt.py

This file creates the key schedule and reads the file and ouputs a decrypted file. The number of bytes in the file will be an even 16 so it takes the last byte in the last chunk and checks the value of it so that it knows how many bytes the original file was padded with.

>decipher.py

inv_sub_bytes: makes it so that each byte in the state is replaced with its entry in a fixed 8-bit lookup table called [sBox](https://en.wikipedia.org/wiki/Rijndael_S-box "Wikipedia for Rijndael S-box"). 

shift_rows: shifts the bytes in each row of the state in a fixed manner

inv_mix_columns: each column of the state is multiplied with a [fixed polynomial equation](https://en.wikipedia.org/wiki/Rijndael_MixColumns "Wikipedia for Rijndael MixColumns")

decipher: Starts the modifying of each chunk of code by calling addRoundKey and then for either 9 or 13 rounds it calls inv_shift_rows, inv_sub_bytes, addRoundKey, and inv_mix_columns then on the last round it only calls inv_shift_rows, inv_sub_bytes, and addRoundKey

>keyschedule.py

keyExpansion: AES Encyrption uses a key schedule to expand a short key into a number of separate round keys based on the idea found [here](https://en.wikipedia.org/wiki/Rijndael_key_schedule "Rijndael Key Schedule Wiki"). Also used by both encrypt.py and decrypt.py.

subWord: helper function for keyExpansion that applies the S-box transformation for every word

rotWord: helper function for keyExpansion that rotates every word one byte to the left

addRoundKey: each byte of the state is added (via XOR) with one in the key schedule
