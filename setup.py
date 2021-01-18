import helpers, os, re

# need to run "python bacon/setup.py"
baconPath = helpers.path('util')

baconrcFile = helpers.run_command_output('cd {} && cd ../ && pwd'.format(baconPath), False).replace('\n', '') + '/.baconrc'

aliasSnippet = '''baconFun() {{
    baconActions={}/baconActions.py
    if [ ! -z $1 ]; then
        if [ $1 = "set" ]; then
            source {}
        else
            python $baconActions $1
        fi
    else
        python $baconActions
    fi
}}
alias bacon="baconFun"'''.format(baconPath, baconrcFile)

alias = aliasSnippet

if not os.path.exists(baconrcFile):
    helpers.write_file(baconrcFile, alias)
else:
    DATA = helpers.read_file(baconrcFile)
    pat = re.compile(alias)
    if not pat.match(DATA):
        APPENDED_DATA = DATA + '\n' + alias
        helpers.write_file(baconrcFile, APPENDED_DATA)