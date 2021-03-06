#===================================================================
#
#	HEADER
#
import sys, re, subprocess, os, helpers

#===================================================================

def execute():

	settings = helpers.get_settings()

	utilitiesPrimeDirectory = 'bacon-bits'
	if settings:
		if 'utilitiesPrimeDirectory' in settings:
			utilitiesPrimeDirectory = settings['utilitiesPrimeDirectory']

	rcPath = '.baconrc'
	if settings:
		if 'rcPath' in settings:
			rcPath = settings['rcPath']
	
	homeDir = 'Documents'
	if settings:
		if 'homeDir' in settings:
			homeDir = settings['homeDir']

	relativeUserPath = os.path.expanduser('~')
	origin = '{}/{}/'.format(relativeUserPath, homeDir)

	name = helpers.user_input("\nGive your tool a name [Eg: BaconUtil]: ")
	helpers.run_command('cp -r {ORIGIN}{UTILITIES_PRIME_DIRECTORY}/bacon/template {ORIGIN}{UTILITIES_PRIME_DIRECTORY}/{NAME}'.format(ORIGIN= origin, UTILITIES_PRIME_DIRECTORY= utilitiesPrimeDirectory, NAME= name), False)

	alias = helpers.user_input("\nWhat would you like the alias to be? ")

	def write_to_bashrc(FILEPATH, ALIAS, EXECUTE):
		if not os.path.exists(FILEPATH):
			subprocess.call(['touch', FILEPATH])
		FILE = open(FILEPATH, 'r')
		data = FILE.read()
		FILE.close()
		data = data + '\nalias ' + ALIAS + '=' + EXECUTE
		FILE = open(FILEPATH, 'w')
		FILE.write(data)
		FILE.close()

	def replace_generic_reference_with_actual(FILEPATH, NAME, PLACEHOLDER):
		FILE = open(FILEPATH, 'r')
		data = FILE.read()
		FILE.close()
		data = data.replace(PLACEHOLDER, NAME)
		FILE = open(FILEPATH, 'w')
		FILE.write(data)
		FILE.close()

	executionString = '"python {}{}/{}/actions.py"'.format(origin, utilitiesPrimeDirectory, name)

	write_to_bashrc('{}{}/{}'.format(origin, utilitiesPrimeDirectory, rcPath), alias, executionString)

	replace_generic_reference_with_actual('{}{}/{}/settings.py'.format(origin, utilitiesPrimeDirectory, name), name, '<tool-name>')
	replace_generic_reference_with_actual('{}{}/{}/messages.py'.format(origin, utilitiesPrimeDirectory, name), name, '<tool-name>')
	replace_generic_reference_with_actual('{}{}/{}/action-list.json'.format(origin, utilitiesPrimeDirectory, name), name, '<tool-name>')
	replace_generic_reference_with_actual('{}{}/{}/action-list.json'.format(origin, utilitiesPrimeDirectory, name), alias, '<alias>')

	statusMsg = '''
NAME:           {NAME}
ALIAS:          {ALIAS}
LOCATION:       {ORIGIN}{UTILITIES_PRIME_DIRECTORY}/{NAME}'''.format(NAME= name, ALIAS= alias, ORIGIN= origin, UTILITIES_PRIME_DIRECTORY= utilitiesPrimeDirectory)
	print(statusMsg)

	print('''
[ Process Complete ]
	''')