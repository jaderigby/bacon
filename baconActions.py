import sys, create, helpers, baconAddAction
import baconMessages as msg
import baconUpdateHelpers
# new imports start here

# settings = helpers.get_settings()

try:
	action = str(sys.argv[1])
except:
	action = None

args = sys.argv[2:]

if action == None:
	msg.statusMessage()

elif action == 'new':
	create.execute()

elif action == '-action':
	baconAddAction.execute(args)

elif action == '-profile':
	helpers.profile()

elif action == "helpers":
	baconUpdateHelpers.execute()
# new actions start here