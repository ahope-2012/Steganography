import audio_encode
import audio_decode
import image_encode
import image_decode
import manual

def main(): # Main menu
	print("\n-----------------------------")
	print("|         Main Menu         |")
	print("-----------------------------")
	print("\nSelect an option: \n1)Audio\n2)Image\n3)Manual\n4)exit")
	valMain = input("\nOption:")
	if valMain == "1":
		audio()
	elif valMain == "2":
		image()
	elif valMain == "3":
		manual.manual()
	elif valMain == "4":
		quit()
	else:
		print("\nEnter valid choice!")
		main()

def audio(): # Audio menu
	print("\n-----------------------------")
	print("|         Audio Menu        |")
	print("-----------------------------")
	print("\nSelect an option: \n1)Encode\n2)Decode\n3)Main Menu")
	valAudio = input("\nOption:")
	if valAudio == "1":
		audio_encode.encode()
	elif valAudio == "2":
		audio_decode.decode()
	elif valAudio == "3":
		main()
	else:
		print("\nEnter valid choice!")
		audio()

def image(): # Image menu
	print("\n-----------------------------")
	print("|         Image Menu        |")
	print("-----------------------------")
	print("\nSelect an option: \n1)Encode\n2)Decode\n3)Main Menu")
	valImage = input("\nOption:")
	if valImage == "1":
		image_encode.encode()
	elif valImage == "2":
		image_decode.decode()
	elif valImage == "3":
		main()
	else:
		print("\nEnter valid choice!")
		image()

def cover(): # Cover art
	print("                                                                             ")
	print("                                                                             ")
	print("              .d       .d8800b.  88008800b.                                  ")
	print("              00       88        00      88                                  ")
	print("              88       00        88  88  8P                                  ")
	print("              00       `80088b.  00     K                                    ")
	print("              88             00  88  00  b.                                  ")
	print("              00             88  00      88     IMAGE & AUDIO                ")
	print("              `80088b. d800880P  880088008P     STEGANOGRAPHY                ")
	print("                                                                             ")
	print("              Least Significant Bit                                          ")
	print("                                                                             ")
	print("                                                                             ")
	print("        A command line interface for image and audio steganography...        ")
	print("                                                                             ")
	main()


if __name__ == "__main__":
    cover()
    