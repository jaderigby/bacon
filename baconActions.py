import sys, create

# settings = helpers.get_settings()

try:
	action = str(sys.argv[1])
except:
	action = None

if action == None:
	print('''
[ new ]		Create a new item
[ export ]	Export a single action
''')

elif action == 'new':
	create.execute()
