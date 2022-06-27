import main
import cv2
import sys
import string
import random
import os
from cryptography.fernet import Fernet

def encode():
	print("\n-----------------------------")
	print("|     Encoding Starts..     |")
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

	image = cv2.imread(image) # Loads image from specified 
	max_bytes = (image.shape[0] * image.shape[1]) // 8 # maximum bytes to encode

	while True: # Asks the user for the secret message, if none exists returns to start
		secret_data = input("\nEnter secret message...\n")
		if not secret_data:
			print('Nothing has been Entered!\n')
			continue
		else:
			key = Fernet.generate_key() # Generates a key
			f = Fernet(key) # Assigns variable 
			secret_data = f.encrypt(secret_data.encode()) # Encrypts secret message based on key

			secret_data = str(secret_data.decode()) + "e1g0l" # Adds an end delimiter to the message
			secret_data = "SdfD1" + secret_data + str(key.decode()) # Adds a start delimiter to the message
			secret_data = secret_data + "m1Ku1"
			#print(secret_data, "\n") # Test variable

			if len(secret_data) > max_bytes | len(key) > max_bytes:
				print("\n------------ ERROR ------------")		
				print("Secret message is too big for the carrier")
				print("Try a bigger carrier or smaller message\n")
				main.main() # returns to main menu

			# Finds out the total amount of duplicate secret messages that can be embedded
			sizeOfMessage = sys.getsizeof(secret_data)
			lengthmessage = max_bytes//sizeOfMessage
			new_Secret_Data = secret_data * lengthmessage # Muliplies the secret message
			break # Else continues

	while True: # Asks the user for a new image name, if none exists returns to start
		newfile = input("\nEnter new image name (inc. extension)...\n")
		if not newfile:
			print('Nothing has been Entered!\n')
			continue
		else:
			break

	bank_secretMessage = 0 # Set index values to zero
	b_secretMessage = ''.join([ format(ord(i), "08b") for i in new_Secret_Data ]) # Converts the secret message & key to binary
	len_secretMessage = len(b_secretMessage) # Size of data to hide

	for row in image:
		for pixel in row:
			r, g, b = [ format(i, "08b") for i in pixel ] # Converts RGB pixels to binary
			if bank_secretMessage < len_secretMessage: # If data count is less than length
				pixel[0] = int(r[:-1] + b_secretMessage[bank_secretMessage], 2) # Modify the LSB (Red pixel)
				bank_secretMessage += 1 # Increase count

			if bank_secretMessage < len_secretMessage: # If data count is less than length
				pixel[1] = int(g[:-1] + b_secretMessage[bank_secretMessage], 2) # Modify the LSB (Green pixel)
				bank_secretMessage += 1 # Increase count

			if bank_secretMessage < len_secretMessage: # If data count is less than length
				pixel[2] = int(b[:-1] + b_secretMessage[bank_secretMessage], 2) # Modify the LSB (Blue pixel)
				bank_secretMessage += 1 # Increase count

			# If all data counts are greaterr than lengths
			if bank_secretMessage >= len_secretMessage:
				break

	cv2.imwrite(newfile, image) # Process to write a new image file, newfile = the new image name, image = the image data

	print("\nSteganography encoding complete!")

	main.main()
