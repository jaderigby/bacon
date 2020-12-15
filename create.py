#===================================================================
#
#	HEADER
#
import sys, re, subprocess, os, helpers

from scab import scab as s

#===================================================================

def execute():

	settings = helpers.get_settings()

	if settings:
		utilities_prime_directory = settings['utilitiesPrimeDirectory']
	else:
		utilities_prime_directory = 'bash-tools'

	relativeUserPath = os.path.expanduser('~')
	origin = '{}/Documents/'.format(relativeUserPath)

	t = s()
	t.scan('{}{}/bacon/template'.format(origin, utilities_prime_directory))
	# t.reIgnore('(/\.+)|(create\.py)')
	t.record()
	name = helpers.user_input("Give your tool a name: ")
	t.build('{}/{}/{}'.format(origin, utilities_prime_directory, name))
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

	executionString = '"python {}{}/{}/actions.py"'.format(origin, utilities_prime_directory, name)

	write_to_bashrc('{}{}/.bashrc'.format(origin, utilities_prime_directory), alias, executionString)

	replace_generic_reference_with_actual('{}{}/{}/settings.py'.format(origin, utilities_prime_directory, name), name, '<tool-name>')
	replace_generic_reference_with_actual('{}{}/{}/messages.py'.format(origin, utilities_prime_directory, name), name, '<tool-name>')
	replace_generic_reference_with_actual('{}{}/{}/action-list.json'.format(origin, utilities_prime_directory, name), name, '<tool-name>')
	replace_generic_reference_with_actual('{}{}/{}/action-list.json'.format(origin, utilities_prime_directory, name), alias, '<alias>')

	print('''
[ Process Complete ]
	''') 