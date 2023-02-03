"""

Test script to ensure a new directory is made along with new sub-directories

"""


import os
import json
import shutil #for copy/overwrite permissions etc
from subprocess import PIPE, run #allows us to use all terminal commands; e.g. compiling go code
import sys

#'test' suffix present in folders; this will be removed once script has been run
TEST_DIR_PATTERN = "test"

#function to find all folders which contain the word 'test'
def find_all_test_paths(source):

	#list for test paths
	test_paths = []

	#walk through folders recursively
	for root, dirs, files in os.walk(source):
		for directory in dirs:

			if TEST_DIR_PATTERN in directory.lower():

				path = os.path.join(source, directory)
				test_paths.append(path)
		break

	return test_paths

#get name of old path and make a new one
def get_name_from_paths(paths, to_strip):

	#new name for paths
	new_names = []

	#strip old names and give directories new names
	for path in paths:

		_, dir_name = os.path.split(path)
		new_dir_name = dir_name.replace(to_strip, "")
		new_names.append(new_dir_name)


#new path for directories
def create_dir(path):

	#does the directory exist?
	if not os.path.exists(path):

		#if not, make it
		os.mkdir(path)


#for deleating directories and sub-directories: destination/target
def copy_and_overwrite(source, dest):

	#does it exist?
	if os.path.exists(dest):

		#if it does then remove it
		shutil.rmtree(dest)

	#copy source content to new folder: target
	shutil.copytree(source, dest)


#main function for source and target driectories
def main(source, target):

	#absolute pathname of the current working directory
	cwd = os.getcwd()

	#source path
	source_path = os.path.join(cwd, source)

	#target path
	target_path = os.path(cwd, target)

	#new name for paths from old ones
	new_game_dirs = get_name_from_paths(game_paths, "_game")

	#test path
	test_paths = find_all_test_paths(source_path)

	#new test directories
	new_test_dirs = get_name_from_paths(test_paths, "_test")

	#create directory for the code
	create_dir(target_path)


	#aggregate src and dest into tuple
	for src, dest in zip(test_paths, new_test_dirs):


		#destination
		dest_path = os.path.join(target_path, dest)

		#overwrite the old paths
		copy_and_overwrite(src, dest_path)

    
if __name__ == "__main__":

	args = sys.argv

	#there needs to be 3 arguments: script, source, target (destination) folders
	if len(args) != 3:

		raise Exception("You need to specify 'source' and 'target'. The script represents the 1st one")

		#i.e. $ python3 main.py source target


	#args[1] = <file.py>; args[2] = source; args[3] = target
	source, target = args[1:]

	#call main
	main(source, target)
