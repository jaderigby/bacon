import sys, addAction, helpers
import messages as msg
# new imports start here

# settings = helpers.get_settings()

try:
	action = str(sys.argv[1])
except:
	action = None

args = sys.argv[2:]

if action == None:
	msg.statusMessage()

elif action == '-action':
	addAction.execute()

elif action == '-profile':
	helpers.profile()
# new actions start here
