# Import Libraries
import binascii
import hashlib
import os
import sys

# Function for Embed Method
def embed(file, filename, data, hexdata, hextext):

	if '89504e470d0a1a0a' in hexdata:
		line = data+hextext
		unhex_file = binascii.unhexlify(line)
		newfile = open(filename[:-4]+'_hide.png',"wb")
		newfile.write(unhex_file)
		print("\n------------------------------ORIGINAL FILE INFO------------------------------\n")
		print('Original Filename: '+filename)
		size = os.path.getsize(filename)
		print('The size of the original file: ' + str(size) + ' bytes')
		hasher = hashlib.sha256(file).hexdigest()
		print('The hash value of the original file: ' + str(hasher))
		print("\n------------------------------MODIFIED FILE INFO------------------------------\n")
		print('Modified Filename: '+filename[:-4]+'_hide.png')
		size_mod = os.path.getsize(filename[:-4]+'_hide.png')
		print('The size of the modified file: ' + str(size_mod) + ' bytes')
		hasher = hashlib.sha256(unhex_file).hexdigest()
		print('The hash value of the modified file: ' + str(hasher))

	elif '.jpg' in filename:
		if 'ffd8' in hexdata:
			line = data+hextext
			unhex_file = binascii.unhexlify(line)
			newfile = open(filename[:-4]+'_hide.jpg',"wb")
			newfile.write(unhex_file)
			print("\n------------------------------ORIGINAL FILE INFO------------------------------\n")
			print('Original Filename: '+filename)
			size = os.path.getsize(filename)
			print('The size of the original file: ' + str(size) + ' bytes')
			hasher = hashlib.sha256(file).hexdigest()
			print('The hash value of the original file: ' + str(hasher))
			print("\n------------------------------MODIFIED FILE INFO------------------------------\n")
			print('Modified Filename: '+filename[:-4]+'_hide.jpg')
			size_mod = os.path.getsize(filename[:-4]+'_hide.jpg')
			print('The size of the modified file: ' + str(size_mod) + ' bytes')
			hasher = hashlib.sha256(unhex_file).hexdigest()
			print('The hash value of the modified file: ' + str(hasher))

	elif '.jpeg' in filename:
		if 'ffd8' in hexdata:
			line = data+hextext
			unhex_file = binascii.unhexlify(line)
			newfile = open(filename[:-5]+'_hide.jpeg',"wb")
			newfile.write(unhex_file)
			print("\n------------------------------ORIGINAL FILE INFO------------------------------\n")
			print('Original Filename: '+filename)
			size = os.path.getsize(filename)
			print('The size of the original file: ' + str(size) + ' bytes')
			hasher = hashlib.sha256(file).hexdigest()
			print('The hash value of the original file: ' + str(hasher))
			print("\n------------------------------MODIFIED FILE INFO------------------------------\n")
			print('Modified Filename: '+filename[:-5]+'_hide.jpeg')
			size_mod = os.path.getsize(filename[:-4]+'_hide.jpeg')
			print('The size of the modified file: ' + str(size_mod) + ' bytes')
			hasher = hashlib.sha256(unhex_file).hexdigest()
			print('The hash value of the modified file: ' + str(hasher))

# Function to find the location of EOF value
def find_all(hexdata, sub):
    count = 0
    my_list = []
    while True:
        count = hexdata.find(sub, count)
        if count == -1:
            break
        my_list.append(count)
        count = count + 1
    return my_list

# Function for Extract Method
def extract(filename, file, data, hexdata):

	if '.png' in filename:
		extra = "49454e44ae426082"
		pos = hexdata.find(extra)
		line = data[pos+len(extra)-2:]
		unhex_file = binascii.unhexlify(line)
		newfile = open(filename[:-4]+'_found.txt',"wb")
		newfile.write(unhex_file)
		print("\n------------------------------ORIGINAL FILE INFO------------------------------\n")
		print('Original Filename: '+filename)
		size = os.path.getsize(filename)
		print('The size of the original file: ' + str(size) + ' bytes')
		hasher = hashlib.sha256(file).hexdigest()
		print('The hash value of the original file: ' + str(hasher))

	elif '.jpg' in filename:
		loc_eof = find_all(hexdata, "ffd9")
		sub = "ffd9"
		loc = loc_eof[-1]
		line = data[loc+len(sub)-2:]
		unhex_file = binascii.unhexlify(line)
		newfile = open(filename[:-4]+'_found.txt',"wb")
		newfile.write(unhex_file)
		print("\n------------------------------ORIGINAL FILE INFO------------------------------\n")
		print('Original Filename: '+filename)
		size = os.path.getsize(filename)
		print('The size of the original file: ' + str(size) + ' bytes')
		hasher = hashlib.sha256(file).hexdigest()
		print('The hash value of the original file: ' + str(hasher))

	elif '.jpeg' in filename:
		loc_eof = find_all(hexdata, "ffd9")
		sub = "ffd9"
		loc = loc_eof[-1]
		line = data[loc+len(sub)-2:]
		unhex_file = binascii.unhexlify(line)
		newfile = open(filename[:-5]+'_found.txt',"wb")
		newfile.write(unhex_file)
		print("\n------------------------------ORIGINAL FILE INFO------------------------------\n")
		print('Original Filename: '+filename)
		size = os.path.getsize(filename)
		print('The size of the original file: ' + str(size) + ' bytes')
		hasher = hashlib.sha256(file).hexdigest()
		print('The hash value of the original file: ' + str(hasher))


# Function to select options from the user and converting input file to binary and hex files and calling appropriate functions
def main():
	while True:
		print("\nChoose a stegnography method from options given below:\n")
		print("		1. Embed Method")
		print("		2. Extract Method")
		print("		3. Exit")
		options = input("\n Enter your choice: ")

		if int(options) == 1:
			filename = input("Enter the filename(with extension): ")
			file = open(filename, "rb").read()
			data = binascii.hexlify(file)
			hexdata = str(data)

			text = input("\n Enter the secret text you want to embed into the file: ")
			text = text.encode('utf-8')
			hextext = binascii.hexlify(text)

			embed(file, filename, data, hexdata, hextext)

		elif int(options) == 2:
			filename = input("Enter the secret embedded filename(with extension): ")
			file = open(filename, "rb").read()
			data = binascii.hexlify(file)
			hexdata = str(data)

			extract(filename, file, data, hexdata)

		elif int(options) == 3:
			print("\nYou are exiting from the program!")
			quit()
		else:
			print("\n Wrong Option! \n\n Choose Again...")

# Main Program
if __name__ == '__main__':
    main()

		
