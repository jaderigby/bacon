# Bacon #

Bacon is a utility for building other utilities. It helps generate a template for creating quick utilities run in bash (using alias commands) and written in Python.  In short, Bacon makes everything better!

## Setup ##

### Section 1 ###

__Note:__ If you would like to use the default setup, you can skip to _Section 2_ and run the commands listed.

First, create a directory called "bash-tools".  Typically, this lives inside your "Documents" folder, but you can create it wherever you like.  Next, `cd` into the `bash-tools` directory. So, for example:

```
cd ~/Documents && mkdir bash-tools
cd bash-tools
```

Now, clone the bacon utility inside your `bash-tools` directory.

```
git clone git@github.com:jaderigby/bacon.git
```

Then, create a `.bashrc` file and add the following:

```
alias bacon="python ~/Documents/bash-tools/bacon/baconActions.py"
```

__Note:__ If you created your `bash-tools` file anywhere else, other than the `Documents` folder, you will need to modify the path above to point to wherever you installed bacon.

Once your .bashrc file is setup, add the following to your `.bash_profile` file.  If you do not have a `.bash_profile` file, you can add it by going to your user's root directory and creating a file called `.bash_profile`:

```
source ~/Documents/bash-tools/.bashrc
```

Finally, do:

```
source ~/.bash_profile
```

__You are set!__

### Section 2 ###

If you are using the default setup, ie placing it inside the `Documents` folder, you can run the following commands for your setup:

```
cd ~/Documents && mkdir bash-tools
cd bash-tools
git clone git@github.com:jaderigby/bacon.git
cd ~/Documents/bash-tools && touch .bashrc
echo "alias bacon=\"python ~/Documents/bash-tools/bacon/baconActions.py\"" >> .bashrc
echo "source ~/Documents/bash-tools/.bashrc" >> ~/.bash_profile
source ~/.bash_profile
```

## Usage ##

Type `bacon` in order to see the options.

When creating a new utility, do:

```
bacon new
```

This will walk you through creating a new utility.

When adding an action to an existing utility, do:

```
bacon add
```

This will scan the `bash-tools` directory and list all folders, ie all utilities, for selection.  Select the utility which you would like to add an action to.

Utilities observe the following behavior:

- Typing the name of the utility - or rather - its alias, shows the list of possible commands/attributes.

- When invoking a utility, each utility follows the pattern: `<utility-name> <action>`

- Utilities come with a handful of `helpers` when writing your utility, that make writing utilities easier.  These are common `helper` functions covering common actions that a typical utility might use.

## Terminology ##

__Utility:__ A Python script, or collection of scripts, accompanied by a bash alias for invoking said script.

__Action:__ A command added to a utility, such as `bacon add` where `add` is the action.

__Bacon:__ A simple utility that makes everything better!

## Structure ##

- __actions.py__ = where the action invocations are defined.
- __messages.py__ = where all messages are to be contained.  This keeps things clean and neat.
- __helpers.py__ = where all common functions should live.  A typical helpers file will contain any functions not defining specific business logic.
- __settings.py__ = where the settings definitions live.  This file typically does not need to be modified.
- __profiles folder__ = the profiles folder is where locally-specific settings live.  Any definition specific to a particular developers setup can be defined here.  This is also where any settings or task-specific data/definitions should live.  You can have multiple profile files inside the `profiles` folder.  Change which profile file your utility points to by changing the reference in the utility's `settings.py` file.
- __profile.py__ = an example profile file.
- __status.py__ = the status file is simply for running the `status` attribute in order to verify setup in the beginning. This can be modified and used however you like or you may remove this file and its accompanying reference in the `actions.py` file.
- __action-list.json__ = this is where the actions are described.  When you do `myUtility status`, this file is read, and the names and descriptions are listed. You can use this file to add descriptions for each of your utility's actions.
- __action.py__ = an example of a typical action file.  This can also be removed, along with its reference inside the `actions.py` file.

## Helpers ##

The helpers file is where you can include the functions that your utility uses.  This file is intended to include any non-business logic.  Bacon utilities come pre-configured with a handful of useful helper functions already.  These are listed below:

- __root()__ = returns the user's root directory path, such as doing `cd ~/`
- __self_path()__ = returns the directory path for the utility.
- __load_profile()__ & __get_settings()__ = these two functions are set up specifically for calling the settings.  If you want to use the settings in an action file, uncomment the commented settings line at the top of the file.
- __read_file()__ = opens a specified file
- __write_file()__ = writes to a specified file the data passed in as the second argument
- __run_command()__ = runs a specified bash command. Also, it has an optional secondary argument which accepts a boolean, to supress the output message. Example: `run_command('pwd', False)`
- __run_command_output()__ = runs a specified command and then returns the output.  Also, it has an optional secondary argument which accepts a boolean, to supress the output message. Example: `run_command_output('pwd', False)`
- __titled()__ = converts any PascalCased/camelCased string to a title string, ie, a string with spaces and capitals at the beginning of each word.
- __kabob()__ = converts any PascalCased/camelCased string to a lowercase string seperated by dashes.
- __user_selection()__ = converts a specified list to an interactive selection, where each list item is numbered.  The first argument determins the string given as the input prompt.  If "x" is selected, or enter is pressed before a selection is made, then the function returns the string "exit".  Any other selection that is not a number, returns the error "Please select a valid entry" and allows the user to try again.