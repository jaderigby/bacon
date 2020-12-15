#===================================================================
#
#	HEADER
#
import sys, re, subprocess, os, helpers

from scab import scab as s

#===================================================================

def execute():

	settings = helpers.get_settings()

	utilitiesPrimeDirectory = 'bash-tools'
	if settings:
		if 'utilitiesPrimeDirectory' in settings:
			utilitiesPrimeDirectory = settings['utilitiesPrimeDirectory']

	rcPath = '.bashrc'
	if settings:
		if 'rcPath' in settings:
			rcPath = settings['rcPath']

	relativeUserPath = os.path.expanduser('~')
	origin = '{}/Documents/'.format(relativeUserPath)

	t = s()
	t.scan('{}{}/bacon/template'.format(origin, utilitiesPrimeDirectory))
	# t.reIgnore('(/\.+)|(create\.py)')
	t.record()
	name = helpers.user_input("Give your tool a name: ")
	t.build('{}/{}/{}'.format(origin, utilitiesPrimeDirectory, name))
	alias = helpers.user_input("What would you like the alias to be? ")

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

	print('''
[ Process Complete ]
	''') 