import os, re, json

def execute(ROOT_DIR):
    def read_file(FILEPATH):
    	FILE = open(FILEPATH, 'r')
    	data = FILE.read()
    	FILE.close()
    	return data

    def write_file(FILEPATH, DATA):
    	FILE = open(FILEPATH, 'w')
    	FILE.write(DATA)
    	FILE.close()

    dirList = os.listdir(ROOT_DIR)
    index = 0
    newList = []
    newFeature = ''
    print
    for item in dirList:
        pat = "\."
        match = re.search(pat, item)
        if not match:
            index += 1
            print "[{}] {}".format(index, item)
            newList.append(item)
    selection = raw_input('''
[x] Exit

Selection: ''')
    if selection != 'x':
        selection = int(selection) - 1
        print '''
PROJECT: {}'''.format(newList[selection])
        fullPath = ROOT_DIR + '/' + newList[selection]
        newFeature = raw_input('''
-- New Feature --
Please give your new feature a name: ''')
        newAction = raw_input('''
What would you like to call the action? ''')

        template = '''import messages as msg

# settings = helpers.get_settings()

def execute():
    msg.example()
'''
        finalPath = fullPath + '/' + newFeature + '.py'
        print '''
PROJECT:        {}
NEW MODULE:     {}
NEW ACTION:     {}
LOCATION:       {}'''.format(newList[selection], newFeature, newAction, finalPath)
        write_file(finalPath, template)
        data = read_file(fullPath + '/actions.py')
        data = data.replace('# new imports start here', '''import {}
# new imports start here'''.format(newFeature))
        newContent = '''
elif action == "{newAction}":
    {newFeature}.execute()
# new actions start here'''.format(newFeature=newFeature, newAction=newAction)
        data = data.replace("# new actions start here", newContent)
        write_file(fullPath + '/actions.py', data)
        actionData = json.loads(read_file(fullPath + '/action-list.json'))
        # actionData['actions'].append('testingObj')
        newItem = {}
        newItem['name'] = newAction
        newItem['description'] = ''
        actionData['actions'].append(newItem)
        write_file(fullPath + '/action-list.json', json.dumps(actionData, indent=4))
    print
    print "[ Process Completed ]"
    print
