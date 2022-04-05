import glob
import sys
import subprocess
from pathlib import Path
import re

given_file = sys.argv[1]

fp1 = open(given_file,'r')
morph_lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file

sentence = []
drel = []
vib = []
for morph_line in morph_lines:
	if(not re.search('\(\(', morph_line) and not re.search(r'\)\)', morph_line) and re.search(r'\t', morph_line)):
		sentence.append(morph_line.split("\t")[1])
		if(not re.search(r'PUNC', morph_line)):
			morph_line = re.sub(r'^.*<fs af=\'(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*)\' .*', r'\1(\7)', morph_line)
			vib.append(morph_line)
	if(re.search(r'drel', morph_line)):
		morph_line = re.sub(r'^.*drel', 'drel', morph_line)
		morph_line = re.sub(r'>', '', morph_line)
		drel.append(morph_line)

final_sentence = ' '.join(sentence)
final_drel = ' '.join(drel)
final_vib = ' '.join(vib)

if(re.search(r'\ \।\ ', final_sentence)):
    final_sentence = re.sub(r'\ \।\ ', '। \n',final_sentence)
	
print("\nHindi Sentence:\n", final_sentence)
print("\nKarakas/Dependency relation in Sentence are :\n",final_drel)
print("\nVibhakti/Case Marker in Sentence word by word () are :\n",final_vib)
print('\n')
		
