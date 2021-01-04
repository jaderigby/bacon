import messages as msg
import os, re, json, helpers

def execute(ARGS):
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
