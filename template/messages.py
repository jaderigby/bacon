import helpers, json

actionList = json.loads(helpers.read_file('action-list.json'))

def statusMessage():
	if len(actionList['actions']) > 0:
		for item in actionList['actions']:
			print('''\n[ {} {} ]\t\t{}
'''.format(actionList['toolName'], item['name'], item['description']))
	else:
		print('''
<tool-name> is working successfully!
''')

def done():
	print('''
[ Process Completed ]
''')

def example():
	print('''
process working!
''')