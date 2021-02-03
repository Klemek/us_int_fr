from os import listdir, remove

# get last version of french file
inp = sorted([f for f in listdir() if f.startswith('usinfr')])[-1]
out = 'usinen' + inp[6:]

# delete english layout
for f in sorted([f for f in listdir() if f.startswith('usinen')]):
	remove(f)

lines = []
	
# copy file and add changes
with open(inp,  encoding='utf8', mode='r') as finp:
	with open(out,  encoding='utf8', mode='w') as fout:
		for line in finp:
			line = line.strip()
			lines += [line]
			if line.startswith('KBD'):
				line = line[:4] + out[:8] + '\t"EN' + line[16:]
			elif line.startswith('LOCALENAME'):
				line = 'LOCALENAME\t"en-US"'
			elif line.startswith('LOCALEID'):
				line = 'LOCALEID\t"00000409"'
			elif line.startswith('0409\tFrench'):
				line = '0409\tEnglish (United States)'
			fout.write(line+'\r\n')

# rewrite input with CRLF
with open(inp,  encoding='utf8', mode='w') as fout:
	for line in lines:
		fout.write(line+'\r\n')
