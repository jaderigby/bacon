import messages as msg
import os, re, json

def do_action(ARGS):
	import helpers
	argDict = helpers.arguments(ARGS)

	name = helpers.path('util').split('/')[-1]
	fullPath = helpers.path('util')
	titleString = "Action"
	if argDict:
		if 'args' in argDict:
			if argDict['args'] == 'true':
				titleString = "Action With Arguments"
	newFeature = helpers.user_input('''
-- New {} --
Please give your new action a name [Eg: OpenFile]: '''.format(titleString))
	newAction = helpers.user_input('''
What would you like to call the action? ''')

	basicSnippet = '''import messages as msg
import helpers

# settings = helpers.get_settings()

def execute():
	msg.example()
'''
	argSnippet = '''import messages as msg
import helpers

# settings = helpers.get_settings()

def execute(ARGS):
	argDict = helpers.arguments(ARGS)
	print(argDict)
'''
	finalPath = helpers.path('util') + '/' + newFeature + '.py'
	statusMsg = '''
NAME:           {}
NEW MODULE:     {}
NEW ACTION:     {}
LOCATION:       {}'''.format(name, newFeature, newAction, finalPath)
	print(statusMsg)
	template = basicSnippet
	if argDict:
		if 'args' in argDict:
			if argDict['args'] == 'true':
				template = argSnippet
	helpers.write_file(finalPath, template)
	data = helpers.read_file(fullPath + '/actions.py')
	data = data.replace('# new imports start here', '''import {}
# new imports start here'''.format(newFeature))

	basicContent = '''
elif action == "{newAction}":
	{newFeature}.execute()
# new actions start here'''.format(newFeature=newFeature, newAction=newAction)
	argContent = '''
elif action == "{newAction}":
	{newFeature}.execute(args)
# new actions start here'''.format(newFeature=newFeature, newAction=newAction)

	newContent = basicContent
	if argDict:
		if 'args' in argDict:
			if argDict['args'] == 'true':
				newContent = argContent
	data = data.replace("# new actions start here", newContent)
	helpers.write_file(fullPath + '/actions.py', data)
	actionData = json.loads(helpers.read_file(fullPath + '/action-list.json'))
	newItem = {}
	newItem['name'] = newAction
	newItem['description'] = ''
	actionData['actions'].append(newItem)
	helpers.write_file(fullPath + '/action-list.json', json.dumps(actionData, indent=4))
	msg.done()

def profile():
	import helpers
	import os
	utilDir = helpers.path('util')
	if not os.path.exists(utilDir + '/profiles/profile.py'):
		snippet = '''{\n\t"settings" : {\n\n\t\t}\n}'''
		helpers.run_command('mkdir {}/profiles'.format(utilDir), False)
		helpers.write_file(utilDir + '/profiles/profile.py', snippet)
		print("\nprofile added!\n")
		msg.done

def helpers():
	import helpers
	# get bacon filepath
	baconHelpersFilepath = helpers.run_command_output('cd {} && cd ../ && pwd'.format(helpers.path('util'))).replace('\n', '') + '/bacon/template/helpers.py'
	utilityHelpersFilepath = '/{}/{}'.format(helpers.path('util'), 'helpers.py')
	# get target helpers content
	content = helpers.read_file(utilityHelpersFilepath)
	customHelpers = content.split("# custom helpers start here\n# =========================")[1]
	# get default helpers template from bacon
	newDefaultHelpers = helpers.read_file(baconHelpersFilepath)
	# pack content and save
	newContent = newDefaultHelpers + customHelpers
	# print(newContent)
	helpers.write_file(utilityHelpersFilepath, newContent)
	msg.done()

def alias():
	import json
	import helpers
	actionList = json.loads(helpers.read_file('{}/{}'.format(helpers.path('util'), 'action-list.json')))
	bashrcFilepath = helpers.run_command_output('cd {} && cd ../'.format(helpers.path('util'))) + '.bashrc'
	contents = helpers.read_file(bashrcFilepath)
	pat = re.compile('alias {}='.format())
	match = re.search(pat, contents)
	formattedAlias = '\nalias {}="python {}/actions.py"'.format(actionList['alias'], helpers.path('util'))
	if not match:
		contents += formattedAlias
	helpers.write_file(bashrcFilepath, contents)