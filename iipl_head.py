# encoding: utf8
import os,sys

#中文路径问题
reload(sys)
sys.setdefaultencoding('utf-8')

#add file head to .iipl
def add_head(file_path):
	# file_path = str(file_path)
	if os.path.exists(file_path) == False:
		print "ERROR: image path not exist:" + str(file_path)
		return

	with open(file_path,'rb') as fin:
		lines = fin.readlines()
	with open(file_path,'wb') as fout:
		fout.write('iiplbest\n')	
		fout.writelines(lines)


# remove file head with .iipl
def remove_head(file_path):
	# file_path = str(file_path)
	if os.path.exists(file_path) == False:
		print "ERROR: image path not exist:" + str(file_path)
		return
		
	with open(file_path,'rb') as fin:
		lines = fin.readlines()
	with open(file_path,'wb') as fout:
		if lines[0] == 'iiplbest\n':
			fout.writelines(lines[1:])
		else:
			print "ERROR: this file is not a .iipl file."	
			# print lines[0]
			fout.writelines(lines)
