#!/usr/bin/env python3
import os
import sys


def main():
	folder = sys.argv[1]
	files = os.listdir(folder)
	
	for f in files:
		input_file = open(folder +'/'+ f,'r')
		texto = input_file.read()
		print(texto)
		input_file.close()
		#teste


main()