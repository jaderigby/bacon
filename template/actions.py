import sys, action, status, helpers
# new imports start here

# settings = helpers.get_settings()

try:
	action = str(sys.argv[1])
except:
	action = None

if action == 'status' or action == None:
	status.execute()

elif action == 'action':
	# You will want to change the name to something specific, when developing
	action.execute()
# new actions start here
