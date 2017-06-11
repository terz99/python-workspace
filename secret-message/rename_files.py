import os

def rename_files():
	file_list = os.listdir(r'/home/dushan/Desktop/prank/prank')

	saved_path = os.getcwd()
	os.chdir(r'/home/dushan/Desktop/prank/prank')
	print("Current working directory is " + os.getcwd())

	for file_name in file_list:
		os.rename(file_name, file_name.translate(str.maketrans('', '', '0123456789')))

	os.chdir(saved_path)

rename_files()