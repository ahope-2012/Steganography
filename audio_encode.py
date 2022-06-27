import wave
import main
import sys
import os
from cryptography.fernet import Fernet

def encode():
	print("\n-----------------------------")
	print("|     Encoding Starts..     |")
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

	location = audio # Used as a string variable for location
	audio = wave.open(audio,mode="rb") # Opens audio file as a binary file
	numberChannels = audio.getnchannels() # Returns all channels in the audio file
	numberFrames = audio.getnframes() # Returns number of audio frames 
	numberSample = numberFrames*numberChannels # First data to gather max bytes
	maxBytes = (numberSample*1)//8 # Takes previous data * LSB then divides for each byte

	while True: # Asks the user for the secret message, if none exists returns to start
		sMessage = input("\nEnter secret message...\n")
		if not sMessage:
			print('Nothing has been Entered!\n')
			continue
		else: 
			key = Fernet.generate_key() # Generates a key
			f = Fernet(key) # Assigns variable 
			sMessage = f.encrypt(sMessage.encode()) # Encrypts secret message based on key
			#print(sMessage, "\n") # Test variable

			sMessage = "e1g0l" + sMessage.decode() # Adds a delimiter to the secret message
			#print(sMessage, "\n") # Test variable

			sMessage = sMessage + "m1Ku1" # Adds a delimiter to the secret message
			#print(sMessage, "\n") # Test variable

			sMessage = sMessage + key.decode() # Adds the key to the secret message
			#print(sMessage, "\n") # Test variable

			sMessage = sMessage + "?????" # Adds a delimiter to the secret message
			#print(sMessage, "\n") # Test variable

			sizeOfMessage = sys.getsizeof(sMessage) # Gets the size of the message + delimiter 
			#print(sizeOfMessage)
			if sizeOfMessage > maxBytes: # if message is too big for carrier
				print("\n------------ ERROR ------------")		
				print("Secret message is too big for the carrier")
				print("Try a bigger carrier or smaller message\n")
				main.main() # returns to main menu

			# Finds out the total amount of duplicate secret messages that can be embedded
			lengthmessage = maxBytes//sizeOfMessage 
			sMessage = sMessage *lengthmessage # Muliplies the secret message
			break # Else continues

	while True: # Asks the user for a new audio name, if none exists returns to start
		newfile = input("\nEnter new audio name (inc. extension)...\n")
		if not newfile:
			print('Nothing has been Entered!\n')
			continue
		else:
			break

	fBytes = bytearray(list(audio.readframes(audio.getnframes()))) # Read audio and convert to byte array
	bAudio = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in sMessage]))) # Text to bit array

	for i, bit in enumerate(bAudio): # Replace LSB of each byte from audio to one bit from sMessage
	    fBytes[i] = (fBytes[i] & 254) | bit

	frameChange = bytes(fBytes) # Gathers all bytes (including modified)

	newAudio =  wave.open(newfile, 'wb') # Process to write a new audio file
	newAudio.setparams(audio.getparams()) # Process to write a new audio file
	newAudio.writeframes(frameChange) # Process to write a new audio file

	newAudio.close() # Close newAudio
	audio.close() # Close Audio

	print("\nSteganography encoding complete!")

	main.main() # Returns to main menu
	