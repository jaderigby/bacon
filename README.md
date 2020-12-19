# Bacon #

__Note:__ These instructions target mac and unix setups, atm.

Bacon is a utility for building other utilities. It helps generate a template for creating quick utilities run in bash (using alias commands) and written in Python.  In short, Bacon makes everything better!

## Setup ##

### Section 1 ###

__Note:__ If you would like to use the default setup, you can skip to _Section 2_ and run the commands listed.

First, create a directory called "bacon-bits".  Typically, this lives inside your "Documents" folder, but you can create it wherever you like.  Next, `cd` into the `bacon-bits` directory. So, for example:

```
cd ~/Documents && mkdir bacon-bits
```

Now, clone the bacon utility inside your `bacon-bits` directory.

```
cd bacon-bits
git clone git@github.com:jaderigby/bacon.git
```

Then, create a `.bashrc` file and add the following:

```
alias bacon="python ~/Documents/bacon-bits/bacon/baconActions.py"
```

__Note:__ If you created your `bacon-bits` file anywhere else, other than the `Documents` folder, you will need to modify the path above to point to wherever you installed bacon.

Once your .bashrc file is setup, add the following to your `.bash_profile` file.  (__Note:__ If you do not have a `.bash_profile` file, you can create one by going to your user's root directory and creating a file called `.bash_profile`):

```
source ~/Documents/bacon-bits/.bashrc
```

Finally, do:

```
source ~/.zshrc
```

__You are set!__

### Section 2 ###

If you are using the default setup, ie placing it inside the `Documents` folder, you can run the following commands for your setup:

```
cd ~/Documents && mkdir bacon-bits
cd bacon-bits
git clone git@github.com:jaderigby/bacon.git
touch .bashrc
echo "alias bacon=\"python ~/Documents/bacon-bits/bacon/baconActions.py\"" >> .bashrc
echo "source ~/Documents/bacon-bits/.bashrc" >> ~/.zshrc
source ~/.zshrc
```

## Usage ##

Type `bacon` in order to see the options.

### Create A New Utility ###

When creating a new utility, do:

```
bacon new
```

This command will walk you through creating a new utility.

### Adding An Action ###

To add a new action, do:

```
utilityName -action
```

To add a new action that supports parameters, do:

```
utilityName -action args:true
```

This will create a new action which can receive additional parameters as key/value pairs, seperated by a colon, such as:

```
myUtility create name:test
```

The above command will result in the following object being assigned to the "argDict" variable:

```
{"name" : "test"}
```

This can be consumed as `argDict['name']` resulting in the value `test`, such as:

```
helpers.write_file(argDict['name'] + '.txt', contents)
```

### Profile Command ###

If you want to create a profile file for your utility, do:

```
utilityName -profile
```

Each time you create a new utility (which adds a new alias to your `bacon-bits/.bashrc` file,) you will want to source the `.bashrc` file:

```
source <path-to-bacon-bits>/bacon-bits/.bashrc
```

### .bashrc Helper ###

Another way, is to create a helper inside of your `.bashrc` file using the following snippet:

```
baconFun() {
    baconActions=~/Dropbox/bacon-bits/bacon/baconActions.py
    if [ ! -z $1 ]; then
        if [ $1 = "set" ]; then
            source ~/Dropbox/bacon-bits/.bashrc
        else
            python $baconActions $1
        fi
    else
        python $baconActions
    fi
}
alias bacon="baconFun"
```

This should go at the top of your file.  Once in place, do:

```
source ~/.zshrc
```

Now, whenever you add a new bacon utility, run:

```
bacon set
```

Running the above command replaces the need to run `source <path-to-bacon-bits>/bacon-bits/.bashrc`.

### Utilities Observe The Following Behavior: ###

- Typing the name of the utility - or rather, its alias - shows the list of possible commands/actions.

- When invoking a utility, each utility follows the pattern: `<utility-name> <action>`

- Utilities come with a handful of `helpers` when writing your utility, that make writing utilities faster and easier.  These are common `helper` functions covering common actions that a typical utility might use.

## Terminology ##

__Utility:__ A Python script, or collection of scripts, accompanied by a bash alias for invoking those scripts.

__Action:__ A command added to a utility, such as `bacon new` where `new` is the action.

__Bacon:__ A simple utility that makes everything better!

## Structure ##

- __actions.py__ = where the action invocations are defined.
- __messages.py__ = where all messages are to be contained.  This keeps things clean and neat.
- __helpers.py__ = where all common functions should live.  A typical helpers file will contain any functions not defining specific business logic.
- __settings.py__ = where the settings definitions live.  This file typically does not need to be modified.
- __profiles folder__ = the profiles folder is where locally-specific settings live.  Any definition specific to a particular developers setup can be defined here, within a `profile.py` file.  This is also where any settings or task-specific data/definitions should live.  You can have multiple profile files inside the `profiles` folder.  Change which profile file your utility points to by changing the reference in the utility's `settings.py` file.
- __addAction.py__ = this runs when using the `-action` command. Used to add new actions to your utility.
- __profile.py__ = this is where locally-specific info can be stored/configured. For example, if two developers are using a utility, but have different configurations for that utility, the `profile.py` file is where these unique parts would be declared.
- __action-list.json__ = this is where the actions are described.  When you do your utility alias with no accompanying action command, this file is read, and the names and descriptions are listed. You can use this file to add descriptions for each of your utility's actions.

## Helpers ##

The helpers file is where you can include the functions that your utility uses.  This file is intended to include any non-business logic.  Bacon utilities come pre-configured with a handful of useful helper functions already.  These are listed below:

- __root()__ = returns the user's root directory path, such as doing `cd ~/`
- __self_path()__ = returns the directory path for the utility.
- __load_profile()__ & __get_settings()__ = these two functions are set up specifically for calling the settings.  If you want to use the settings in an action file, uncomment the commented settings line at the top of the file.
- __read_file()__ = opens a specified file.
- __write_file()__ = writes to a specified file with the data being passed in as the second parameter.
- __run_command()__ = runs a specified bash command. Also, it has an optional secondary parameter which accepts a boolean, to supress the output message. Example: `run_command('pwd', False)`. __Note:__ This can be a string or a list of single commands (each command to be chained together as a seperate item within the list, such as ['git', 'push']).
- __run_command_output()__ = runs a specified command and then returns the output.  Also, it has an optional secondary parameter which accepts a boolean, to supress the output message. Example: `run_command_output('pwd', False)`
- __titled()__ = converts any PascalCased/camelCased string to a title string, ie, a string with spaces and capitals at the beginning of each word.
- __kabob()__ = converts any PascalCased/camelCased string to a lowercase string seperated by dashes.
- __user_input__ = used to capture user inputs.
- __user_selection()__ = converts a specified list to an interactive selection, where each list item is numbered.  The first argument determins the string given as the input prompt.  If "x" is selected, or enter is pressed before a selection is made, then the function returns the string "exit".  Any other selection that is not a number, returns the error "Please select a valid entry" and allows the user to try again.
- __arguments()__ = use this to create a dictionary object for multiple command-line arguments.
- __profile()__ = creates a new profile folder and profile file wthen invoked.

## Bacon Profile ##

In addition to your utility having profiles, bacon has support for a `profile.py` file, as well.  In fact, if you are installing bacon anywhere else other than `Documents`, you can use a profile.py file to make it work.  Observe the following:

- __homeDir__ = to change the location to anything other than`Documents`, such as `"homeDir" : "Development"`. This would reference the `Development` directory, rather than the default `Documents` directory.
- __utilitiesPrimeDirectory__ = to change the bacon home folder to anything other than `bacon-bits`.
- __rcPath__ = to change the `.bashrc` reference to something else, such as `.baconrc`

To use these, create a new directory inside of the `bacon` directory, and call it `profiles`.  Then inside the `profiles` directory, create a file called `profile.py`.  Add the following to this file:

```
{
    "settings" : {

    }
}
```

Then, if you want to use one of the options above, such as `homeDir`, you would add the following:

```
{
    "settings" : {
        "homeDir" : "Development"
    }
}
```