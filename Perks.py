import baconMessages as msg
import helpers, os, re

# settings = helpers.get_settings()

def execute():
	baconBitsPath = helpers.run_command_output('cd {} && cd ../ && pwd'.format(helpers.path('util')), False).replace('\n', '')
	baconrcFile = baconBitsPath + '/.baconrc'
	DATA = helpers.read_file(baconrcFile)
	utilList = os.listdir(baconBitsPath)
	count = 0
	# print(utilList)
	MODIFIED_DATA_STR = DATA
	for item in utilList:
		path = baconBitsPath + '/' + item
		try:
			alias = helpers.get_alias(path)
		except:
			alias = False
		if alias:
			aliasStr1 = '''        elif [ $1 = "{ALIAS}" ]; then
            cd {PATH}
        #~~~ bacon:goto placeholder'''.format(ALIAS= alias, PATH= path)
			aliasStr2 = '''        elif [ $1 = "{ALIAS}" ]; then
            open {PATH}
        #~~~ bacon:show placeholder'''.format(ALIAS= alias, PATH= path)
			pat = re.compile('elif \[ \$1 = "{ALIAS}" \]; then'.format(ALIAS = alias))
			match = re.search(pat, DATA)
			if not match:
				count += 1
				print('\nadding utility to goto: {}'.format(alias))
				MODIFIED_DATA_STR = MODIFIED_DATA_STR.replace('        #~~~ bacon:goto placeholder', aliasStr1)
				MODIFIED_DATA_STR = MODIFIED_DATA_STR.replace('        #~~~ bacon:show placeholder', aliasStr2)
	if count > 0:
		helpers.write_file(baconrcFile, MODIFIED_DATA_STR)
	else:
		print("\n:: Nothing to add ::")

	msg.done()
