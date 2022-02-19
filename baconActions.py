import sys, create, helpers, baconAddAction
import baconMessages as msg
import addAlias
import Perks
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

elif action == "alias":
	addAlias.execute()

elif action == "perks":
	Perks.execute()
# new actions start here