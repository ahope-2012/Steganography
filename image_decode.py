import main
import cv2
import re
import os
from cryptography.fernet import Fernet

def decode():
	print("\n-----------------------------")
	print("|     Decoding Starts..     |")
	print("-----------------------------\n")

	while True: # Asks the user for a carrier name, if none exists returns to start
		image = input("Enter image carrier name (inc. extension)...\n")
		if not image:
			print('Nothing has been Entered!\n')
			continue
		elif not os.path.isfile(image):
			print("\nNo file exists, try again!\n")
			continue
		else:
			break

	image = cv2.imread(image) # read the image
	bank_secretMessage = "" # Holds LSB secret message, (Red pixel)
	
	# Extract LSB and store in binary_data[x]
	for row in image:
		for pixel in row:
			r, g, b = [ format(i, "08b") for i in pixel ]
			bank_secretMessage += r[-1]
			bank_secretMessage += g[-1]
			bank_secretMessage += b[-1]

	# Divide all LSB and convert to charcters
	all_data_secretMessage = [ bank_secretMessage[i: i+8] for i in range(0, len(bank_secretMessage), 8) ]
	decoded_secretMessage = ""

	for byte in all_data_secretMessage:
		decoded_secretMessage += chr(int(byte, 2))

	# Finds the first delimiter, then removes the last 5 chars
	secretMessage = decoded_secretMessage.split("SdfD1")[1] #[:-5]
	# Takes the secretMessage splits backwards to recover the message, then removes the last 5 chars 
	split_1 = secretMessage.split("e1g0l")[1][:-5]
	# Takes the secretMessage splits forwards to recover the key
	split_2 = secretMessage.split("e1g0l")[0]

	decoded = Fernet(split_1).decrypt(split_2.encode()) # Decrypt with key

	print("\n*************************")
	print("*     Secret Message    *")
	print("*************************")
	print(re.sub("(.{40})", "\\1\n", decoded.decode())) # Prints secret message and displays 40 characters on CLI

	#print(decoded_data[:-5]) # Displays decoded message full width

	main.main() # Returns to main menu
