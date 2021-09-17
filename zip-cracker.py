import os
try:
	import zipfile
except:
	os.system("pip install zipfile")
os.system('clear')
print("""\033[1;92m
  ___________ _____  
 |___  /_   _|  __ \ 
    / /  | | | |__) |
   / /   | | |  ___/ 
  / /__ _| |_| |     
 /_____|_____|_|     
                     
                     
""")
print("\033[1;93m Author:ABIR HOSSAIN")
print()
print("\033[1;96m[1] My password list")
print("\033[1;96m[2] your password list")
print("\033[1;96m[3] exit")
print()
os.system("rm -rf ABIR-ZIP.txt")
kp=input("\033[1;92mchose option :")
if kp=='1':
	try:
		xp=input("\033[1;95mEnter zip file name :")
	except IOError:
		print("\033[1;92mzip file not found")
	print()
	print('\033[1;95mgenrariting password list.....')
	print()
	print("\033[1;94mwaite few seconde")
	wd='/sdcard/ABIR-ZIP.txt'	
	amount=(100000)
	print()
	for i in range(amount):
		file=open("ABIR-ZIP.txt","a")
		file.write(str(i)+"\n")
	print()
if kp=='3':
	exit()
if kp=='2':
	try:
		xp=input("\033[1;95mEnter zip file name :")
	except IOError:
		print("file not found")
	print()
	wd=input("\033[1;96mpassword list name :")
	print()
	print()
else:
	kp
def crack_password(password_list, obj):
    idx = 0
    with open(password_list, 'rb') as file: 

        for line in file: 

            for word in line.split(): 

                try: 

                    idx += 1

                    obj.extractall(pwd=word) 
                    print()
                    print("\033[1;93mPassword found at line", idx)
                    print('')

                    print("\033[1;92mPassword is", word.decode()) 

                    return True

                except:

                    continue

    return False
password_list = wd
zip_file = xp
obj = zipfile.ZipFile(zip_file) 
cnt = len(list(open(password_list, "rb")))
print("\033[1;96mThere are total", cnt, 

      "number of passwords to test") 
if crack_password(password_list, obj) == False:
    print()
    print("\033[1;96mPassword not found in this file") 