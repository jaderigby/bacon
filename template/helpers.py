import json
from settings import settings

profilePath = settings['profile_url'] + settings['profile']

def load_profile():
	return json.loads(read_file(profilePath))

def get_settings():
	profile = load_profile()
	return profile['settings']

def read_file(FILEPATH):
	FILE = open(FILEPATH, 'r')
	data = FILE.read()
	FILE.close()
	return data

def write_file(FILEPATH, DATA):
	FILE = open(FILEPATH, 'w')
	FILE.write(DATA)
	FILE.close()

def run_command(CMD):
	import subprocess
	print('\n============== Running Command: {}\n'.format(CMD))
	subprocess.call(CMD, shell=True)

def run_command_output(CMD):
	import subprocess
	print('\n============== Running Command: {}\n'.format(CMD))
	result = False
	if CMD != None:
		process = subprocess.Popen(CMD, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
		out, err = process.communicate()

		if err:
			print(err)
		
		else:
			result = out

	return result

# returns PascalCased/camelCased strings as strings with spaces. Acronyms, such as NASASatellite will resolve to "NASA Satellite"
# Be advised: does not account for numbers
def titled(NAME):
	import re
	charList = []
	pat = re.compile('[A-Z]')
	nameList = list(NAME)
	for i, char in enumerate(nameList):
		if (i + 1 < len(nameList) and i - 1 >= 0):
			up_ahead = nameList[i + 1]
			from_behind = nameList[i - 1]
		else:
			up_ahead = ''
			from_behind = ''
		if pat.match(char) and i != 0:
			if pat.match(from_behind) and pat.match(up_ahead):
				charList.append(char)
			else:
				charList.append(' ')
				charList.append(char)
		else:
			charList.append(char)
	return ''.join(charList)

def kabob(NAME):
	str = titled(NAME)
	return str.replace(' ', '-').lower()