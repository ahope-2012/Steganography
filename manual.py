import main

def manual(): # Print out for manual
	print("\n-----------------------------")
	print("|          Manual           |")
	print("-----------------------------\n")
	print("Audio files known to work...")
	print("WAV, AIFF\n")
	print("Image files known to work...")
	print("PNG, TIFF, BMP\n")
	print("When the CLI first loads, you will be presented...")
	print("with the 'Menu Menu' this will present 4 options.\n")
	print("Option 1 - Will take you to the audio section.")
	print("           3 options, encode, decode & back.\n")
	print("Option 2 - Will take you to the image section.")
	print("           3 options, encode, decode & back.\n")
	print("Option 3 - Is the section you are currently in.")
	print("           To exit press 'y' or 'Y'.\n")
	print("Option 4 - Will quit the program.\n")
	print("Audio and Image Encoding -")
	print("	Both these sections work in a similar way. This")
	print("	will ask for a carrier name, ensure that it has")
	print("	a file extension at the end. Next, it will ask")
	print("	for the secret message. Then finally, it will")
	print("	ask for the steg file name and extension.\n")
	print("Audio and Image Decoding -")
	print("	Again, both these sections work in a similar way.")
	print("	This will ask for the steg carrier name, ensure ")
	print("	that it has a file extension at the end. Next, it")
	print("	will display the secret message embedded inside.\n")
	print("The thrid option in both the audio and image")
	print("sections, is a way to return to the 'Main Menu'.\n\n")

	lower = "y" # Lower case y variable
	upper = "Y" # Upper case Y variable

	while True: # Loop to exit manual.py
		valexit = input("\nPress 'Y' to exit: ")
		if not valexit:
			print('Nothing has been Entered!\n')
			continue # Loops if nothing has been entered
		elif valexit == lower:
			main.main() # Only exits if lower case
		elif valexit == upper:
			main.main() # Only exits if upper case
		else:
			print("\nEnter valid choice!")
			continue # Loops if invalid choice
			