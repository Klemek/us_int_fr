from os import listdir, remove



# get last version of french file
inp = sorted([f for f in listdir() if f.startswith('usinfr')])[-1]


def convert(code, name, localeid, localename):
	out = 'usin' + code + inp[6:]
	
	# delete english layout
	for f in sorted([f for f in listdir() if f.startswith('usin' + code)]):
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
					line = 'LOCALENAME\t"' + localename + '"'
				elif line.startswith('LOCALEID'):
					line = 'LOCALEID\t"' + localeid + '"'
				elif line.startswith('0409\tFrench'):
					line = '0409\t' + name
				fout.write(line+'\r\n')

	# rewrite input with CRLF
	with open(inp,  encoding='utf8', mode='w') as fout:
		for line in lines:
			fout.write(line+'\r\n')

	    
convert("us", "English (United States)", "00000409", "en-US")
convert("gb", "English (United Kingdom)", "00000809", "en-GB")

