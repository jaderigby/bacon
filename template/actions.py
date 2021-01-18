import sys, sizzle
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
	sizzle.do_action(args)

elif action == '-profile':
	sizzle.profile()

elif action == '-helpers':
	sizzle.helpers()

elif action == '-alias':
	sizzle.alias()
# new actions start here
