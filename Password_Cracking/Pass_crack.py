# Import libraries
import hashlib
import sys
import time

# Function for Brute-Force Attack
def brute():
	hash_input = input("\nEnter the hash value: ")
	LIST = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*)(-_=+][}{|;:'.>,</?"
	start_time = time.time()
	count = 1


	for word in LIST:
		enc_word = word.encode('utf-8')
		hash_comp = hashlib.md5(enc_word.strip()).hexdigest()
		if hash_comp == hash_input:
			print("\n-------------------------PASSWORD FOUND-------------------------")
			print("\nThe cracked password is: " + word)
			end_time = time.time() - start_time
			print("\nThe time taken to crack the password is: " + str(end_time) + " sec")
			print("\nThe number of attemped passwords: " + str(count))
			print("\n----------------------------------------------------------------")
			quit()
		else:
			count = count + 1
			continue

	for i in LIST:
		for j in LIST:
			word = i+j
			enc_word = word.encode('utf-8')
			hash_comp = hashlib.md5(enc_word.strip()).hexdigest()
			if hash_comp == hash_input:
				print("\n-------------------------PASSWORD FOUND-------------------------")
				print("\nThe cracked password is: " + word)
				end_time = time.time() - start_time
				print("\nThe time taken to crack the password is: " + str(end_time) + " sec")
				print("\nThe number of attemped passwords: " + str(count))
				print("\n----------------------------------------------------------------")
				quit()
			else:
				count = count + 1
				continue
	
	for i in LIST:
		for j in LIST:
			for k in LIST:
				word = i+j+k
				enc_word = word.encode('utf-8')
				hash_comp = hashlib.md5(enc_word.strip()).hexdigest()
				if hash_comp == hash_input:
					print("\n-------------------------PASSWORD FOUND-------------------------")
					print("\nThe cracked password is: " + word)
					end_time = time.time() - start_time
					print("\nThe time taken to crack the password is: " + str(end_time) + " sec")
					print("\nThe number of attemped passwords: " + str(count))
					print("\n----------------------------------------------------------------")
					quit()
				else:
					count = count + 1
					continue

	print("\nPASSWORD: @User, You are not far from me !!!")
	for i in LIST:
		for j in LIST:
			for k in LIST:
				for l in LIST:
					word = i+j+k+l
					enc_word = word.encode('utf-8')
					hash_comp = hashlib.md5(enc_word.strip()).hexdigest()
					if hash_comp == hash_input:
						print("\n-------------------------PASSWORD FOUND-------------------------")
						print("\nThe cracked password is: " + word)
						end_time = time.time() - start_time
						print("\nThe time taken to crack the password is: " + str(end_time) + " sec")
						print("\nThe number of attemped passwords: " + str(count))
						print("\n----------------------------------------------------------------")
						quit()
					else:
						count = count + 1
						continue
	
	print("\nPASSWORD: @User, Wait for me... Here I come !!!")
	for i in LIST:
		for j in LIST:
			for k in LIST:
				for l in LIST:
					for m in LIST:
						word = i+j+k+l+m
						enc_word = word.encode('utf-8')
						hash_comp = hashlib.md5(enc_word.strip()).hexdigest()
						if hash_comp == hash_input:
							print("\n-------------------------PASSWORD FOUND-------------------------")
							print("\nThe cracked password is: " + word)
							end_time = time.time() - start_time
							print("\nThe time taken to crack the password is: " + str(end_time) + " sec")
							print("\nThe number of attemped passwords: " + str(count))
							print("\n----------------------------------------------------------------")
							quit()
						else:
							count = count + 1
							continue

	print("\nPASSWORD: @User, You will have to wait longer to find me !!!")
	for i in LIST:
		for j in LIST:
			for k in LIST:
				for l in LIST:
					for m in LIST:
						for n in LIST:
							word = i+j+k+l+m+n
							enc_word = word.encode('utf-8')
							hash_comp = hashlib.md5(enc_word.strip()).hexdigest()
							if hash_comp == hash_input:
								if flag == 1:
									print("\n-------------------------PASSWORD FOUND-------------------------")
									print("\nThe cracked password is: " + word)
									end_time = time.time() - start_time
									print("\nThe time taken to crack the password is: " + str(end_time) + " sec")
									print("\nThe number of attemped passwords: " + str(count))
									print("\n----------------------------------------------------------------")
									quit()
								else:
									print("\n--------------- PASSWORD: @USER, YOU CAN'T FIND ME...BETTER LUCK NEXT TIME... ---------------")
							else:
								count = count + 1
								continue

# Function for Dictionary Attack
def dictonary():
	hash_input = input("\nEnter the hash value: ")
	word_list = input("\nEnter the filename with the wordlist: ")
	start_time = time.time()
	flag = 0

	try:
		file = open(word_list,'r')
	except:
		print("\nFile not found!!!")
		quit()

	for word in file:
		enc_word = word.encode('utf-8')
		hash_comp = hashlib.md5(enc_word.strip()).hexdigest()
		if hash_comp == hash_input:
			print("\n-------------------------PASSWORD FOUND-------------------------")
			print("\nThe cracked password is: " + word)
			end_time = time.time() - start_time
			print("\nThe time taken to crack the password is: " + str(end_time) + " sec")
			print("\n----------------------------------------------------------------")
			flag = 1
			break
	if flag == 0:
		print("\nPassword: @User, I am not in the wordlist !!")

# Function to select options
def option():
	while True:
		print("\nChoose a password cracking method from the options given below:\n")
		print("    1. Brute-Force Attack")
		print("    2. Dictionary Attack")
		print("    3. Exit")
		options = input("\nEnter your option: ")
		if 1 <= int(options) <= 3:
			return options
		else:
			print("\nOops !!! Wrong Option... \n\nChoose Again...")
			
# Main program
while True:
	opt = int(option())
	if opt == 1:
		brute()
	elif opt == 2:
		dictonary()
	elif opt == 3:
		print("\nSad to see you leaving the program !!!")
		quit()