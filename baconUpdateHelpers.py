import baconMessages as msg
import re, helpers

# settings = helpers.get_settings()

def execute():
	# select utility to update
	utilityList = helpers.run_command_output('cd {} && ls ../'.format(helpers.path('util'))).split()
	selection = helpers.user_selection('Select utility to update: ', utilityList)
	if selection != 'exit':
		selectedUtility = utilityList[selection - 1]
		print('\nYou have selected: {}'.format(helpers.decorate('green', selectedUtility)))
		baconBitsFilepath = helpers.run_command_output('cd {} && cd ../ && pwd'.format(helpers.path('util'))).replace('\n', '')
		utilityHelpersFilepath = baconBitsFilepath + '/{}/{}'.format(selectedUtility, 'helpers.py')
		# get target helpers content
		content = helpers.read_file(utilityHelpersFilepath)
		customHelpers = content.split("# custom helpers start here\n# =========================")[1]
		# get default helpers template from bacon
		newDefaultHelpers = helpers.read_file('{}/template/helpers.py'.format(helpers.path('util')))
		# pack content and save
		newContent = newDefaultHelpers + customHelpers
		# print(newContent)
		helpers.write_file(utilityHelpersFilepath, newContent)
	msg.done()