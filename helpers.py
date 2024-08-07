import json
from settings import settings

profilePath = settings['profile_url'] + settings['profile']

def load_profile():
	import os
	if os.path.exists(profilePath):
		return json.loads(read_file(profilePath))
	else:
		return json.loads("{}")

def get_settings():
	profile = load_profile()
	if 'settings' in profile:
		return profile['settings']
	else:
		return settings

def user_input(STRING):
	try:
		return raw_input(STRING)
	except:
		return input(STRING)

def read_file(FILEPATH):
	FILE = open(FILEPATH, 'r')
	data = FILE.read()
	FILE.close()
	return data

def write_file(FILEPATH, DATA):
	with open(FILEPATH, 'w') as f: f.write(DATA)

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
			result = out.decode('utf-8')

	return result

def path(TYPE):
	import os
	if TYPE == 'user':
		return os.path.expanduser('~/')
	elif TYPE == 'util' or TYPE == 'utility':
		return os.path.dirname(os.path.realpath(__file__))
	elif TYPE == 'current':
		return run_command_output('pwd', False).replace('\n', '')
	else:
		return False

def decorate(COLOR, STRING):
	bcolors = {
		 'lilac' : '\033[95m'
		,'blue' : '\033[94m'
		,'cyan' : '\033[96m'
		,'green' : '\033[92m'
		,'yellow' : '\033[93m'
		,'red' : '\033[91m'
		,'bold' : '\033[1m'
		,'underline' : '\033[4m'
		,'endc' : '\033[0m'
	}

	return bcolors[COLOR] + STRING + bcolors['endc']

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
		selection = user_input('{}'.format(DESCRIPTION))
		pat = re.compile("[0-9]+")
		if pat.match(selection):
			selection = int(selection)
		if isinstance(selection, int):
			finalAnswer = selection
			break
		elif selection == 'x':
			finalAnswer = 'exit'
			break
		elif selection == '':
			finalAnswer = 'exit'
			break
		else:
			print("\nPlease select a valid entry...")
	return finalAnswer

def arguments(ARGS, DIVIDER=':'):
	ARGS_FORMATTED = []
	for item in ARGS:
		if DIVIDER not in item:
			ARGS_FORMATTED.append('{}:t'.format(item))
		else:
			ARGS_FORMATTED.append(item)
	return dict(item.split('{}'.format(DIVIDER), 1) for item in ARGS_FORMATTED)

def get_alias(FILEPATH):
	actionList = json.loads(read_file('{}/{}'.format(FILEPATH, 'action-list.json')))
	alias = actionList['alias']
	return alias

def kv_set(DICT, KEY, DEFAULT = False):
	if KEY in DICT:
		DICT[KEY] = 't' if DICT[KEY] == 'true' else 'f' if DICT[KEY] == 'false' else DICT[KEY]
		return DICT[KEY]
	else:
		return DEFAULT

def profile():
	import baconMessages as msg
	import os
	utilDir = path('util')
	if not os.path.exists(utilDir + '/profiles/profile.py'):
		snippet = '''{\n\t"settings" : {\n\n\t\t}\n}'''
		run_command('mkdir {}/profiles'.format(utilDir), False)
		write_file(utilDir + '/profiles/profile.py', snippet)
		print("\nprofile added!\n")
		msg.done()