import os
import sys
import hashlib
import binascii

def find_all(hexdata, sub):
    start = 0
    return_list = []
    while True:
        start = hexdata.find(sub, start)
        if start == -1:
            break
        return_list.append(start)
        start += len(sub)
    return return_list

def extract_jpg(hexdata):
    start_of_jpg = find_all(hexdata, "ffd8ff")
    end_of_jpg = find_all(hexdata, "ffd9")

    file_no = 0
    # start writing the files
    for start in start_of_jpg:
        for end in end_of_jpg:
            if start < end:
                # write code to save the file and hash
                res = hexdata[start:end]
                res = res.replace(" ",".").encode('utf-8')
                try:
                    res = binascii.unhexlify(res)
                except binascii.Error:
                    pass
                new_file = open(os.path.join('Joshy/JPG','File_'+str(file_no)+'.jpg'),"wb")
                new_file.write(res)
                hasher = hashlib.sha256(res).hexdigest()
                hash_file = open(os.path.join('Joshy/JPG','Hashes.txt'),"a")
                hash_file.write(hasher+"\n")
                print("-----------------------------Successfully Carved File------------------------------\n")
                print("File Type: JPG\n")
                size_carve = len(res)
                print('The size of the carved file: ' + str(size_carve) + ' bytes\n')
                print('The location offset of the carved file: '+str(start)+' : '+str(end)+'\n')
                file_no = file_no + 1

def extract_jpeg(hexdata):
    start_of_jpeg = find_all(hexdata, "ffd8ff")
    end_of_jpeg = find_all(hexdata, "ffd9")

    file_no = 0
    # start writing the files
    for start in start_of_jpeg:
        for end in end_of_jpeg:
            if start < end:
                # write code to save the file and hash
                res = hexdata[start:end]
                res = res.replace(" ",".").encode('utf-8')
                try:
                    res = binascii.unhexlify(res)
                except binascii.Error:
                    pass
                new_file = open(os.path.join('Joshy/JPEG','File_'+str(file_no)+'.jpeg'),"wb")
                new_file.write(res)
                hasher = hashlib.sha256(res).hexdigest()
                hash_file = open(os.path.join('Joshy/JPEG','Hashes.txt'),"a")
                hash_file.write(hasher+"\n")
                print("-----------------------------Successfully Carved File------------------------------\n")
                print("File Type: JPEG\n")
                size_carve = len(res)
                print('The size of the carved file: ' + str(size_carve) + ' bytes\n')
                print('The location offset of the carved file: '+str(start)+' : '+str(end)+'\n')
                file_no = file_no + 1


def extract_png(hexdata):
    start_of_png = find_all(hexdata, "89504e470d0a1a0a")
    end_of_png = find_all(hexdata, "49454e44ae426082")
    file_no = 0
    # start writing the files
    for start in start_of_png:
        for end in end_of_png:
            if start < end:
                # write code to save the file and hash
                res = hexdata[start:end]
                res = res.replace(" ",".").encode('utf-8')
                try:
                    res = binascii.unhexlify(res)
                except binascii.Error:
                    pass
                new_file = open(os.path.join('Joshy/PNG','File_'+str(file_no)+'.png'),"wb")
                new_file.write(res)
                hasher = hashlib.sha256(res).hexdigest()
                hash_file = open(os.path.join('Joshy/PNG','Hashes.txt'),"a")
                hash_file.write(hasher+"\n")
                print("-----------------------------Successfully Carved File-----------------------------\n")
                print("File Type: PNG\n")
                size_carve = len(res)
                print('The size of the carved file: ' + str(size_carve) + ' bytes\n')
                print('The location offset of the carved file: '+str(start)+' : '+str(end)+'\n')
                file_no = file_no + 1

def main():
    filename = input("Enter filename(with extension): ")
    file = open(filename, "rb").read()
    hexdata = str(binascii.hexlify(file))

    os.makedirs('Joshy/JPG')
    os.makedirs('Joshy/JPEG')
    os.mkdir('Joshy/PNG')

    extract_jpg(hexdata)
    extract_jpeg(hexdata)
    extract_png(hexdata)

if __name__ == '__main__':
    main()
