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
		return False

def user_input(STRING):
    try: 
        input = raw_input
    except NameError:
        pass
    return input(STRING)

def read_file(FILEPATH):
	FILE = open(FILEPATH, 'r')
	data = FILE.read()
	FILE.close()
	return data