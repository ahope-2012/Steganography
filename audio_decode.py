import wave
import main
import re
import os
from cryptography.fernet import Fernet

def decode():
	print("\n-----------------------------")
	print("|     Decoding Starts..     |")
	print("-----------------------------\n")

	while True: # Asks the user for a carrier name, if none exists returns to start
		audio = input("Enter audio carrier name (inc. extension)...\n")
		if not audio:
			print('Nothing has been Entered!\n')
			continue
		elif not os.path.isfile(audio):
			print("\nNo file exists, try again!\n")
			continue
		else:
			break

	audio = wave.open(audio,mode="rb") # Opens audio file as a binary file
	fBytes = bytearray(list(audio.readframes(audio.getnframes()))) # Read audio and convert to byte array

	hiddenBytes = [fBytes[i] & 1 for i in range(len(fBytes))] # Extract LSB
	sMessage = "".join(chr(int("".join(map(str,hiddenBytes[i:i+8])),2)) for i in range(0,len(hiddenBytes),8)) # Convert to string

	#print(sMessage[0:400], "\n") # Test variable

	split_1 = sMessage.split("e1g0l")[1] # Removes the first delimiter 
	#print(split_1[0:400], "\n") # Test variable

	split_2 = split_1.split("m1Ku1")[0] # Finds the middle delimiter for encrypted secret message
	#print(split_2[0:400], "\n") # Test variable

	split_3 = split_1.split("m1Ku1")[1] # Removes the middle delimiter for key
	#print(split_3[0:400], "\n") # Test variable

	split_4 = split_3.split("SdfD1")[0] # Removes the last delimiter 
	#print(split_4[0:400], "\n") # Test variable

	decoded = Fernet(split_4).decrypt(split_2.encode()) # Decrypt with key

	print("\n*************************")
	print("*     Secret Message    *")
	print("*************************")
	print(re.sub("(.{40})", "\\1\n", decoded.decode())) # Prints secret message and displays 40 characters on CLI

	#print(decoded.decode()) # Displays decoded message full width

	audio.close() # Close Audio

	main.main() # Returns to main menu
