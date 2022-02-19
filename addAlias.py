import baconMessages as msg
import helpers, os, re

settings = helpers.get_settings()

def execute():
	baconBitsPath = helpers.run_command_output('cd {} && cd ../ && pwd'.format(helpers.path('util')), False).replace('\n', '')
	baconrcFile = baconBitsPath + '/.baconrc'
	DATA = helpers.read_file(baconrcFile)
	utilList = os.listdir(baconBitsPath)
	addPerks = helpers.kv_set(settings, 'perks')
	count = 0
	# print(utilList)
	print(addPerks)
	APPENDED_DATA_STR = DATA
	for item in utilList:
		path = baconBitsPath + '/' + item
		try:
			alias = helpers.get_alias(path)
		except:
			alias = False
		if alias:
			aliasStr = 'alias {ALIAS}="python {PATH}/actions.py"'.format(ALIAS= alias, PATH= path)
			# print(aliasStr)
			pat = re.compile(aliasStr)
			match = re.search(pat, DATA)
			if not match:
				count += 1
				print('\nadding alias: {}'.format(alias))
				APPENDED_DATA_STR += '\n' + aliasStr
				if addPerks:
					aliasStrGoto = '''        elif [ $1 = "{ALIAS}" ]; then
                cd {PATH}
            #~~~ bacon:goto placeholder'''.format(ALIAS= alias, PATH= path)
					aliasStrShow = '''        elif [ $1 = "{ALIAS}" ]; then
                open {PATH}
            #~~~ bacon:show placeholder'''.format(ALIAS= alias, PATH= path)
					APPENDED_DATA_STR = APPENDED_DATA_STR.replace('        #~~~ bacon:goto placeholder', aliasStrGoto)
					APPENDED_DATA_STR = APPENDED_DATA_STR.replace('        #~~~ bacon:show placeholder', aliasStrShow)
	if count > 0:
		helpers.write_file(baconrcFile, APPENDED_DATA_STR)
	else:
		print("\n:: Nothing to add ::")

	msg.done()
