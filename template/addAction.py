import messages as msg
import os, re, json, helpers

def execute():
	name = helpers.self_path().split('/')[-1]
	fullPath = helpers.self_path()
	newFeature = helpers.user_input('''
-- New Action --
Please give your new action a name [Eg: OpenFile]: ''')
	newAction = helpers.user_input('''
What would you like to call the action? ''')

	template = '''import messages as msg

# settings = helpers.get_settings()

def execute():
    msg.example()
'''
	finalPath = helpers.self_path() + '/' + newFeature + '.py'
	print('''
NAME:           {}
NEW MODULE:     {}
NEW ACTION:     {}
LOCATION:       {}''').format(name, newFeature, newAction, finalPath)
	helpers.write_file(finalPath, template)
	data = helpers.read_file(fullPath + '/actions.py')
	data = data.replace('# new imports start here', '''import {}
# new imports start here'''.format(newFeature))
	newContent = '''
elif action == "{newAction}":
    {newFeature}.execute()
# new actions start here'''.format(newFeature=newFeature, newAction=newAction)
	data = data.replace("# new actions start here", newContent)
	helpers.write_file(fullPath + '/actions.py', data)
	actionData = json.loads(helpers.read_file(fullPath + '/action-list.json'))
	newItem = {}
	newItem['name'] = newAction
	newItem['description'] = ''
	actionData['actions'].append(newItem)
	helpers.write_file(fullPath + '/action-list.json', json.dumps(actionData, indent=4))
	msg.done()
