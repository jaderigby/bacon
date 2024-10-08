import json
from settings import settings

profilePath = settings['profile_url'] + settings['profile']

def load_profile():
	import os
	return json.loads(read_file(profilePath)) if os.path.exists(profilePath) else json.loads("{}")

def get_settings():
	profile = load_profile()
	if 'settings' in profile:
		for key in profile['settings']:
			settings[key] = profile['settings'][key]
	return settings

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

def read_file(FILEPATH):
	FILE = open(FILEPATH, 'r')
	data = FILE.read()
	FILE.close()
	return data

def write_file(FILEPATH, DATA):
	with open(FILEPATH, 'w') as f: f.write(DATA)

def ls_dir(PATH):
	import os
	return [d for d in os.listdir(PATH) if os.path.isdir(os.path.join(PATH, d))]

def run_command(CMD, option = True):
	import subprocess
	shellStatus = True
	str = ''
	showCmd = CMD
	if isinstance(CMD, list):
		shellStatus = False
		for item in CMD:
			str += (' ' + item)
		showCmd = str
	if option:
		print('\n============== Running Command: {}\n'.format(showCmd))
	subprocess.call(CMD, shell=shellStatus)

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

def user_input(STRING):
	try:
		return raw_input(STRING)
	except:
		return input(STRING)

def list_expander(LIST):
    baseList = LIST.replace(' ', '').split(',')
    expandedList = []
    for item in baseList:
        if '-' in item:
            rangeList = item.split('-')
            tempList = [elem for elem in range(int(rangeList[0]), int(rangeList[1]) + 1)]
            expandedList += tempList
        else:
            expandedList.append(int(item))
    return expandedList

# generates a user selection session, where the passed in list is presented as numbered selections; selecting "x" or just hitting enter results in the string "exit" being returned. Any invaild selection is captured and presented with the message "Please select a valid entry"
def user_selection(DESCRIPTION, LIST, LIST_SELECT = False, DETAILED = False):
	import re
	str = ''
	for i, item in enumerate(LIST, start=1):
		str += '\n[{index}] {item}'.format(index=i, item=item)
	str += '\n\n[x] Exit\n'

	finalAnswer = False

	while True:
		print(str)
		selection = user_input('{}'.format(DESCRIPTION))
		pat = re.compile("[0-9,\- ]+") if LIST_SELECT else re.compile("[0-9]+")
		if pat.match(selection):
			selection = list_expander(selection) if LIST_SELECT else int(selection)
		if isinstance(selection, int) or isinstance(selection, list):
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
	
	finalAnswerObj = {}
	
	if finalAnswer == 'exit':
		return finalAnswer
	
	else:
		if isinstance(finalAnswer, list):
			finalAnswerObj = []
			for item in finalAnswer:
				tempObj = {}
				tempObj['option'] = item
				tempObj['index'] = item - 1
				tempObj['value'] = LIST[item - 1]
				finalAnswerObj.append(tempObj)
		else:
			finalAnswerObj['option'] = finalAnswer
			finalAnswerObj['index'] = finalAnswer - 1
			finalAnswerObj['value'] = LIST[finalAnswer - 1]
	if DETAILED:
		return finalAnswerObj
	else:
		return finalAnswerObj['option']

def arguments(ARGS, DIVIDER=':'):
	import re

	ARGS_FORMATTED = {}
	pat = re.compile('[a-zA-Z0-9]*:[\w\,_-{]*:')
	
	for item in ARGS:

		if DIVIDER not in item:
			ARGS_FORMATTED[item] = 't'
		elif pat.match(item):
			parsed = item.replace('{','').replace('}','').split(':')
			itemParentKey = parsed[0]
			itemKey  = parsed[1]
			itemValue = parsed[2]
			if itemParentKey in ARGS_FORMATTED:
				ARGS_FORMATTED[itemParentKey][itemKey] = itemValue
			else:
				newObj = {}
				newObj[itemKey] = itemValue
				ARGS_FORMATTED[itemParentKey] = newObj
		else:
			parsed = item.split(':')
			itemKey  = parsed[0]
			itemValue = parsed[1]
			ARGS_FORMATTED[itemKey] = itemValue
	
	return ARGS_FORMATTED

def kv_set(DICT, KEY, DEFAULT = False):
	if KEY in DICT:
		DICT[KEY] = 't' if DICT[KEY] == 'true' else 'f' if DICT[KEY] == 'false' else DICT[KEY]
		return DICT[KEY]
	else:
		return DEFAULT


# custom helpers start here
# =========================