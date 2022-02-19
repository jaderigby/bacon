#!/usr/bin/python

def main():

    def decorate(COLOR, STRING):
        bcolors = {
            'lilac' : '\033[95m'
            ,'blue' : '\033[94m'
            ,'cyan' : '\033[96m'
            ,'green' : '\033[92m'
            ,'yellow' : '\033[93m'
            ,'red' : '\033[91m'
            ,'bold' : '\033[1m'
            ,'underline' : '\033[4m'
            ,'endc' : '\033[0m'
        }

        return bcolors[COLOR] + STRING + bcolors['endc']

    def run_command(CMD, option = True):
        import subprocess
        shellStatus = True
        str = ''
        showCmd = CMD
        if isinstance(CMD, list):
            shellStatus = False
            for item in CMD:
                str += (' ' + item)
            showCmd = str
        if option:
            print('\n============== Running Command: {}\n'.format(showCmd))
        subprocess.call(CMD, shell=shellStatus)
    
    def verify_installation(CMD):
        import subprocess
        result  = False
        if CMD != None:
            process = subprocess.Popen(CMD, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            out, err = process.communicate()

            for line in out.splitlines():
                if not "command not found" in line:
                    result = True
    
    def handle_bacon():
        run_command('mkdir ~/Documents/bacon-bits && mv ~/Documents/bacon ~/Documents/bacon-bits/bacon')
        run_command('scp ~/Documents/bacon-bits/bacon/.baconrc ~/Documents/bacon-bits/.baconrc')
        run_command("echo 'source ~/Documents/bacon-bits/.baconrc' >> ~/.zshrc")
    

    #=============== Initialize ===============

    print(decorate('yellow', '\n\n============= 1. Checking/Installing Homebrew ... ============='))
    if verify_installation('brew --version') == True:
        run_command('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
    else:
        print(decorate('cyan', '\nHomebrew already installed. Moving on ...\n'))
    print(decorate('yellow', '============= 2. Checking/Installing git ... ============='))
    if verify_installation('git --version') == True:
        run_command('brew install git')
    else:
        print(decorate('cyan', '\ngit already installed. Moving on ...\n'))
    print(decorate('yellow', '============= 3. Initializing bacon ... ============='))
    handle_bacon()

    print('\n[ Process Completed ]\n')

if __name__ == '__main__':
    main()