#!/usr/bin/python3
#coding:utf-8

import re
import csv
import sys

def separate(filename,repo,keys):
	new_list = []
	mark = ['(A)','(B)','(C)','(D)','(E)']
	f = open(repo+'/'+filename)
	for i in f:
		if "valign='top'" in i:
			new_dict, k = {}, []
			i = i.strip('\n').split('td valign')[1]+'<'
			i = re.findall('>(.*?)<', i)
			for j in i:
				if j != '':
					k.append(j)

			line = k[-1]
			del k[-1]
			for j in mark:
				if j in line:
					state = line.find(j)
					k.append(line[:state])
					line = line[state+3:]
			k.append(line)
			# print(line)
			if(len(k) == 7): # They are datas we want
				new_dict['file'] = filename
				new_dict['Question'] = k[2]
				new_dict['Option'] = k[3:7]
				new_dict['Answer'] = k[1]
				new_list.append(new_dict)
	return new_list

def main():
	with open(sys.argv[1]+'_output.csv', 'w', newline='') as csvfile:
		keys = ['file','Question','Option','Answer']
		writer = csv.DictWriter(csvfile,fieldnames = keys)

		for line in sys.stdin:
			for name in line.rstrip().split(' '):
				new_list = separate(name,sys.argv[1],keys)

				for i in new_list:
					writer.writerow(i)
    
if __name__ == "__main__":
    main()