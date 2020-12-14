import sys, create, addBacon

# settings = helpers.get_settings()

try:
	action = str(sys.argv[1])
except:
	action = None

if action == None:
	print('''
[ new ]		Create a new item
[ add ]		Add an action
''')

elif action == 'new':
	create.execute()

elif action == 'add':
	origin = str(sys.argv[0].replace('/bacon/baconActions.py', ''))
	addBacon.execute(origin)
