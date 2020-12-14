import json
from settings import settings

profilePath = settings['profile_url'] + settings['profile']

# path for current user. Example: "~/"
def root():
	import os
	return os.path.expanduser('~/')

# path to utility
def self_path():
	import os
	return os.path.dirname(os.path.realpath(__file__))

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

def run_command(CMD, option = True):
	import subprocess
	if option:
		print('\n============== Running Command: {}\n'.format(CMD))
	subprocess.call(CMD, shell=True)

def run_command_output(CMD, option = True):
	import subprocess
	if option:
		print('\n============== Outputting Command: {}\n'.format(CMD))
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

# processes string through titled function above; then, replaces spaces with dashes, such as: "NASA Satellite" to "nasa-satellite"
def kabob(NAME):
	str = titled(NAME)
	return str.replace(' ', '-').lower()

# generates a user selection session, where the passed in list is presented as numbered selections; selecting "x" or just hitting enter results in the string "exit" being returned. Any invaild selection is captured and presented with the message "Please select a valid entry"
def user_selection(DESCRIPTION, LIST):
	import re
	str = ''
	for i, item in enumerate(LIST, start=1):
		str += '\n[{index}] {item}'.format(index=i, item=item)
	str += '\n\n[x] Exit\n'

	finalAnswer = False

	while True:
		print(str)
		selection = raw_input('{}'.format(DESCRIPTION))
		pat = re.compile("[0-9]+")
		if pat.match(selection):
			selection = int(selection)
		if isinstance(selection, int):
			finalAnswer = selection
			break
		elif selection is 'x':
			finalAnswer = 'exit'
			break
		elif selection is '':
			finalAnswer = 'exit'
			break
		else:
			print("\nPlease select a valid entry...")
	return finalAnswer